
passes = 0
failures = 0

for students in range(10):
    result = int(input("Enter result (1 = pass, 2 = failure): "))
    while 0 > result > 2:
        result = int(input("Enter result (1 = pass, 2 = failure): "))

    if result == 1:
        passes = passes + 1
    else:
        failures = failures + 1

print("Passed: ", passes)
print("Failed: ", failures)

if passes > 8:
    print("Bonus to instructor")
