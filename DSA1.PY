                    # BEGINNER LEVEL
# ARRAY BASED QUESTION
# print elements
# from array import *
# values = list(map(int,input("enter elements:").split()))
# arr = array('i',values)
# print(arr)

# sum elements
# from array import *
# values = list(map(int,input("enter elements:").split()))
# arr = array('i',values)
# print(sum(arr))

# find maximum minimum
# from array import *
# values = list(map(int,input("enter elements:").split()))
# arr = array('i',values)
# print("Max:",max(arr))
# print("Min:",min(arr))

# count how many time elments occurs in array
#from array import *
# values = list(map(int,input("enter elements:").split()))
# arr = array('i',values) 
# x = 4
# print(arr.count(x))

#  exists number in array
# from array import *
# values = list(map(int,input("enter elements:").split()))
# arr = array('i',values) 
# x = 4
# if x in arr:
#     print("exist")
# else:
#     print("not exist")

# remove all even numbers
# arr = [2 ,4 ,3, 5]
# arr = [x for x in arr if x %2 !=0]
# print(arr)

# insert element
# from array import *
# values = list(map(int,input("enter elements:").split()))
# arr = array('i',values)
# arr.insert(0,10)
# print(arr)

                #    INTERMEDIATE LEVEL
# find second largest number
# from array import *
# values = list(map(int,input("enter elements:").split()))
# arr = array('i',values)
# new = list(set(arr))
# new.sort()
# print("second largest number:",new[-2])

# find average of all elements
# from array import *
# values = list(map(int,input("enter elements:").split()))
# arr = array('i',values)
# average = sum(arr)/len(arr)
# print("Average:",average)

# Remove duplicates from the array
# from array import *
# values = list(map(int,input("enter elements:").split()))
# arr = array('i',values)
# arr=list(set(arr))
# print(arr)

# Rotate thr array to the right by 1 position
# from array import *
# values = list(map(int,input("enter elements:").split()))
# arr = array('i',values)
# arr = [arr[-1]] + [arr[:-1]]
# print(arr)

# Sort an array in asc order without using sorted()
# from array import *
# values = list(map(int,input("enter elements:").split()))
# arr = array('i',values)
# for i in range(len(arr)):
#     for j in range(i+1,len(arr)):
#         if arr[j]>arr[i]:
#             arr[i],arr[j] = arr[j],arr[i]
# print(arr)

# Split the array into two halves
from array import *
values = list(map(int,input("enter elements:").split()))
arr = array('i',values)
mid = len(arr)//2
print("first half:",arr[:mid])
print("second half:",arr[mid:])
