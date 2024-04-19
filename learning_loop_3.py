#Control structures

#if-else Statement is used for decision-making based on conditions.
age = 18
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

#for Loop:A for loop is used to iterate over a sequence (such as a list, tuple, string, or dictionary) and execute a block of code for each element in the sequence..
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

#while Loop is used for executing a block of code repeatedly as long as a condition is true.
count = 0
while count < 5:
    print(count)
    count += 1

# the break statement is used to exit (or break out of) a loop prematurely. -is used in for Loop and While Loop conditions

fruits = ["apple", "banana", "cherry", "date", "elderberry"]

for fruit in fruits:
    print(fruit)
    if fruit == "cherry":
        break # goes at the end.