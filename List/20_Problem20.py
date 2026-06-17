 #* Q. Given a list containing exactly 5 integers, where the value 100 appears at least once: 1. Print how many times 100 appears  2. Remove one occurrence of 100   3. Print the updated list. 

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

print(arr.count(100))
arr.remove(100)

print(arr)