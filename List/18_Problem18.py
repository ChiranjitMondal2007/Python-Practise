 #* Q. Given a list containing exactly 5 integers, remove the middle element and print: 1. The removed element  2. The updated list

arr = []

num1 = int(input("Enter a number 1 :"))
arr.append(num1)

num2 = int(input("Enter a number 1 :"))
arr.append(num2)

num3 = int(input("Enter a number 1 :"))
arr.append(num3)

num4 = int(input("Enter a number 1 :"))
arr.append(num4)

num5 = int(input("Enter a number 1 :"))
arr.append(num5)

print(arr.pop(2))

print(arr)