number = int(input("Enter new term value (not exceeding): "))

def fibonacci(n):
    if n in {0, 1}:  # Base case
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

result = 0
count = 0
while result < number:
    count += 1
    val = [fibonacci(n) for n in range(count)]
    data = [i if (i % 2 == 0) else 0 for i in val]
    result = sum(data)

print("The output is: {}".format(result))

