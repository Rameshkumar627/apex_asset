val = input("Enter natural numbers: ")

try:
    number = int(val)
    data = [i if (i % 3 == 0) | (i % 5 == 0) else 0 for i in range(0, number)]
    result = sum(data)
    print("The output is: {}".format(result))

except:
    print("Number is not an natural number")


