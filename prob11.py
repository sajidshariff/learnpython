# Write a Python program to create a histogram from a given list of integers.
def histogram(numbers):
    for num in numbers:
        output = ''
        times = num
        while( times > 0 ):
          output += '*'
          times = times - 1
        print(output)

histogram([2, 3, 6, 5])
print('')
histogram([1,2, 3, 4, 5, 6, 7, 8, 9, 10])
