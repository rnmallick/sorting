a = []
import random
generate = input('Do you want to choose your numbers, or should the computer generate some? Type computer or player.')
if generate == 'computer':
    start = int(input('First boundary:'))
    end = int(input('Second bondary:'))
    number = int(input('Number of numbers:'))
    for q in range(number):
        a.append(random.randint(start , end))
if generate == 'player':
    print('Type your elements. Say stop when you want to stop.')
    while True:
        z = input('Number:')
        try:
            t = int(z)
            a.append(t)
        except ValueError:
            break
print('Here is your list:',a)
l = len(a) 
for x in range(1 , l):
    for y in range(x):
        if a[x] < a[y]:
            s = a[x]
            a[x] = a[y]
            a[y] = s
print(a)    
print('Sorted!')
