fruits = ["orange","apple","Grapes"]

def add_fruit(fruits,fruit_to_add):
    fruits.append(fruit_to_add)
    print('fruits insight function',fruits)

fruit_to_add="mango"
add_fruit(fruits,fruit_to_add)
print('Fruits outside function', fruits)

