while True:
    print('Please input your ID')
    name = input()
    if name != 'bob':
        continue
    #elif name != 'bob':
     #   break
    print('Please provide the password')
    password = input()
    if password == 'bob':        
        break
        print('wrong password')
print('Welcome')

name = ''
while not name:
    print('Enter your Name')
    name=input()
print('How many')
num = int(input())
if num:
    print('Be Sure')
print('Done')
