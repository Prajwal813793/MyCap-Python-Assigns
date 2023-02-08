# the start and end of the range are accepted from the user using the input function 

start = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))

positive_numbers = []

#A for loop is then used to iterate through the numbers in the range, and an if statement checks if each number is greater than 0
#If it is greater than 0, then it is added to the positive_numbers list
for num in range(start, end + 1):
    if num > 0:
        positive_numbers.append(num)

print("Positive numbers:", positive_numbers)

