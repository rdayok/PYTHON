letter = ("a", "b", "c", "d", "e")
print(letter)
print(type(letter))

# tuple of numbers 1 to 100
numbers = tuple(range(1, 101))
print(numbers)

# Taking the even numbers to form a new tuple
even_numbers = numbers[1:100:2]
print(even_numbers)
odd_numbers = numbers[:100:2]
print(odd_numbers)
added = even_numbers + odd_numbers
print(added)

