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
    },
    'Bitumen': {
        'properties': {
            'durability': 7,
            'cost': 6,
            'weather_resistance': 6,
            'load_capacity': 7,
            'maintenance': 5
        },
        'suitable_conditions': {
            'traffic_load': ['medium', 'high'],
            'weather': ['moderate', 'hot'],
            'soil_type': ['granular', 'rocky']
        },
        'advantages': [
            'Flexible pavement',
            'Water resistant',
            'Good skid resistance',
            'Cost-effective'
        ]
    },
    'Cobblestone': {
        'properties': {
            'durability': 8,
            'cost': 7,
            'weather_resistance': 8,
            'load_capacity': 6,
            'maintenance': 7
        },
        'suitable_conditions': {
            'traffic_load': ['low', 'medium'],
            'weather': ['all'],
            'soil_type': ['granular', 'rocky']
        },
        'advantages': [
            'Aesthetic appeal',
            'Long lifespan',
            'Good drainage',
            'Historical value'
        ]
    },
    'Recycled Asphalt': {
        'properties': {
            'durability': 7,
            'cost': 5,
            'weather_resistance': 6,
            'load_capacity': 7,
            'maintenance': 6
        },
        'suitable_conditions': {
            'traffic_load': ['medium', 'high'],
            'weather': ['moderate', 'hot'],
            'soil_type': ['granular', 'rocky']
        },
        'advantages': [
            'Environmentally friendly',
            'Cost-effective',
            'Reduced waste',
            'Similar performance to new asphalt'
        ]
    },
    'Brick': {
        'properties': {
            'durability': 7,
            'cost': 6,
            'weather_resistance': 7,
            'load_capacity': 5,
            'maintenance': 6
        },
        'suitable_conditions': {
            'traffic_load': ['low', 'medium'],
            'weather': ['all'],
            'soil_type': ['granular', 'rocky']
        },
        'advantages': [
            'Aesthetic appeal',
            'Good drainage',
            'Easy repairs',
            'Long lifespan'
        ]
    },
    'Macadam': {
        'properties': {
            'durability': 6,
            'cost': 5,
            'weather_resistance': 6,
            'load_capacity': 6,
            'maintenance': 5
        },
        'suitable_conditions': {
            'traffic_load': ['low', 'medium'],
            'weather': ['moderate', 'dry'],
            'soil_type': ['granular', 'rocky']
        },
        'advantages': [
            'Simple construction',
            'Good drainage',
            'Cost-effective',
            'Historical significance'
        ]
    },
    'Composite Pavement': {
        'properties': {
            'durability': 9,
            'cost': 9,
            'weather_resistance': 8,
            'load_capacity': 9,
            'maintenance': 7
        },
        'suitable_conditions': {
            'traffic_load': ['high', 'very high'],
            'weather': ['all'],
            'soil_type': ['all']
        },
        'advantages': [
            'High durability',
            'Reduced maintenance',
            'Superior performance',
            'Versatile application'
        ]
    },
    'Rubberized Asphalt': {
        'properties': {
            'durability': 8,
            'cost': 8,
            'weather_resistance': 7,
            'load_capacity': 8,
            'maintenance': 7
        },
        'suitable_conditions': {
            'traffic_load': ['medium', 'high'],
            'weather': ['moderate', 'hot'],
            'soil_type': ['granular', 'rocky']
        },
        'advantages': [
            'Noise reduction',
            'Better skid resistance',
            'Environmental benefits',
            'Longer service life'
        ]
    }
}

WEATHER_CONDITIONS = ['hot', 'moderate', 'cold', 'wet', 'dry']
TRAFFIC_LOADS = ['low', 'medium', 'high', 'very high']
SOIL_TYPES = ['granular', 'rocky', 'clayey', 'silty']