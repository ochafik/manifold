#
# cd bindings/python_cffi
# ( mkdir -p ../../build && cd ../../build && cmake -DCMAKE_BUILD_TYPE=Release -DMANIFOLD_CBIND=ON -DBUILD_SHARED_LIBS=ON -DMANIFOLD_PAR=TBB .. && make -j6 )
# ( mkdir -p ../../build && cd ../../build && cmake -DCMAKE_BUILD_TYPE=Release -DMANIFOLD_CBIND=ON -DBUILD_SHARED_LIBS=OFF -DMANIFOLD_PAR=TBB .. && make -j6 )
# python regenerate.py && python example.py
# hyperfine --warmup=1  -L ffi CFFI,NANOBIND "FFI={ffi} python example.py"
#
# MANIFOLD_LIBRARY=../../build/bindings/c/libmanifoldc.dylib python example.py
# hyperfine --warmup=1  -L ffi CFFI,NANOBIND "FFI={ffi} MANIFOLD_LIBRARY=../../build/bindings/c/libmanifoldc.dylib python example.py"

import os

_ffi = os.environ.get('FFI', 'CFFI')
if _ffi == 'NANOBIND':
  from manifold3d import Manifold, Mesh
elif _ffi == 'CFFI':
  from manifold3d_cffi import Manifold, Mesh
else:
  raise Exception(f'Invalid FFI: {_ffi}')

objs = [Manifold.sphere(i, 100).translate((i, 0, 0)) for i in range(100)]
# objs = [Manifold.cube((i, 1, 1)).translate((i, 0, 0)) for i in range(1000)]
out = sum(objs, Manifold())

# a = Manifold.sphere(1, 10)
# b = Manifold.sphere(2, 10).translate((1, 0, 0))
# out = a + b

m = out.to_mesh()
v = m.vert_properties
t = m.tri_verts
print(f'v: {v.shape} = {v}')
print(f't: {t.shape} = {t}')
