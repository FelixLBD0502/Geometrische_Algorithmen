import geopandas as gpd
import matplotlib.pyplot as plt
from shapely.geometry import Polygon, MultiPolygon, Point

# Erstelle ein Polygon
polygon1 = Polygon([(2, 5), (10, 5), (10, 2), (2, 2)])

# Erstelle ein zweites Polygon
polygon2 = Polygon([(3, 10), (7, 10), (7, 5), (3, 5)])

# Erstelle ein Multipolygon aus den beiden Polygonen
multi_polygon = MultiPolygon([polygon1, polygon2])

# Definiere den Abstand zwischen den Windkraftanlagen
d = 3

# Generiere eine Grid-Geometrie mit einem Gitterabstand von d und berechne die Anzahl von Punkten,
# die innerhalb des Multi-Polygons liegen
bbox = multi_polygon.bounds
min_x, min_y, max_x, max_y = bbox
rows = int((max_y - min_y) / d) + 1
cols = int((max_x - min_x) / d) + 1
points = []
for x in range(cols):
    for y in range(rows):
        point = Point(min_x + x * d, min_y + y * d)
        points.append(point)

# Erstelle ein GeoDataFrame aus den Punkten
gdf = gpd.GeoDataFrame({'geometry': points})

# Filtere die Punkte nach denen, die innerhalb des Multi-Polygons liegen
gdf = gdf[gdf.intersects(multi_polygon)]
num_points = len(gdf)

# Gebe die Koordinaten der Punkte aus
print("Die maximale Anzahl von Punkten innerhalb des Multi-Polygons mit einem Abstand von "
      + str(d) + " beträgt:", num_points)

# Koordinaten der Punkte als Liste ausgeben
point_coords = [list(point.coords)[0] for point in gdf['geometry']]
print("Koordinaten der Punkte:")
print(point_coords)

# Zeige das Multi-Polygon und die Punkte
fig, ax = plt.subplots()
gdf.plot(ax=ax, color='red', markersize=2)
df = gpd.GeoDataFrame(geometry=[multi_polygon])
df.plot(ax=ax, alpha=0.5)
ax.axis('on')
ax.set_aspect('equal')
ax.set_xlim(0, 11)
ax.set_ylim(0, 11)
plt.xticks(range(0, 12, 1))
plt.yticks(range(1, 12, 1))
ax.grid(linestyle='--', linewidth=0.5)

# Speichere das MultiPolygon als PDF
plt.savefig("multipolygon_d=" + str(d) + ".pdf", bbox_inches='tight')
