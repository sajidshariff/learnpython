# Write a Python program to test whether a passed letter is a vowel or not.
vowels_list = ['a','e','i','o','u']

input_letter = input("Enter a letter of your choice: ")
entered_letter = str(input_letter[0])
if entered_letter in vowels_list:
    print(f'{entered_letter} is a vowel')
else:
    print(f'{entered_letter} is not a vowel')