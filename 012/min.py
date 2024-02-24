numbers=[1,3,4,5,7,8,-1,24,53,-2]
def tim(numbers):
    min=numbers[1]
    for i in range(len(numbers)):
        if min>numbers[i]:
            min=numbers[i]
    return min
print(tim(numbers))