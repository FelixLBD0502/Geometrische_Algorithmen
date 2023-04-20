from shapely.geometry import Polygon, MultiPolygon
from windkraftpark import windpark_abstand_d

def test_windpark_abstand_d():
    polygon1 = Polygon([(2, 5), (10, 5), (10, 2), (2, 2)])
    polygon2 = Polygon([(3, 10), (7, 10), (7, 5), (3, 5)])
    multi_polygon = MultiPolygon([polygon1, polygon2])
    d = 2
    num_points, point_coords = windpark_abstand_d(multi_polygon, d)
    assert num_points == 17

test_windpark_abstand_d()