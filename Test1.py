
from shapely.geometry import Polygon, MultiPolygon

# Erstelle ein Polygon
polygon1 = Polygon([(2, 5), (10, 5), (10, 2), (2, 2)])

# Erstelle ein zweites Polygon
polygon2 = Polygon([(3, 10), (7, 10), (3, 6), (7, 6)])

# Erstelle ein Multipolygon aus den beiden Polygonen
multi_polygon = MultiPolygon([polygon1, polygon2])

# Definiere den Abstand zwischen den Windkraftanlagen
d = 2