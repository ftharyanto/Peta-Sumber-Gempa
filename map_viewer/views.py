import shapefile
import os
from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings

def map_view(request):
    return render(request, 'map_viewer/map.html')

def shp_to_geojson(shp_path, name_field):
    try:
        reader = shapefile.Reader(shp_path)
        fields = [f[0].lower() for f in reader.fields[1:]] # Skip DeletionFlag
        
        features = []
        for sr in reader.shapeRecords():
            geom = sr.shape.__geo_interface__
            
            # Map record values to field names
            props = {}
            for i, field_name in enumerate(fields):
                val = sr.record[i]
                # Convert bytes to string if necessary
                if isinstance(val, bytes):
                    val = val.decode('utf-8', errors='ignore')
                props[field_name] = val
            
            # Ensure 'name' is present for the template logic
            name_idx = fields.index(name_field.lower()) if name_field.lower() in fields else 0
            props['display_name'] = sr.record[name_idx]
            
            features.append({
                'type': 'Feature',
                'geometry': geom,
                'properties': props
            })
            
        return {
            'type': 'FeatureCollection',
            'features': features
        }
    except Exception as e:
        return {'error': str(e)}

def get_sesar_data(request):
    # Base path is the project root
    base_dir = settings.BASE_DIR
    shp_path = os.path.join(base_dir, 'Sesar', 'PusGeN2024_Shallow_Crustal_v5_12.shp')
    data = shp_to_geojson(shp_path, 'Name')
    return JsonResponse(data)

def get_subduksi_data(request):
    base_dir = settings.BASE_DIR
    shp_path = os.path.join(base_dir, 'Subduksi', '2024_Subduction trench_v2.shp')
    data = shp_to_geojson(shp_path, 'TrenchName')
    return JsonResponse(data)
