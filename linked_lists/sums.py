def find_two_sum(numbers, target_sum):
    for num in numbers:
        possible_number = target_sum - num
        if possible_number in numbers:
            return [possible_number, num]
        else:
            return None

numbers = [3,1,5,7,5,9]
print(find_two_sum(numbers, 10))