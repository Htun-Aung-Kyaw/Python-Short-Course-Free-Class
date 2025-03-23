num = input('Enter ID: ')
try:
    i_num = int(num)
except:
    i_num = 'error'

if i_num != 'error':
    print("Correct ID")
else:
    print('Not an ID')


