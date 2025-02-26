import numpy as np
from data.materials_database import MATERIALS_DATABASE

def calculate_material_score(material_properties, params):
    """Calculate material suitability score based on input parameters."""
    score = 0
    weight_factors = {
        'traffic_load': 0.35,
        'weather': 0.25,
        'soil_type': 0.25,
        'durability': 0.15
    }
    
    # Traffic load compatibility
    if params['traffic_load'] in material_properties['suitable_conditions']['traffic_load']:
        score += 100 * weight_factors['traffic_load']
    
    # Weather compatibility
    if params['weather'] in material_properties['suitable_conditions']['weather'] or \
       'all' in material_properties['suitable_conditions']['weather']:
        score += 100 * weight_factors['weather']
    
    # Soil type compatibility
    if params['soil_type'] in material_properties['suitable_conditions']['soil_type'] or \
       'all' in material_properties['suitable_conditions']['soil_type']:
        score += 100 * weight_factors['soil_type']
    
    # Property scores
    property_score = np.mean([
        material_properties['properties']['durability'],
        material_properties['properties']['weather_resistance'],
        material_properties['properties']['load_capacity']
    ]) * 10
    
    score += property_score * weight_factors['durability']
    
    return score

def get_recommendations(params):
    """Get material recommendations based on input parameters."""
    recommendations = []
    
    for material, properties in MATERIALS_DATABASE.items():
        score = calculate_material_score(properties, params)
        recommendations.append({
            'material': material,
            'score': score,
            'properties': properties['properties'],
            'advantages': properties['advantages']
        })
    
    # Sort by score
    recommendations.sort(key=lambda x: x['score'], reverse=True)
    return recommendations
