def find_largest_number(numbers):
    if not numbers:
        return None
    largest = numbers[0]
    for number in numbers:
        if number > largest:
            largest = number
    return largest

# Example usage
numbers = [10, 20, 4, 45, 99]
print("The largest number is:", find_largest_number(numbers))