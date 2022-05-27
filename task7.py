#1. Write a Python program to get the smallest number from a list.
# def smallest():
#     small=1
#     a=[1,2,3,4,5,6,7]
#     for i in  a:
#         if i < small:
#             small=i
#     return(small)
# print(f"smallest number is {smallest()}")            


#2.  Write a Python function to check a list is empty or not.
# def empty():
#     a=[1,2]
#     if  a:
#         print("not empty")
#     else:
#         print("empty")
# empty()

#3.  Write a Python program to select an item randomly from a list.
# import random
# a=[1,2,3,4,5]
# print(random.choice(a))

#4.  Write a Python program to copy a list.
# a=[1,2,3,4]
# b=[]
# b=a.copy()
# print(a)
# print(b)

#5.  Write a Python program to find the 2nd largest number in a list.
# a=[1,2,6,12,7,9,50,5]
# largest=a[0]
# for i in a:
#     if i>largest:
#         t = largest
#         largest=i
# print(f"second largest number is second {t}") 

#6.Write a Python program to print a specified list after removing the 3rd elements.
# a=[15,34,3,434,43,2,3,4,5]
# b=[]
# for i in range(len(a)):
#     if(i!=2):
#         b.append(a[i])
# print(b)

# 7. Write a Python program to count the number of even and odd numbers from a series of numbers.
# a=[1,4,7,10,15,20,17,19,8]
# even=0
# odd=0
# for i in a: 
#     if i%2==0:
#         even=even+1
#     else:
#         odd=odd+1
# print("even number in series are:",(even))
# print("odd number in series are:",(odd))

# 8. Write a Python program to add an item in a tuple.
a=(1,2,4,6)
a=list(a)
a.append(9)
a=tuple(a)
print(a)










        

   





   
    
