print('Hello! My name is Aid.')
print('I was created in 2020.')
print('Please, remind me your name.')

name = input()

print('What a great name you have, ' + name + '!')
print('Let me guess your age.')
print('Enter remainders of dividing your age by 3, 5 and 7.')

age = (int(input()) * 70 + int(input()) * 21 + int(input()) * 15) % 105

print("Your age is " + str(age) + "; that's a good time to start programming!")
print('Now I will prove to you that I can count to any number you want.')

maxCount = int(input())
count = 0
while count <= maxCount:
    print(count, "!")
    count += 1

print('Completed, have a nice day!')
