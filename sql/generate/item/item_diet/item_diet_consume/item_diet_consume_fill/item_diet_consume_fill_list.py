from sql.generate.item.item_diet import item_diet_list
from sql.generate.item.item_diet.item_diet_consome.item_diet_consume_list import item_diet_consume_list

d = {diet: index + 1 for index, diet in enumerate(item_diet_list)}
c = {consume[0]: index+1 for index, consume in enumerate(item_diet_consume_list)}



item_diet_consume_fill_list = [
    *( (d["alcohol"], c[consume]) for consume in ["delectable", "delicious", "nutritious", "tasty", "palatable", "acceptable", "toxic"]),

    *( (d["bug"], c[consume]) for consume in ["palatable", "acceptable", "edible", "monotonous", "tough", "offensive", "inedible", "harmful", "mind-altering", "toxic"]),
    
    *( (d["diary"], c[consume]) for consume in ["delectable", "delicious", "nutritious", "tasty", "palatable", "offensive", "inedible", "toxic"]),
    
    *( (d["fungus"], c[consume]) for consume in ["delectable", "delicious", "nutritious", "tasty", "palatable", "edible", "offensive", "inedible", "harmful", "mind-altering", "toxic"]),

    *( (d["gemstone"], c[consume]) for consume in ["hard", "solid", "inedible", "harmful"]),
 
    *( (d["meat large"], c[consume]) for consume in ["delicious", "nutritious", "tasty", "palatable", "acceptable", "edible", "monotonous", "tough", "offensive", "inedible", "harmful", "toxic"]),

    *( (d["meat medium"], c[consume]) for consume in ["tasty", "palatable", "acceptable", "edible", "monotonous", "tough", "offensive", "inedible", "harmful", "toxic"]),

    *( (d["meat small"], c[consume]) for consume in [ "palatable", "acceptable", "edible", "monotonous", "offensive", "inedible", "toxic"]),

    *( (d["metal"], c[consume]) for consume in ["solid", "inedible", "harmful", "toxic"]),

    *( (d["plant grass"], c[consume]) for consume in ["delectable", "delicious", "nutritious", "tasty", "palatable", "acceptable", "edible", "monotonous", "tough", "hard", "solid", "offensive", "inedible", "harmful", "mind-altering", "toxic"]),

    *( (d["plant hard root"], c[consume]) for consume in ["monotonous", "tough", "hard", "solid", "toxic"]),

    *( (d["plant soft root"], c[consume]) for consume in ["acceptable", "edible", "monotonous", "tough", "hard", "solid", "inedible", "mind-altering"]),


    *( (d["rock"], c[consume]) for consume in ["solid", "inedible", "harmful"]),

    *( (d["shellfish"], c[consume]) for consume in ["delectable", "delicious", "nutritious", "tasty", "offensive", "inedible", "toxic"]),


    *( (d["vegetable"], c[consume]) for consume in ["nutritious", "tasty", "palatable", "acceptable", "edible", "monotonous", "tough", "offensive", "inedible", "harmful", "toxic"]),
   
    *( (d["vermin"], c[consume]) for consume in ["offensive", "inedible", "harmful", "toxic"]),

    *( (d["wood"], c[consume]) for consume in ["hard", "solid", "inedible", "harmful"])
]
