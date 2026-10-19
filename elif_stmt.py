num=int(input('Enter the number: '))
if 0<=num<=9:
    print('Single digit number.')
elif 10<=num<=99:
    print('Double digit number.')
elif 100<=num<=999:
    print('Triple digit number.')
else:
    print(len(str(num)), 'is the length of given number.')