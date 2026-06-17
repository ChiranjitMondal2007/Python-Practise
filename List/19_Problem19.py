 #* Q. Given a list containing exactly 3 integers, insert:1. 100 at index 1  2. 200 at index 3

arr = []

num1 = int(input("Enter a number 1 :"))
arr.append(num1)

num2 = int(input("Enter a number 1 :"))
arr.append(num2)

num3 = int(input("Enter a number 1 :"))
arr.append(num3)

arr.insert(1,100)
arr.insert(3,200)

print(arr)