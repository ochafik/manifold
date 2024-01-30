"""
  Alternative Python bindings for the manifold library.

  See https://cffi.readthedocs.io/en/latest/cdef.html for more on cffi.
"""

try:
    from manifold3d_cffi.cffi import ffi as ffi, lib as lib
except ImportError as e:
    raise ImportError(f"Couldn't find manifold bindings ({e}). Run `python regenerate.py` or check your PYTHONPATH.")

# import os, platform

# __exact_library = os.environ.get("MANIFOLD_LIBRARY")
# if __exact_library:
#     __candidates = [__exact_library]
# elif platform.system() == "Windows":
#     __candidates = ["manifold.dll"]
# else:
#     __candidates = ["libmanifold.so", "libmanifold.so"]
#     if platform.system() == "Darwin":
#         __candidates += ["libmanifold.dylib"]

# for i, name in enumerate(__candidates):
#     try:
#         # This is where all the functions, enums and constants are defined
#         lib = ffi.dlopen(name)
#     except OSError:
#         if i < len(__candidates) - 1:
#             continue
#         raise OSError(f"Couldn't find manifold's shared library (tried names: {__candidates}). Add its directory to DYLD_LIBRARY_PATH (on Mac) or LD_LIBRARY_PATH, or define MANIFOLD_LIBRARY.")

# This contains the cffi helpers such as new, cast, string, etc.
# https://cffi.readthedocs.io/en/latest/ref.html#ffi-interface
ffi = ffi

from typing import Callable, Optional, Tuple
import numpy as np

# c_lib = ffi.dlopen(None)
# print(c_lib)
# print([n for n in dir(lib) if 'malloc' in n])
# print(dir(lib))
# # malloc = c_lib.malloc
# malloc = ffi.def_extern("malloc")
# print(f'malloc = {malloc}')
# # from _cffi_backend import load_library

def _new_meshgl_ptr(f: Callable[[ffi.CData], ffi.CData]):
  return ffi.gc(f(lib.malloc(lib.manifold_meshgl_size())), lib.manifold_delete_meshgl)
  # return ffi.gc(f(ffi.new("char[]", lib.manifold_meshgl_size())), lib.manifold_delete_meshgl)

def _new_manifold_ptr(f: Callable[[ffi.CData], ffi.CData]):
  return ffi.gc(f(lib.malloc(lib.manifold_manifold_size())), lib.manifold_delete_manifold)
  # return ffi.gc(f(ffi.new("char[]", lib.manifold_manifold_size())), lib.manifold_delete_manifold)

class Mesh:
  def __init__(self, vert_properties: Optional[np.ndarray] = None, tri_verts: Optional[np.ndarray] = None, *, mem: Optional[ffi.CData] = None):
    if mem is not None:
      assert vert_properties is None and tri_verts is None
      self.mem = mem
      # self._tri_verts = None
      # self._vert_properties = None
    else:
      assert vert_properties is not None and tri_verts is not None
      vert_properties_shape=vert_properties.shape
      tri_verts_shape=tri_verts.shape
      assert len(vert_properties_shape) == 2 and vert_properties.dtype == float
      assert len(tri_verts_shape) == 2 and tri_verts_shape[1] == 3 and tri_verts_shape.dtype == int

      tri_verts = tri_verts.ascontiguousarray()
      vert_properties = vert_properties.ascontiguousarray()
      # self._tri_verts = tri_verts
      # self._vert_properties = vert_properties

      n_tris=tri_verts_shape[0]
      n_verts=vert_properties_shape[0]
      n_props=vert_properties_shape[1]
      assert n_props >= 3
      assert n_tris >= 4
      assert n_verts >= 3

      self.mem = _new_meshgl_ptr(
        lambda mem:
          lib.manifold_meshgl(mem,
            vert_props=ffi.from_buffer(vert_properties),
            n_verts=n_verts,
            n_props=n_props,
            tri_verts=ffi.from_buffer(tri_verts),
            n_tris=n_tris))
      
  @property
  def tri_verts(self):
    n_tris = lib.manifold_meshgl_tri_length(self.mem) // 3
    tri_verts = np.ndarray((n_tris, 3), dtype=np.uint32)
    lib.manifold_meshgl_tri_verts(ffi.from_buffer(tri_verts), self.mem)
    return tri_verts
  
  @property
  def vert_properties(self):
    n_verts=lib.manifold_meshgl_num_vert(self.mem)
    n_props=lib.manifold_meshgl_num_prop(self.mem)
    vert_properties=np.ndarray((n_verts, n_props), dtype=np.float32)
    length=lib.manifold_meshgl_vert_properties_length(self.mem)
    assert length == n_verts * n_props
    lib.manifold_meshgl_vert_properties(ffi.from_buffer(vert_properties), self.mem)
    return vert_properties

class Manifold:
  def __init__(self, mesh: Optional[Mesh] = None, mem: Optional[ffi.CData]=None):
    if mem is not None:
      assert mesh is None
      self.mem = mem
    elif mesh is not None:
      self.mem = _new_manifold_ptr(lambda mem: lib.manifold_of_meshgl(mem, mesh))
    else:
      self.mem = _new_manifold_ptr(lambda mem: lib.manifold_empty(mem))

  def __add__(self, other: 'Manifold') -> 'Manifold':
    return Manifold(mem=_new_manifold_ptr(lambda mem: lib.manifold_union(mem, self.mem, other.mem)))
  
  def __sub__(self, other: 'Manifold') -> 'Manifold':
    return Manifold(manifold=_new_manifold_ptr(lambda mem: lib.manifold_difference(mem, self.manifold, other.manifold)))
  
  def __xor__(self, other: 'Manifold') -> 'Manifold':
    return Manifold(manifold=_new_manifold_ptr(lambda mem: lib.manifold_intersection(mem, self.manifold, other.manifold)))
    
  def to_mesh(self):
    return Mesh(mem=_new_meshgl_ptr(lambda mem: lib.manifold_get_meshgl(mem, self.mem)))
  
  def translate(self, v: Tuple[float, float, float]):
    (x, y, z) = v
    return Manifold(mem=_new_manifold_ptr(lambda mem: lib.manifold_translate(mem, self.mem, x, y, z)))
    
  @staticmethod
  def sphere(radius, circular_segments):
    return Manifold(mem=_new_manifold_ptr(lambda mem: lib.manifold_sphere(mem, radius, circular_segments)))

  @staticmethod
  def cube(size, center=False):
    (x, y, z) = size
    return Manifold(mem=_new_manifold_ptr(lambda mem: lib.manifold_cube(mem, x, y, z, center)))
