import numpy as np
from typing import Dict, Any

def calculate_load_bearing_capacity(traffic_load: str, material_properties: Dict[str, Any]) -> float:
    """Calculate the load bearing capacity score based on traffic load and material properties."""
    load_factors = {
        'low': 0.6,       # Increased base factors to be less restrictive
        'medium': 0.8,
        'high': 0.9,
        'very high': 1.0
    }

    base_capacity = material_properties['properties']['load_capacity']
    load_multiplier = load_factors.get(traffic_load, 0.8)  # Default to medium if unknown
    durability_factor = material_properties['properties']['durability'] / 10

    return (base_capacity * load_multiplier * durability_factor) * 10

def calculate_cost_efficiency(material_properties: Dict[str, Any]) -> float:
    """Calculate cost efficiency considering initial cost and maintenance."""
    cost = material_properties['properties']['cost']
    durability = material_properties['properties']['durability']
    maintenance_factor = material_properties['properties']['maintenance']

    # Higher score means better cost efficiency
    lifespan_factor = durability * 0.7 + maintenance_factor * 0.3
    cost_factor = (10 - cost) / 10  # Inverse of cost (lower cost = higher score)

    return (lifespan_factor * 0.6 + cost_factor * 0.4) * 10

def calculate_environmental_impact(material_properties: Dict[str, Any], is_recycled: bool) -> float:
    """Calculate environmental impact score."""
    base_score = 6.0  # Lowered default score to allow more variation

    # Adjust score based on material properties
    if is_recycled:
        base_score += 3.0

    # Factor in maintenance (less maintenance = better for environment)
    maintenance_impact = (10 - material_properties['properties']['maintenance']) * 0.2
    base_score += maintenance_impact

    return min(10.0, base_score)  # Cap at 10

def calculate_weather_resistance(weather: str, material_properties: Dict[str, Any]) -> float:
    """Calculate weather resistance score based on conditions."""
    weather_factors = {
        'hot': {'durability_weight': 0.4, 'weather_resistance_weight': 0.6},
        'moderate': {'durability_weight': 0.5, 'weather_resistance_weight': 0.5},
        'cold': {'durability_weight': 0.4, 'weather_resistance_weight': 0.6},
        'wet': {'durability_weight': 0.3, 'weather_resistance_weight': 0.7},
        'dry': {'durability_weight': 0.6, 'weather_resistance_weight': 0.4}
    }

    factors = weather_factors.get(weather, weather_factors['moderate'])
    durability_score = material_properties['properties']['durability']
    weather_resistance = material_properties['properties']['weather_resistance']

    return (durability_score * factors['durability_weight'] + 
            weather_resistance * factors['weather_resistance_weight']) * 10

def calculate_maintenance_prediction(
    material_properties: Dict[str, Any],
    traffic_load: str,
    weather: str
) -> Dict[str, float]:
    """Predict maintenance requirements and lifecycle costs."""
    base_maintenance = material_properties['properties']['maintenance']
    durability = material_properties['properties']['durability']

    # Traffic load impact
    traffic_factors = {'low': 0.7, 'medium': 0.85, 'high': 1.0, 'very high': 1.15}
    traffic_impact = traffic_factors.get(traffic_load, 0.85)

    # Weather impact
    weather_impact = 1.0
    if weather in ['hot', 'wet']:
        weather_impact = 1.15
    elif weather in ['cold']:
        weather_impact = 1.1

    # Calculate maintenance intervals and costs
    maintenance_interval = (durability * 0.7 + (10 - base_maintenance) * 0.3) * 0.5
    maintenance_interval /= (traffic_impact * weather_impact)

    annual_maintenance_cost = (base_maintenance * traffic_impact * weather_impact) / durability * 10

    return {
        'maintenance_interval_years': round(maintenance_interval, 1),
        'annual_maintenance_cost_factor': round(annual_maintenance_cost, 2)
    }

def get_comprehensive_score(params: Dict[str, Any], material_properties: Dict[str, Any]) -> Dict[str, float]:
    """Calculate comprehensive material scoring including all advanced metrics."""
    is_recycled = 'Recycled' in material_properties.get('material', '')

    load_capacity_score = calculate_load_bearing_capacity(params['traffic_load'], material_properties)
    cost_efficiency_score = calculate_cost_efficiency(material_properties)
    environmental_score = calculate_environmental_impact(material_properties, is_recycled)
    weather_resistance_score = calculate_weather_resistance(params['weather'], material_properties)
    maintenance_predictions = calculate_maintenance_prediction(
        material_properties, params['traffic_load'], params['weather']
    )

    # Adjusted weights to be more balanced
    weights = {
        'load_capacity': 0.3,
        'cost_efficiency': 0.25,
        'environmental_impact': 0.2,
        'weather_resistance': 0.25
    }

    final_score = (
        load_capacity_score * weights['load_capacity'] +
        cost_efficiency_score * weights['cost_efficiency'] +
        environmental_score * weights['environmental_impact'] +
        weather_resistance_score * weights['weather_resistance']
    )

    return {
        'final_score': round(final_score, 2),
        'load_capacity_score': round(load_capacity_score, 2),
        'cost_efficiency_score': round(cost_efficiency_score, 2),
        'environmental_score': round(environmental_score, 2),
        'weather_resistance_score': round(weather_resistance_score, 2),
        'maintenance_interval': maintenance_predictions['maintenance_interval_years'],
        'annual_maintenance_cost': maintenance_predictions['annual_maintenance_cost_factor']
    }