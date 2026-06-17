 #* Q. Given a list containing exactly 4 integers, remove the value 100 using a list method and print the updated list.  


arr = []

num1 = int(input("Enter a number 1 :"))
arr.append(num1)

num2 = int(input("Enter a number 1 :"))
arr.append(num2)

num3 = int(input("Enter a number 1 :"))
arr.append(num3)

num4 = int(input("Enter a number 1 :"))
arr.append(num4)

arr.remove(100)

print(arr)