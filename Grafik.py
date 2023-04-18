# Das leere Multipolygon als Grafik in einem Koordinatensystem
import geopandas as gpd
import matplotlib.pyplot as plt
from shapely.geometry import Polygon, MultiPolygon

# Erstelle ein Polygon
polygon1 = Polygon([(2, 5), (10, 5), (10, 2), (2, 2)])

# Erstelle ein zweites Polygon
polygon2 = Polygon([(3, 10), (7, 10), (7, 5), (3, 5)])

# Erstelle ein Multipolygon aus den beiden Polygonen
multi_polygon = MultiPolygon([polygon1, polygon2])

# Erstelle ein geopandas GeoDataFrame
df = gpd.GeoDataFrame(geometry=[multi_polygon])

# Zeige die Polygone
fig, ax = plt.subplots()
df.plot(ax=ax)
ax.axis('on')
ax.set_aspect('equal')
ax.set_xlim(0, 11)
ax.set_ylim(0, 11)
plt.xticks(range(0, 12, 1))
plt.yticks(range(1, 12, 1))
ax.grid(linestyle='--', linewidth=0.5)

# Speichere das MultiPolygon als PDF
plt.savefig("multipolygon1.pdf", bbox_inches='tight')