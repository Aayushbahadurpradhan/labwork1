# Write a Python program to guess a number between 1 to 9.
import random
a=int(input("enter a number"))
b= random.randint(1, 10)
while a!= b:
    b= int(input('Guess a number between 1 to 10 '))
print('Well guessed!')

target_random, guess_num = random.randint(1,10), 0
while target_random != guess_num:
    guess_num = int(input('guess a number between 1 to 10 until you get right num'))
print('well guessed')