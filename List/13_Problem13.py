 #* Q. Given a list containing exactly 3 integers, insert the number 100 at the middle position using a list method.

arr = []

num1 = int(input("Enter a number 1 :"))
arr.append(num1)

num2 = int(input("Enter a number 1 :"))
arr.append(num2)

num3 = int(input("Enter a number 1 :"))
arr.append(num3)

arr.insert(1,100)

print(arr)