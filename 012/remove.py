numbers=[1,4,12,23,34,45,56,7,8,9]

def remove_largest(numbers):
    largest=0
    for number in numbers:
        if number > largest:
            largest=number
    numbers.remove(largest)
print("day so ban dau",numbers)
remove_largest(numbers)
print("day so luc sau khi xoa",numbers)