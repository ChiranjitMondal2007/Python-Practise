arr = []

nums1 = int(input("Enter a number 1 :"))
arr.append(nums1)

nums2 = int(input("Enter a number 2 :"))
arr.append(nums2)

nums3 = int(input("Enter a number 3 :"))
arr.append(nums3)

newarr =[]
newarr.append(arr[0])
newarr.append(arr[-1])

print(newarr)
