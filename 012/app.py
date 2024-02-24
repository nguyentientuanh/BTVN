expenses=["ban-500-2102","ghe-500-2102","tivi-500-2102"]
def add_item(myTempList, item):
    myTempList.append(item)

def find(myTempList, item_name):
    result = -1
    length = len(myTempList)
    for i in range(length):
        if myTempList[i]==item_name:
            result = i
    return result

def remove_item(myTempList, item_name):
    if find(myTempList, item_name) > -1:
        del myTempList[find(myTempList, item_name)]
    else:
        print(item_name + " not in list")
print("Your expenses:", expenses)

print("What do you want to do? -\n"\
        "1. Add\n" \
        "2. Remove")

option = int(input("Select option 1 or 2: "))
name_input = input("Item name: ")

if option == 1:
    add_item(expenses, name_input)
    print("Your expenses: ", expenses)
elif option == 2:
    remove_item(expenses, name_input)
    print("Your expenses: ", expenses)
else:
    print("Invalid input")

    