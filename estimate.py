from pathlib import Path

from src.agoro_field_boundary_detector import FieldBoundaryDetectorInterface

import json

model_path=Path.cwd() / "models/mask_rcnn"

# Load in the model, will start GEE session
model = FieldBoundaryDetectorInterface(model_path)

coord=[37.226007, -94.255782]

lng=coord[0]
lat=coord[1]

# Make the prediction
pred = model(lng, lat, thr=0.4)

geojson_data = {
    "type": "FeatureCollection",
    "features": [
        {
            "type": "Feature",
            "geometry": {
                "type": "Polygon",
                "coordinates": [[(lat, lng) for lng, lat in pred]]
            },
            "properties": {}
        }
    ]
}

with open('out.geojson', "w") as output_file:
    json.dump(geojson_data, output_file, indent=2)
