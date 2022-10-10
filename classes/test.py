# print("Hello " + input("What is your name?"))

# print(len(input("What is your name")))

#   Using in variables
# name=input("What is your name? ")
# length=len(name)
# print(length)

#indexing using
# print("Hello"[0])
# print("123"+"234")
# print(123+345)

#Indexing using with input function and input function using taking as an input name and index using 
# name=input("Enter your name")
# jannu=input("please enter your index")
# print(name[int(jannu)])

#We are using a type casting
# num_char=len(input("What is your name? "))
# new_num_char=str(num_char)
# print("your name has" + new_num_char + "characters")

#add two number using indexing metheod
# user_input=input("please enter two digit integer: ")
# a=user_input[0]
# b=user_input[1]
# sum= int(a) + int(b)
# print("Given integer sum is " , sum)

#conditional statements(check even or odd number)
# rx=input("Enter your number you want to check")
# xy=int(rx)
# if(xy%2==0):
#     print("even")
# else:
#     print("odd")

#Example of conditional statement(leap year or not)
# year=input("please enter year which one you want to check leap or not leap year")
# ioi=int(year)
# if(ioi%4==0):
#     if(ioi%100==0):
#         if(ioi%400==0):
#             print("This is a leap year")
#         else:
#             print("This is not a leap year")
#     else:
#         print("This is a leap year")
# else:
#     print("This is not a leap year") 

# x="RAVI RANJAN SINGH".lower()
# y="ravi ranjan singh".upper()
# z="RAVI RANJAN SINGH".count("I") (hERE NO CONSIDER UPPER LOWER HERE CONSIDER ONLY WHICH WAY TO SEARCH UPPER OR LOWER BUT IF YOU WANT TO ALL SAME LEETTER FOUNT IN ANY WORD FIRSTLT CONVERT INTO UPPER OR LOWER CASE THEN YOU CAN EASILY FIND THIS LETTER)
# print(x,y,z)               

#HOW CAN WE USING OTP 4 DIGIT
# import random
# x=random.randint(1111,9999)
# print(x)
                
                #file handling 
# f = open("abc.txt", "r")
# # for x in f:
# #     print(x)
# print(f.readline())
# f.close()

#append vale in a spacific file
# f = open("abc.txt", "a")
# f.write("Now the file has more content!")
# f.close()

# #open and read the file after the appending:
# f = open("abc.txt", "r")
# print(f.read())

#over write
# f = open("abc.txt", "w")
# f.write("Now the file has more content!")
# f.close()

# #open and read the file after the appending:
# f = open("abc.txt", "r")
# print(f.read())


# f = open("myfile.txt", "r")
# f = open("myfile.txt", "a")
# f.write("Now the file has more kdfkjdfoafn content!")
# f = open("myfile.txt", "r")
# print(f.readline())
# f.close

# import os
# os.remove("myfile.txt")

# import os
# if os.path.exists("abc.txt"):
#   os.remove("abc.txt")
# else:
#   print("The file does not exist")

# import os
# os.rmdir("avc")

from itertools import count


string = [10,12,14,16,18,12]
# print(string.find('can'))
# print(string.find('I',10,15))
# print(string.find('you',15))
# a=string.find('good day')
# if a!=-1:
#     print('The string contains "good day"')
# else:
#     print('The string does not contain "good day"')
print(len(string))
print(count(string))
