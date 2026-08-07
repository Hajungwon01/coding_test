a = int(input())

tmp = a%2
if tmp == 0: 
    status = 'even' 
else: 
    status = 'odd'
print(f'{a} is {status}')