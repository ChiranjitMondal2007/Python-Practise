arr = []

num1 = int(input("Enter a number 1 :"))
arr.append(num1)

num2 = int(input("Enter a number 2 :"))
arr.append(num2)

num3 = int(input("Enter a number 3 :"))
arr.append(num3)

newarr = []

newarr.append(arr[0])
newarr.append(arr[1])
newarr.append(arr[-1])
newarr.append(arr[1])

print(newarr)