MATERIALS_DATABASE = {
    'Asphalt Concrete': {
        'properties': {
            'durability': 8,
            'cost': 7,
            'weather_resistance': 7,
            'load_capacity': 8,
            'maintenance': 6
        },
        'suitable_conditions': {
            'traffic_load': ['medium', 'high'],
            'weather': ['moderate', 'hot'],
            'soil_type': ['granular', 'rocky']
        },
        'advantages': [
            'Good load distribution',
            'Smooth riding surface',
            'Quick construction',
            'Recyclable'
        ]
    },
    'Portland Cement Concrete': {
        'properties': {
            'durability': 9,
            'cost': 8,
            'weather_resistance': 9,
            'load_capacity': 9,
            'maintenance': 8
        },
        'suitable_conditions': {
            'traffic_load': ['high', 'very high'],
            'weather': ['all'],
            'soil_type': ['all']
        },
        'advantages': [
            'High durability',
            'Low maintenance',
            'Long service life',
            'High load capacity'
        ]
    },
    'Gravel': {
        'properties': {
            'durability': 5,
            'cost': 4,
            'weather_resistance': 5,
            'load_capacity': 5,
            'maintenance': 4
        },
        'suitable_conditions': {
            'traffic_load': ['low', 'medium'],
            'weather': ['moderate', 'dry'],
            'soil_type': ['granular', 'rocky']
        },
        'advantages': [
            'Low cost',
            'Easy construction',
            'Good drainage',
            'Simple maintenance'
        ]
    }
}

WEATHER_CONDITIONS = ['hot', 'moderate', 'cold', 'wet', 'dry']
TRAFFIC_LOADS = ['low', 'medium', 'high', 'very high']
SOIL_TYPES = ['granular', 'rocky', 'clayey', 'silty']
