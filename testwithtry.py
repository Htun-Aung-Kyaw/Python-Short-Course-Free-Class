num = input('Enter ID: ')
try:
    i_num = int(num)
except:
    i_num = 'c'

if i_num != 'c':
    print("Correct ID")
else:
    print('Not an ID')


