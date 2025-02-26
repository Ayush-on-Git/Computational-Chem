import numpy as np
from data.materials_database import MATERIALS_DATABASE
from utils.advanced_calculations import get_comprehensive_score

def get_recommendations(params):
    """Get material recommendations based on input parameters with advanced calculations."""
    recommendations = []

    for material, properties in MATERIALS_DATABASE.items():
        properties_with_material = {**properties, 'material': material}
        scores = get_comprehensive_score(params, properties_with_material)

        recommendations.append({
            'material': material,
            'score': scores['final_score'],
            'properties': properties['properties'],
            'advantages': properties['advantages'],
            'detailed_scores': {
                'load_capacity': scores['load_capacity_score'],
                'cost_efficiency': scores['cost_efficiency_score'],
                'environmental_impact': scores['environmental_score'],
                'weather_resistance': scores['weather_resistance_score']
            },
            'maintenance_predictions': {
                'interval_years': scores['maintenance_interval'],
                'annual_cost_factor': scores['annual_maintenance_cost']
            }
        })

    # Sort by final score
    recommendations.sort(key=lambda x: x['score'], reverse=True)
    return recommendations