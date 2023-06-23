#With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary.
# Suppose the following input is supplied to the program: 8

dict_i = {}
entered_number = int(input("Enter an integer: "))
for num in range(1,entered_number+1):
    dict_i[num] = num*num
print(dict_i)