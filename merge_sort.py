# This is merge sort
# Copyright 2018 Rohan Nayak Mallick

import random
import math
a = []
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
for x in range(l):
    a[x] = [a[x]]
while True:
    l = len(a)
    for x in range(0 , math.floor(l/2)):
        s = []
        while True:
            if a[x][0] < a[x+1][0]:
                s.append(a[x][0])
                a[x].remove(a[x][0])
            else:
                s.append(a[x+1][0])
                a[x+1].remove(a[x+1][0])
            if a[x] == []:
                s.extend(a[x+1])
                break
            if a[x+1] == []:
                s.extend(a[x])
                break
        a.remove(a[x+1])
        a[x] = s
    if len(a) == 1:
        break            
print(a[0])
print('Sorted!')
        
