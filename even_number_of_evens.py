def even_number_of_evens(numbers):
    counter = 0
    for number in numbers:
        if number % 2 == 0 and number >= 1:
            counter += 1
    if counter % 2 == 0 and counter >= 1:
        return True
    # elif counter % 2 != 0:
        # return False
    else:
        return False

assert even_number_of_evens([]) == False, "No numbers"   
assert even_number_of_evens([2]) == False, "One even number"
assert even_number_of_evens([2, 4]) == True, "Two even numbers"
assert even_number_of_evens([2, 3]) == False, "Two numbers, only one even"
assert even_number_of_evens([2, 3, 9, 10, 13, 7, 8]) == False, "Multiple numbers, three even"
assert even_number_of_evens([2, 3, 9, 10, 13, 7, 8, 5, 12]) == True, "Multiple numbers, four even"
assert even_number_of_evens([1, 3, 9]) == False, "No even numbers"

print("All tests passed!")