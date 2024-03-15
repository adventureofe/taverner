from sql.generate.element.element_list import element_list

e = {element[0]: index+1 for index, element in enumerate(element_list)}

element_effectivness_list = [
    ("strong"),
    ("weak")
]
