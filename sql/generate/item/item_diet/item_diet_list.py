from sql.generate.item.item_diet.item_consumability.item_consumability import item_consumability_list

c = {consumability[0]: index+1 for index, consumability in enumerate(item_consumability_list)}

item_diet_list = [
    # name #consumability
    ('fungus', 10),
    ('wood', 4),
    ('gemstone', 2),
    ('rock', 1),
    ('meat large',5 ),
    ('meat medium', 7),
    ('shellfish', 8),
    ('alcohol', 7),
    ('general', 4),
    ('vermin', 2),
    ('diary', 8),
    ('meat small', 8),
    ('bug small', 5),
    ('harsh veg', 4),
    ('soft veg', 6),
    ('metal', 1)
]
