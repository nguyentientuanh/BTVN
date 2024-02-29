products = {
            'SMART WATCH': 550,
            'PHONE' : 1000,
            'PLAYSTATION': 500,
            'LAPTOP' : 1550,
            'MUSIC PLAYER' : 600,
            'TABLET' : 400 
           }

def display(products,price):
    for item in products:
        if products[item]<=price:
            print(item,":",products[item])
price=int(input("nhap gia tien:"))

display(products,price)