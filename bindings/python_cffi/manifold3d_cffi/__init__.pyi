# auto-generated file
import manifold3d_cffi.ffi as ffi
import numpy as np
from typing import Union

class ffi:
  def typeof(x) -> ffi.CType: ...
  def new(type: ffi.CType, *args, **kwargs) -> ffi.CData: ...
  def cast(type: Union[ffi.CType, str], data: ffi.CData) -> ffi.CData: ...
  def from_buffer(data: Union[bytes, bytearray, memoryview]) -> ffi.CData: ...
  def buffer(data: ffi.CData, size: int) -> Union[bytes, bytearray, memoryview]: ...
  def string(data: ffi.CData) -> str: ...

class lib:
  def malloc(size: int) -> ffi.CData:
    """void *malloc(size_t size);"""
    ...
  def manifold_as_original(mem: ffi.CData, m: ffi.CData) -> ffi.CData:
    """ManifoldManifold *manifold_as_original(void *mem, ManifoldManifold *m);"""
    ...
  def manifold_batch_boolean(mem: ffi.CData, ms: ffi.CData, op: ffi.CData) -> ffi.CData:
    """
    ManifoldManifold *manifold_batch_boolean(void *mem, ManifoldManifoldVec *ms,
                                             ManifoldOpType op);
    """
    ...
  def manifold_batch_hull(mem: ffi.CData, ms: ffi.CData) -> ffi.CData:
    """ManifoldManifold *manifold_batch_hull(void *mem, ManifoldManifoldVec *ms);"""
    ...
  def manifold_boolean(mem: ffi.CData, a: ffi.CData, b: ffi.CData, op: ffi.CData) -> ffi.CData:
    """
    ManifoldManifold *manifold_boolean(void *mem, ManifoldManifold *a,
                                       ManifoldManifold *b, ManifoldOpType op);
    """
    ...
  def manifold_bounding_box(mem: ffi.CData, m: ffi.CData) -> ffi.CData:
    """ManifoldBox *manifold_bounding_box(void *mem, ManifoldManifold *m);"""
    ...
  def manifold_box(mem: ffi.CData, x1: float, y1: float, z1: float, x2: float, y2: float, z2: float) -> ffi.CData:
    """
    ManifoldBox *manifold_box(void *mem, float x1, float y1, float z1, float x2,
                              float y2, float z2);
    """
    ...
  def manifold_box_center(b: ffi.CData) -> ffi.CData:
    """ManifoldVec3 manifold_box_center(ManifoldBox *b);"""
    ...
  def manifold_box_contains_box(a: ffi.CData, b: ffi.CData) -> int:
    """int manifold_box_contains_box(ManifoldBox *a, ManifoldBox *b);"""
    ...
  def manifold_box_contains_pt(b: ffi.CData, x: float, y: float, z: float) -> int:
    """int manifold_box_contains_pt(ManifoldBox *b, float x, float y, float z);"""
    ...
  def manifold_box_dimensions(b: ffi.CData) -> ffi.CData:
    """ManifoldVec3 manifold_box_dimensions(ManifoldBox *b);"""
    ...
  def manifold_box_does_overlap_box(a: ffi.CData, b: ffi.CData) -> int:
    """int manifold_box_does_overlap_box(ManifoldBox *a, ManifoldBox *b);"""
    ...
  def manifold_box_does_overlap_pt(b: ffi.CData, x: float, y: float, z: float) -> int:
    """int manifold_box_does_overlap_pt(ManifoldBox *b, float x, float y, float z);"""
    ...
  def manifold_box_include_pt(b: ffi.CData, x: float, y: float, z: float) -> None:
    """void manifold_box_include_pt(ManifoldBox *b, float x, float y, float z);"""
    ...
  def manifold_box_is_finite(b: ffi.CData) -> int:
    """int manifold_box_is_finite(ManifoldBox *b);"""
    ...
  def manifold_box_max(b: ffi.CData) -> ffi.CData:
    """ManifoldVec3 manifold_box_max(ManifoldBox *b);"""
    ...
  def manifold_box_min(b: ffi.CData) -> ffi.CData:
    """ManifoldVec3 manifold_box_min(ManifoldBox *b);"""
    ...
  def manifold_box_mul(mem: ffi.CData, b: ffi.CData, x: float, y: float, z: float) -> ffi.CData:
    """
    ManifoldBox *manifold_box_mul(void *mem, ManifoldBox *b, float x, float y,
                                  float z);
    """
    ...
  def manifold_box_scale(b: ffi.CData) -> float:
    """float manifold_box_scale(ManifoldBox *b);"""
    ...
  def manifold_box_size() -> int:
    """size_t manifold_box_size();"""
    ...
  def manifold_box_transform(mem: ffi.CData, b: ffi.CData, x1: float, y1: float, z1: float, x2: float, y2: float, z2: float, x3: float, y3: float, z3: float, x4: float, y4: float, z4: float) -> ffi.CData:
    """
    ManifoldBox *manifold_box_transform(void *mem, ManifoldBox *b, float x1,
                                        float y1, float z1, float x2, float y2,
                                        float z2, float x3, float y3, float z3,
                                        float x4, float y4, float z4);
    """
    ...
  def manifold_box_translate(mem: ffi.CData, b: ffi.CData, x: float, y: float, z: float) -> ffi.CData:
    """
    ManifoldBox *manifold_box_translate(void *mem, ManifoldBox *b, float x, float y,
                                        float z);
    """
    ...
  def manifold_box_union(mem: ffi.CData, a: ffi.CData, b: ffi.CData) -> ffi.CData:
    """ManifoldBox *manifold_box_union(void *mem, ManifoldBox *a, ManifoldBox *b);"""
    ...
  def manifold_calculate_curvature(mem: ffi.CData, m: ffi.CData, gaussian_idx: int, mean_idx: int) -> ffi.CData:
    """
    ManifoldManifold *manifold_calculate_curvature(void *mem, ManifoldManifold *m,
                                                   int gaussian_idx, int mean_idx);
    """
    ...
  def manifold_compose(mem: ffi.CData, ms: ffi.CData) -> ffi.CData:
    """ManifoldManifold *manifold_compose(void *mem, ManifoldManifoldVec *ms);"""
    ...
  def manifold_copy(mem: ffi.CData, m: ffi.CData) -> ffi.CData:
    """ManifoldManifold *manifold_copy(void *mem, ManifoldManifold *m);"""
    ...
  def manifold_cross_section_area(cs: ffi.CData) -> float:
    """double manifold_cross_section_area(ManifoldCrossSection *cs);"""
    ...
  def manifold_cross_section_batch_boolean(mem: ffi.CData, csv: ffi.CData, op: ffi.CData) -> ffi.CData:
    """
    ManifoldCrossSection *manifold_cross_section_batch_boolean(
        void *mem, ManifoldCrossSectionVec *csv, ManifoldOpType op);
    """
    ...
  def manifold_cross_section_batch_hull(mem: ffi.CData, css: ffi.CData) -> ffi.CData:
    """
    ManifoldCrossSection *manifold_cross_section_batch_hull(
        void *mem, ManifoldCrossSectionVec *css);
    """
    ...
  def manifold_cross_section_boolean(mem: ffi.CData, a: ffi.CData, b: ffi.CData, op: ffi.CData) -> ffi.CData:
    """
    ManifoldCrossSection *manifold_cross_section_boolean(void *mem,
                                                         ManifoldCrossSection *a,
                                                         ManifoldCrossSection *b,
                                                         ManifoldOpType op);
    """
    ...
  def manifold_cross_section_bounds(mem: ffi.CData, cs: ffi.CData) -> ffi.CData:
    """
    ManifoldRect *manifold_cross_section_bounds(void *mem,
                                                ManifoldCrossSection *cs);
    """
    ...
  def manifold_cross_section_circle(mem: ffi.CData, radius: float, circular_segments: int) -> ffi.CData:
    """
    ManifoldCrossSection *manifold_cross_section_circle(void *mem, float radius,
                                                        int circular_segments);
    """
    ...
  def manifold_cross_section_compose(mem: ffi.CData, csv: ffi.CData) -> ffi.CData:
    """
    ManifoldCrossSection *manifold_cross_section_compose(
        void *mem, ManifoldCrossSectionVec *csv);
    """
    ...
  def manifold_cross_section_copy(mem: ffi.CData, cs: ffi.CData) -> ffi.CData:
    """
    ManifoldCrossSection *manifold_cross_section_copy(void *mem,
                                                      ManifoldCrossSection *cs);
    """
    ...
  def manifold_cross_section_decompose(mem: ffi.CData, cs: ffi.CData) -> ffi.CData:
    """
    ManifoldCrossSectionVec *manifold_cross_section_decompose(
        void *mem, ManifoldCrossSection *cs);
    """
    ...
  def manifold_cross_section_difference(mem: ffi.CData, a: ffi.CData, b: ffi.CData) -> ffi.CData:
    """
    ManifoldCrossSection *manifold_cross_section_difference(
        void *mem, ManifoldCrossSection *a, ManifoldCrossSection *b);
    """
    ...
  def manifold_cross_section_empty(mem: ffi.CData) -> ffi.CData:
    """ManifoldCrossSection *manifold_cross_section_empty(void *mem);"""
    ...
  def manifold_cross_section_empty_vec(mem: ffi.CData) -> ffi.CData:
    """ManifoldCrossSectionVec *manifold_cross_section_empty_vec(void *mem);"""
    ...
  def manifold_cross_section_hull(mem: ffi.CData, cs: ffi.CData) -> ffi.CData:
    """
    ManifoldCrossSection *manifold_cross_section_hull(void *mem,
                                                      ManifoldCrossSection *cs);
    """
    ...
  def manifold_cross_section_hull_polygons(mem: ffi.CData, ps: ffi.CData) -> ffi.CData:
    """
    ManifoldCrossSection *manifold_cross_section_hull_polygons(
        void *mem, ManifoldPolygons *ps);
    """
    ...
  def manifold_cross_section_hull_simple_polygon(mem: ffi.CData, ps: ffi.CData) -> ffi.CData:
    """
    ManifoldCrossSection *manifold_cross_section_hull_simple_polygon(
        void *mem, ManifoldSimplePolygon *ps);
    """
    ...
  def manifold_cross_section_intersection(mem: ffi.CData, a: ffi.CData, b: ffi.CData) -> ffi.CData:
    """
    ManifoldCrossSection *manifold_cross_section_intersection(
        void *mem, ManifoldCrossSection *a, ManifoldCrossSection *b);
    """
    ...
  def manifold_cross_section_is_empty(cs: ffi.CData) -> int:
    """int manifold_cross_section_is_empty(ManifoldCrossSection *cs);"""
    ...
  def manifold_cross_section_mirror(mem: ffi.CData, cs: ffi.CData, ax_x: float, ax_y: float) -> ffi.CData:
    """
    ManifoldCrossSection *manifold_cross_section_mirror(void *mem,
                                                        ManifoldCrossSection *cs,
                                                        float ax_x, float ax_y);
    """
    ...
  def manifold_cross_section_num_contour(cs: ffi.CData) -> int:
    """int manifold_cross_section_num_contour(ManifoldCrossSection *cs);"""
    ...
  def manifold_cross_section_num_vert(cs: ffi.CData) -> int:
    """int manifold_cross_section_num_vert(ManifoldCrossSection *cs);"""
    ...
  def manifold_cross_section_of_polygons(mem: ffi.CData, p: ffi.CData, fr: ffi.CData) -> ffi.CData:
    """
    ManifoldCrossSection *manifold_cross_section_of_polygons(void *mem,
                                                             ManifoldPolygons *p,
                                                             ManifoldFillRule fr);
    """
    ...
  def manifold_cross_section_of_simple_polygon(mem: ffi.CData, p: ffi.CData, fr: ffi.CData) -> ffi.CData:
    """
    ManifoldCrossSection *manifold_cross_section_of_simple_polygon(
        void *mem, ManifoldSimplePolygon *p, ManifoldFillRule fr);
    """
    ...
  def manifold_cross_section_offset(mem: ffi.CData, cs: ffi.CData, delta: float, jt: ffi.CData, miter_limit: float, circular_segments: int) -> ffi.CData:
    """
    ManifoldCrossSection *manifold_cross_section_offset(
        void *mem, ManifoldCrossSection *cs, double delta, ManifoldJoinType jt,
        double miter_limit, int circular_segments);
    """
    ...
  def manifold_cross_section_rotate(mem: ffi.CData, cs: ffi.CData, deg: float) -> ffi.CData:
    """
    ManifoldCrossSection *manifold_cross_section_rotate(void *mem,
                                                        ManifoldCrossSection *cs,
                                                        float deg);
    """
    ...
  def manifold_cross_section_scale(mem: ffi.CData, cs: ffi.CData, x: float, y: float) -> ffi.CData:
    """
    ManifoldCrossSection *manifold_cross_section_scale(void *mem,
                                                       ManifoldCrossSection *cs,
                                                       float x, float y);
    """
    ...
  def manifold_cross_section_simplify(mem: ffi.CData, cs: ffi.CData, epsilon: float) -> ffi.CData:
    """
    ManifoldCrossSection *manifold_cross_section_simplify(void *mem,
                                                          ManifoldCrossSection *cs,
                                                          double epsilon);
    """
    ...
  def manifold_cross_section_size() -> int:
    """size_t manifold_cross_section_size();"""
    ...
  def manifold_cross_section_square(mem: ffi.CData, x: float, y: float, center: int) -> ffi.CData:
    """
    ManifoldCrossSection *manifold_cross_section_square(void *mem, float x, float y,
                                                        int center);
    """
    ...
  def manifold_cross_section_to_polygons(mem: ffi.CData, cs: ffi.CData) -> ffi.CData:
    """
    ManifoldPolygons *manifold_cross_section_to_polygons(void *mem,
                                                         ManifoldCrossSection *cs);
    """
    ...
  def manifold_cross_section_transform(mem: ffi.CData, cs: ffi.CData, x1: float, y1: float, x2: float, y2: float, x3: float, y3: float) -> ffi.CData:
    """
    ManifoldCrossSection *manifold_cross_section_transform(void *mem,
                                                           ManifoldCrossSection *cs,
                                                           float x1, float y1,
                                                           float x2, float y2,
                                                           float x3, float y3);
    """
    ...
  def manifold_cross_section_translate(mem: ffi.CData, cs: ffi.CData, x: float, y: float) -> ffi.CData:
    """
    ManifoldCrossSection *manifold_cross_section_translate(void *mem,
                                                           ManifoldCrossSection *cs,
                                                           float x, float y);
    """
    ...
  def manifold_cross_section_union(mem: ffi.CData, a: ffi.CData, b: ffi.CData) -> ffi.CData:
    """
    ManifoldCrossSection *manifold_cross_section_union(void *mem,
                                                       ManifoldCrossSection *a,
                                                       ManifoldCrossSection *b);
    """
    ...
  def manifold_cross_section_vec(mem: ffi.CData, sz: int) -> ffi.CData:
    """ManifoldCrossSectionVec *manifold_cross_section_vec(void *mem, size_t sz);"""
    ...
  def manifold_cross_section_vec_get(mem: ffi.CData, csv: ffi.CData, idx: int) -> ffi.CData:
    """
    ManifoldCrossSection *manifold_cross_section_vec_get(
        void *mem, ManifoldCrossSectionVec *csv, int idx);
    """
    ...
  def manifold_cross_section_vec_length(csv: ffi.CData) -> int:
    """size_t manifold_cross_section_vec_length(ManifoldCrossSectionVec *csv);"""
    ...
  def manifold_cross_section_vec_push_back(csv: ffi.CData, cs: ffi.CData) -> None:
    """
    void manifold_cross_section_vec_push_back(ManifoldCrossSectionVec *csv,
                                              ManifoldCrossSection *cs);
    """
    ...
  def manifold_cross_section_vec_reserve(csv: ffi.CData, sz: int) -> None:
    """
    void manifold_cross_section_vec_reserve(ManifoldCrossSectionVec *csv,
                                            size_t sz);
    """
    ...
  def manifold_cross_section_vec_set(csv: ffi.CData, idx: int, cs: ffi.CData) -> None:
    """
    void manifold_cross_section_vec_set(ManifoldCrossSectionVec *csv, int idx,
                                        ManifoldCrossSection *cs);
    """
    ...
  def manifold_cross_section_vec_size() -> int:
    """size_t manifold_cross_section_vec_size();"""
    ...
  def manifold_cross_section_warp(mem: ffi.CData, cs: ffi.CData, fun: ffi.CData) -> ffi.CData:
    """
    ManifoldCrossSection *manifold_cross_section_warp(
        void *mem, ManifoldCrossSection *cs, ManifoldVec2 (*fun)(float, float));
    """
    ...
  def manifold_cube(mem: ffi.CData, x: float, y: float, z: float, center: int) -> ffi.CData:
    """
    ManifoldManifold *manifold_cube(void *mem, float x, float y, float z,
                                    int center);
    """
    ...
  def manifold_cylinder(mem: ffi.CData, height: float, radius_low: float, radius_high: float, circular_segments: int, center: int) -> ffi.CData:
    """
    ManifoldManifold *manifold_cylinder(void *mem, float height, float radius_low,
                                        float radius_high, int circular_segments,
                                        int center);
    """
    ...
  def manifold_decompose(mem: ffi.CData, m: ffi.CData) -> ffi.CData:
    """ManifoldManifoldVec *manifold_decompose(void *mem, ManifoldManifold *m);"""
    ...
  def manifold_delete_box(b: ffi.CData) -> None:
    """void manifold_delete_box(ManifoldBox *b);"""
    ...
  def manifold_delete_cross_section(cs: ffi.CData) -> None:
    """void manifold_delete_cross_section(ManifoldCrossSection *cs);"""
    ...
  def manifold_delete_cross_section_vec(csv: ffi.CData) -> None:
    """void manifold_delete_cross_section_vec(ManifoldCrossSectionVec *csv);"""
    ...
  def manifold_delete_manifold(m: ffi.CData) -> None:
    """void manifold_delete_manifold(ManifoldManifold *m);"""
    ...
  def manifold_delete_manifold_vec(ms: ffi.CData) -> None:
    """void manifold_delete_manifold_vec(ManifoldManifoldVec *ms);"""
    ...
  def manifold_delete_meshgl(m: ffi.CData) -> None:
    """void manifold_delete_meshgl(ManifoldMeshGL *m);"""
    ...
  def manifold_delete_polygons(p: ffi.CData) -> None:
    """void manifold_delete_polygons(ManifoldPolygons *p);"""
    ...
  def manifold_delete_rect(b: ffi.CData) -> None:
    """void manifold_delete_rect(ManifoldRect *b);"""
    ...
  def manifold_delete_simple_polygon(p: ffi.CData) -> None:
    """void manifold_delete_simple_polygon(ManifoldSimplePolygon *p);"""
    ...
  def manifold_destruct_box(b: ffi.CData) -> None:
    """void manifold_destruct_box(ManifoldBox *b);"""
    ...
  def manifold_destruct_cross_section(m: ffi.CData) -> None:
    """void manifold_destruct_cross_section(ManifoldCrossSection *m);"""
    ...
  def manifold_destruct_cross_section_vec(csv: ffi.CData) -> None:
    """void manifold_destruct_cross_section_vec(ManifoldCrossSectionVec *csv);"""
    ...
  def manifold_destruct_manifold(m: ffi.CData) -> None:
    """void manifold_destruct_manifold(ManifoldManifold *m);"""
    ...
  def manifold_destruct_manifold_vec(ms: ffi.CData) -> None:
    """void manifold_destruct_manifold_vec(ManifoldManifoldVec *ms);"""
    ...
  def manifold_destruct_meshgl(m: ffi.CData) -> None:
    """void manifold_destruct_meshgl(ManifoldMeshGL *m);"""
    ...
  def manifold_destruct_polygons(p: ffi.CData) -> None:
    """void manifold_destruct_polygons(ManifoldPolygons *p);"""
    ...
  def manifold_destruct_rect(b: ffi.CData) -> None:
    """void manifold_destruct_rect(ManifoldRect *b);"""
    ...
  def manifold_destruct_simple_polygon(p: ffi.CData) -> None:
    """void manifold_destruct_simple_polygon(ManifoldSimplePolygon *p);"""
    ...
  def manifold_difference(mem: ffi.CData, a: ffi.CData, b: ffi.CData) -> ffi.CData:
    """
    ManifoldManifold *manifold_difference(void *mem, ManifoldManifold *a,
                                          ManifoldManifold *b);
    """
    ...
  def manifold_empty(mem: ffi.CData) -> ffi.CData:
    """ManifoldManifold *manifold_empty(void *mem);"""
    ...
  def manifold_extrude(mem: ffi.CData, cs: ffi.CData, height: float, slices: int, twist_degrees: float, scale_x: float, scale_y: float) -> ffi.CData:
    """
    ManifoldManifold *manifold_extrude(void *mem, ManifoldCrossSection *cs,
                                       float height, int slices,
                                       float twist_degrees, float scale_x,
                                       float scale_y);
    """
    ...
  def manifold_genus(m: ffi.CData) -> int:
    """int manifold_genus(ManifoldManifold *m);"""
    ...
  def manifold_get_circular_segments(radius: float) -> int:
    """int manifold_get_circular_segments(float radius);"""
    ...
  def manifold_get_meshgl(mem: ffi.CData, m: ffi.CData) -> ffi.CData:
    """ManifoldMeshGL *manifold_get_meshgl(void *mem, ManifoldManifold *m);"""
    ...
  def manifold_get_properties(m: ffi.CData) -> ffi.CData:
    """ManifoldProperties manifold_get_properties(ManifoldManifold *m);"""
    ...
  def manifold_hull(mem: ffi.CData, m: ffi.CData) -> ffi.CData:
    """ManifoldManifold *manifold_hull(void *mem, ManifoldManifold *m);"""
    ...
  def manifold_hull_pts(mem: ffi.CData, ps: ffi.CData, length: int) -> ffi.CData:
    """ManifoldManifold *manifold_hull_pts(void *mem, ManifoldVec3 *ps, size_t length);"""
    ...
  def manifold_intersection(mem: ffi.CData, a: ffi.CData, b: ffi.CData) -> ffi.CData:
    """
    ManifoldManifold *manifold_intersection(void *mem, ManifoldManifold *a,
                                            ManifoldManifold *b);
    """
    ...
  def manifold_is_empty(m: ffi.CData) -> int:
    """int manifold_is_empty(ManifoldManifold *m);"""
    ...
  def manifold_level_set(mem: ffi.CData, sdf: ffi.CData, bounds: ffi.CData, edge_length: float, level: float) -> ffi.CData:
    """
    SDF
    By default, the execution policy (sequential or parallel) of
    manifold_level_set will be chosen automatically depending on the size of the
    job and whether Manifold has been compiled with a PAR backend. If you are
    using these bindings from a language that has a runtime lock preventing the
    parallel execution of closures, then you should use manifold_level_set_seq to
    force sequential execution.

    ManifoldMeshGL *manifold_level_set(void *mem, float (*sdf)(float, float, float),
                                       ManifoldBox *bounds, float edge_length,
                                       float level);
    """
    ...
  def manifold_level_set_context(mem: ffi.CData, sdf: ffi.CData, bounds: ffi.CData, edge_length: float, level: float, ctx: ffi.CData) -> ffi.CData:
    """
    The _context variants of manifold_level_set allow a pointer to be passed
    back to each invocation of the sdf function pointer, for languages that
    need additional data.

    ManifoldMeshGL *manifold_level_set_context(
        void *mem, float (*sdf)(float, float, float, void *), ManifoldBox *bounds,
        float edge_length, float level, void *ctx);
    """
    ...
  def manifold_level_set_seq(mem: ffi.CData, sdf: ffi.CData, bounds: ffi.CData, edge_length: float, level: float) -> ffi.CData:
    """
    ManifoldMeshGL *manifold_level_set_seq(void *mem,
                                           float (*sdf)(float, float, float),
                                           ManifoldBox *bounds, float edge_length,
                                           float level);
    """
    ...
  def manifold_level_set_seq_context(mem: ffi.CData, sdf: ffi.CData, bounds: ffi.CData, edge_length: float, level: float, ctx: ffi.CData) -> ffi.CData:
    """
    ManifoldMeshGL *manifold_level_set_seq_context(
        void *mem, float (*sdf)(float, float, float, void *), ManifoldBox *bounds,
        float edge_length, float level, void *ctx);
    """
    ...
  def manifold_manifold_empty_vec(mem: ffi.CData) -> ffi.CData:
    """ManifoldManifoldVec *manifold_manifold_empty_vec(void *mem);"""
    ...
  def manifold_manifold_pair_size() -> int:
    """size_t manifold_manifold_pair_size();"""
    ...
  def manifold_manifold_size() -> int:
    """size_t manifold_manifold_size();"""
    ...
  def manifold_manifold_vec(mem: ffi.CData, sz: int) -> ffi.CData:
    """ManifoldManifoldVec *manifold_manifold_vec(void *mem, size_t sz);"""
    ...
  def manifold_manifold_vec_get(mem: ffi.CData, ms: ffi.CData, idx: int) -> ffi.CData:
    """
    ManifoldManifold *manifold_manifold_vec_get(void *mem, ManifoldManifoldVec *ms,
                                                int idx);
    """
    ...
  def manifold_manifold_vec_length(ms: ffi.CData) -> int:
    """size_t manifold_manifold_vec_length(ManifoldManifoldVec *ms);"""
    ...
  def manifold_manifold_vec_push_back(ms: ffi.CData, m: ffi.CData) -> None:
    """
    void manifold_manifold_vec_push_back(ManifoldManifoldVec *ms,
                                         ManifoldManifold *m);
    """
    ...
  def manifold_manifold_vec_reserve(ms: ffi.CData, sz: int) -> None:
    """void manifold_manifold_vec_reserve(ManifoldManifoldVec *ms, size_t sz);"""
    ...
  def manifold_manifold_vec_set(ms: ffi.CData, idx: int, m: ffi.CData) -> None:
    """
    void manifold_manifold_vec_set(ManifoldManifoldVec *ms, int idx,
                                   ManifoldManifold *m);
    """
    ...
  def manifold_manifold_vec_size() -> int:
    """size_t manifold_manifold_vec_size();"""
    ...
  def manifold_meshgl(mem: ffi.CData, vert_props: ffi.CData, n_verts: int, n_props: int, tri_verts: ffi.CData, n_tris: int) -> ffi.CData:
    """
    ManifoldMeshGL *manifold_meshgl(void *mem, float *vert_props, size_t n_verts,
                                    size_t n_props, uint32_t *tri_verts,
                                    size_t n_tris);
    """
    ...
  def manifold_meshgl_copy(mem: ffi.CData, m: ffi.CData) -> ffi.CData:
    """ManifoldMeshGL *manifold_meshgl_copy(void *mem, ManifoldMeshGL *m);"""
    ...
  def manifold_meshgl_face_id(mem: ffi.CData, m: ffi.CData) -> ffi.CData:
    """uint32_t *manifold_meshgl_face_id(void *mem, ManifoldMeshGL *m);"""
    ...
  def manifold_meshgl_face_id_length(m: ffi.CData) -> int:
    """size_t manifold_meshgl_face_id_length(ManifoldMeshGL *m);"""
    ...
  def manifold_meshgl_halfedge_tangent(mem: ffi.CData, m: ffi.CData) -> ffi.CData:
    """float *manifold_meshgl_halfedge_tangent(void *mem, ManifoldMeshGL *m);"""
    ...
  def manifold_meshgl_merge_from_vert(mem: ffi.CData, m: ffi.CData) -> ffi.CData:
    """uint32_t *manifold_meshgl_merge_from_vert(void *mem, ManifoldMeshGL *m);"""
    ...
  def manifold_meshgl_merge_length(m: ffi.CData) -> int:
    """size_t manifold_meshgl_merge_length(ManifoldMeshGL *m);"""
    ...
  def manifold_meshgl_merge_to_vert(mem: ffi.CData, m: ffi.CData) -> ffi.CData:
    """uint32_t *manifold_meshgl_merge_to_vert(void *mem, ManifoldMeshGL *m);"""
    ...
  def manifold_meshgl_num_prop(m: ffi.CData) -> int:
    """int manifold_meshgl_num_prop(ManifoldMeshGL *m);"""
    ...
  def manifold_meshgl_num_tri(m: ffi.CData) -> int:
    """int manifold_meshgl_num_tri(ManifoldMeshGL *m);"""
    ...
  def manifold_meshgl_num_vert(m: ffi.CData) -> int:
    """int manifold_meshgl_num_vert(ManifoldMeshGL *m);"""
    ...
  def manifold_meshgl_run_index(mem: ffi.CData, m: ffi.CData) -> ffi.CData:
    """uint32_t *manifold_meshgl_run_index(void *mem, ManifoldMeshGL *m);"""
    ...
  def manifold_meshgl_run_index_length(m: ffi.CData) -> int:
    """size_t manifold_meshgl_run_index_length(ManifoldMeshGL *m);"""
    ...
  def manifold_meshgl_run_original_id(mem: ffi.CData, m: ffi.CData) -> ffi.CData:
    """uint32_t *manifold_meshgl_run_original_id(void *mem, ManifoldMeshGL *m);"""
    ...
  def manifold_meshgl_run_original_id_length(m: ffi.CData) -> int:
    """size_t manifold_meshgl_run_original_id_length(ManifoldMeshGL *m);"""
    ...
  def manifold_meshgl_run_transform(mem: ffi.CData, m: ffi.CData) -> ffi.CData:
    """float *manifold_meshgl_run_transform(void *mem, ManifoldMeshGL *m);"""
    ...
  def manifold_meshgl_run_transform_length(m: ffi.CData) -> int:
    """size_t manifold_meshgl_run_transform_length(ManifoldMeshGL *m);"""
    ...
  def manifold_meshgl_size() -> int:
    """size_t manifold_meshgl_size();"""
    ...
  def manifold_meshgl_tangent_length(m: ffi.CData) -> int:
    """size_t manifold_meshgl_tangent_length(ManifoldMeshGL *m);"""
    ...
  def manifold_meshgl_tri_length(m: ffi.CData) -> int:
    """size_t manifold_meshgl_tri_length(ManifoldMeshGL *m);"""
    ...
  def manifold_meshgl_tri_verts(mem: ffi.CData, m: ffi.CData) -> ffi.CData:
    """uint32_t *manifold_meshgl_tri_verts(void *mem, ManifoldMeshGL *m);"""
    ...
  def manifold_meshgl_vert_properties(mem: ffi.CData, m: ffi.CData) -> ffi.CData:
    """float *manifold_meshgl_vert_properties(void *mem, ManifoldMeshGL *m);"""
    ...
  def manifold_meshgl_vert_properties_length(m: ffi.CData) -> int:
    """size_t manifold_meshgl_vert_properties_length(ManifoldMeshGL *m);"""
    ...
  def manifold_meshgl_w_tangents(mem: ffi.CData, vert_props: ffi.CData, n_verts: int, n_props: int, tri_verts: ffi.CData, n_tris: int, halfedge_tangent: ffi.CData) -> ffi.CData:
    """
    ManifoldMeshGL *manifold_meshgl_w_tangents(void *mem, float *vert_props,
                                               size_t n_verts, size_t n_props,
                                               uint32_t *tri_verts, size_t n_tris,
                                               float *halfedge_tangent);
    """
    ...
  def manifold_mirror(mem: ffi.CData, m: ffi.CData, nx: float, ny: float, nz: float) -> ffi.CData:
    """
    ManifoldManifold *manifold_mirror(void *mem, ManifoldManifold *m, float nx,
                                      float ny, float nz);
    """
    ...
  def manifold_num_edge(m: ffi.CData) -> int:
    """int manifold_num_edge(ManifoldManifold *m);"""
    ...
  def manifold_num_tri(m: ffi.CData) -> int:
    """int manifold_num_tri(ManifoldManifold *m);"""
    ...
  def manifold_num_vert(m: ffi.CData) -> int:
    """int manifold_num_vert(ManifoldManifold *m);"""
    ...
  def manifold_of_meshgl(mem: ffi.CData, mesh: ffi.CData) -> ffi.CData:
    """ManifoldManifold *manifold_of_meshgl(void *mem, ManifoldMeshGL *mesh);"""
    ...
  def manifold_original_id(m: ffi.CData) -> int:
    """int manifold_original_id(ManifoldManifold *m);"""
    ...
  def manifold_polygons(mem: ffi.CData, ps: ffi.CData, length: int) -> ffi.CData:
    """
    ManifoldPolygons *manifold_polygons(void *mem, ManifoldSimplePolygon **ps,
                                        size_t length);
    """
    ...
  def manifold_polygons_get_point(ps: ffi.CData, simple_idx: int, pt_idx: int) -> ffi.CData:
    """
    ManifoldVec2 manifold_polygons_get_point(ManifoldPolygons *ps, int simple_idx,
                                             int pt_idx);
    """
    ...
  def manifold_polygons_get_simple(mem: ffi.CData, ps: ffi.CData, idx: int) -> ffi.CData:
    """
    ManifoldSimplePolygon *manifold_polygons_get_simple(void *mem,
                                                        ManifoldPolygons *ps,
                                                        int idx);
    """
    ...
  def manifold_polygons_length(ps: ffi.CData) -> int:
    """size_t manifold_polygons_length(ManifoldPolygons *ps);"""
    ...
  def manifold_polygons_simple_length(ps: ffi.CData, idx: int) -> int:
    """size_t manifold_polygons_simple_length(ManifoldPolygons *ps, int idx);"""
    ...
  def manifold_polygons_size() -> int:
    """size_t manifold_polygons_size();"""
    ...
  def manifold_precision(m: ffi.CData) -> float:
    """float manifold_precision(ManifoldManifold *m);"""
    ...
  def manifold_project(mem: ffi.CData, m: ffi.CData) -> ffi.CData:
    """ManifoldCrossSection *manifold_project(void *mem, ManifoldManifold *m);"""
    ...
  def manifold_rect(mem: ffi.CData, x1: float, y1: float, x2: float, y2: float) -> ffi.CData:
    """ManifoldRect *manifold_rect(void *mem, float x1, float y1, float x2, float y2);"""
    ...
  def manifold_rect_center(r: ffi.CData) -> ffi.CData:
    """ManifoldVec2 manifold_rect_center(ManifoldRect *r);"""
    ...
  def manifold_rect_contains_pt(r: ffi.CData, x: float, y: float) -> int:
    """int manifold_rect_contains_pt(ManifoldRect *r, float x, float y);"""
    ...
  def manifold_rect_contains_rect(a: ffi.CData, b: ffi.CData) -> int:
    """int manifold_rect_contains_rect(ManifoldRect *a, ManifoldRect *b);"""
    ...
  def manifold_rect_dimensions(r: ffi.CData) -> ffi.CData:
    """ManifoldVec2 manifold_rect_dimensions(ManifoldRect *r);"""
    ...
  def manifold_rect_does_overlap_rect(a: ffi.CData, r: ffi.CData) -> int:
    """int manifold_rect_does_overlap_rect(ManifoldRect *a, ManifoldRect *r);"""
    ...
  def manifold_rect_include_pt(r: ffi.CData, x: float, y: float) -> None:
    """void manifold_rect_include_pt(ManifoldRect *r, float x, float y);"""
    ...
  def manifold_rect_is_empty(r: ffi.CData) -> int:
    """int manifold_rect_is_empty(ManifoldRect *r);"""
    ...
  def manifold_rect_is_finite(r: ffi.CData) -> int:
    """int manifold_rect_is_finite(ManifoldRect *r);"""
    ...
  def manifold_rect_max(r: ffi.CData) -> ffi.CData:
    """ManifoldVec2 manifold_rect_max(ManifoldRect *r);"""
    ...
  def manifold_rect_min(r: ffi.CData) -> ffi.CData:
    """ManifoldVec2 manifold_rect_min(ManifoldRect *r);"""
    ...
  def manifold_rect_mul(mem: ffi.CData, r: ffi.CData, x: float, y: float) -> ffi.CData:
    """ManifoldRect *manifold_rect_mul(void *mem, ManifoldRect *r, float x, float y);"""
    ...
  def manifold_rect_scale(r: ffi.CData) -> float:
    """float manifold_rect_scale(ManifoldRect *r);"""
    ...
  def manifold_rect_size() -> int:
    """size_t manifold_rect_size();"""
    ...
  def manifold_rect_transform(mem: ffi.CData, r: ffi.CData, x1: float, y1: float, x2: float, y2: float, x3: float, y3: float) -> ffi.CData:
    """
    ManifoldRect *manifold_rect_transform(void *mem, ManifoldRect *r, float x1,
                                          float y1, float x2, float y2, float x3,
                                          float y3);
    """
    ...
  def manifold_rect_translate(mem: ffi.CData, r: ffi.CData, x: float, y: float) -> ffi.CData:
    """
    ManifoldRect *manifold_rect_translate(void *mem, ManifoldRect *r, float x,
                                          float y);
    """
    ...
  def manifold_rect_union(mem: ffi.CData, a: ffi.CData, b: ffi.CData) -> ffi.CData:
    """ManifoldRect *manifold_rect_union(void *mem, ManifoldRect *a, ManifoldRect *b);"""
    ...
  def manifold_refine(mem: ffi.CData, m: ffi.CData, refine: int) -> ffi.CData:
    """ManifoldManifold *manifold_refine(void *mem, ManifoldManifold *m, int refine);"""
    ...
  def manifold_reserve_ids(n: int) -> int:
    """uint32_t manifold_reserve_ids(uint32_t n);"""
    ...
  def manifold_revolve(mem: ffi.CData, cs: ffi.CData, circular_segments: int) -> ffi.CData:
    """
    ManifoldManifold *manifold_revolve(void *mem, ManifoldCrossSection *cs,
                                       int circular_segments);
    """
    ...
  def manifold_rotate(mem: ffi.CData, m: ffi.CData, x: float, y: float, z: float) -> ffi.CData:
    """
    ManifoldManifold *manifold_rotate(void *mem, ManifoldManifold *m, float x,
                                      float y, float z);
    """
    ...
  def manifold_scale(mem: ffi.CData, m: ffi.CData, x: float, y: float, z: float) -> ffi.CData:
    """
    ManifoldManifold *manifold_scale(void *mem, ManifoldManifold *m, float x,
                                     float y, float z);
    """
    ...
  def manifold_set_circular_segments(number: int) -> None:
    """void manifold_set_circular_segments(int number);"""
    ...
  def manifold_set_min_circular_angle(degrees: float) -> None:
    """void manifold_set_min_circular_angle(float degrees);"""
    ...
  def manifold_set_min_circular_edge_length(length: float) -> None:
    """void manifold_set_min_circular_edge_length(float length);"""
    ...
  def manifold_set_properties(mem: ffi.CData, m: ffi.CData, num_prop: int, fun: ffi.CData) -> ffi.CData:
    """
    ManifoldManifold *manifold_set_properties(
        void *mem, ManifoldManifold *m, int num_prop,
        void (*fun)(float *new_prop, ManifoldVec3 position, const float *old_prop));
    """
    ...
  def manifold_simple_polygon(mem: ffi.CData, ps: ffi.CData, length: int) -> ffi.CData:
    """
    ManifoldSimplePolygon *manifold_simple_polygon(void *mem, ManifoldVec2 *ps,
                                                   size_t length);
    """
    ...
  def manifold_simple_polygon_get_point(p: ffi.CData, idx: int) -> ffi.CData:
    """
    ManifoldVec2 manifold_simple_polygon_get_point(ManifoldSimplePolygon *p,
                                                   int idx);
    """
    ...
  def manifold_simple_polygon_length(p: ffi.CData) -> int:
    """size_t manifold_simple_polygon_length(ManifoldSimplePolygon *p);"""
    ...
  def manifold_simple_polygon_size() -> int:
    """size_t manifold_simple_polygon_size();"""
    ...
  def manifold_slice(mem: ffi.CData, m: ffi.CData, height: float) -> ffi.CData:
    """
    ManifoldCrossSection *manifold_slice(void *mem, ManifoldManifold *m,
                                         float height);
    """
    ...
  def manifold_smooth(mem: ffi.CData, mesh: ffi.CData, half_edges: ffi.CData, smoothness: ffi.CData, n_idxs: int) -> ffi.CData:
    """
    ManifoldManifold *manifold_smooth(void *mem, ManifoldMeshGL *mesh,
                                      int *half_edges, float *smoothness,
                                      int n_idxs);
    """
    ...
  def manifold_sphere(mem: ffi.CData, radius: float, circular_segments: int) -> ffi.CData:
    """
    ManifoldManifold *manifold_sphere(void *mem, float radius,
                                      int circular_segments);
    """
    ...
  def manifold_split(mem_first: ffi.CData, mem_second: ffi.CData, a: ffi.CData, b: ffi.CData) -> ffi.CData:
    """
    ManifoldManifoldPair manifold_split(void *mem_first, void *mem_second,
                                        ManifoldManifold *a, ManifoldManifold *b);
    """
    ...
  def manifold_split_by_plane(mem_first: ffi.CData, mem_second: ffi.CData, m: ffi.CData, normal_x: float, normal_y: float, normal_z: float, offset: float) -> ffi.CData:
    """
    ManifoldManifoldPair manifold_split_by_plane(void *mem_first, void *mem_second,
                                                 ManifoldManifold *m,
                                                 float normal_x, float normal_y,
                                                 float normal_z, float offset);
    """
    ...
  def manifold_status(m: ffi.CData) -> ffi.CData:
    """ManifoldError manifold_status(ManifoldManifold *m);"""
    ...
  def manifold_tetrahedron(mem: ffi.CData) -> ffi.CData:
    """ManifoldManifold *manifold_tetrahedron(void *mem);"""
    ...
  def manifold_transform(mem: ffi.CData, m: ffi.CData, x1: float, y1: float, z1: float, x2: float, y2: float, z2: float, x3: float, y3: float, z3: float, x4: float, y4: float, z4: float) -> ffi.CData:
    """
    ManifoldManifold *manifold_transform(void *mem, ManifoldManifold *m, float x1,
                                         float y1, float z1, float x2, float y2,
                                         float z2, float x3, float y3, float z3,
                                         float x4, float y4, float z4);
    """
    ...
  def manifold_translate(mem: ffi.CData, m: ffi.CData, x: float, y: float, z: float) -> ffi.CData:
    """
    ManifoldManifold *manifold_translate(void *mem, ManifoldManifold *m, float x,
                                         float y, float z);
    """
    ...
  def manifold_trim_by_plane(mem: ffi.CData, m: ffi.CData, normal_x: float, normal_y: float, normal_z: float, offset: float) -> ffi.CData:
    """
    ManifoldManifold *manifold_trim_by_plane(void *mem, ManifoldManifold *m,
                                             float normal_x, float normal_y,
                                             float normal_z, float offset);
    """
    ...
  def manifold_union(mem: ffi.CData, a: ffi.CData, b: ffi.CData) -> ffi.CData:
    """
    ManifoldManifold *manifold_union(void *mem, ManifoldManifold *a,
                                     ManifoldManifold *b);
    """
    ...
  def manifold_warp(mem: ffi.CData, m: ffi.CData, fun: ffi.CData) -> ffi.CData:
    """
    ManifoldManifold *manifold_warp(void *mem, ManifoldManifold *m,
                                    ManifoldVec3 (*fun)(float, float, float));
    """
    ...