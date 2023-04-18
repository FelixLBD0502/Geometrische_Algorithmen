# Zur logischen Orientierung (File hat keine Funktion)
from shapely.geometry import Polygon, MultiPolygon, MultiPoint, Point

# Erstelle ein Polygon
polygon1 = Polygon([(2, 5), (10, 5), (10, 2), (2, 2)])

# Erstelle ein zweites Polygon
polygon2 = Polygon([(3, 10), (7, 10), (7, 5), (3, 5)])

# Erstelle ein Multipolygon aus den beiden Polygonen
multi_polygon = MultiPolygon([polygon1, polygon2])

# Definiere den Abstand zwischen den Windkraftanlagen
d = 1
# d(P1(x1|y1)|P2(x2|y2)) = math.sqrt((x1 - x2)^2+(y1 - y2)^2)
# 1. Bedingung: Innerhalb des Multi Polygons
# 2. Bedingung: Abstand zu allen anderen Punkten mindestens d
# Finde einen Algorithmus der die maximale Anzahl an Windkraftanlagen (in Form von geometrischen Punkten) mit einem Abstand von d definiert
# Anschließend sollen


print("Die maximale Anzahl von Windkraftanlagen mit einem Abstand von " + str(d) + " beträgt: " + str(num_points) + ".")

