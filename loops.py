#LOOPS

#for loops
people = ['John', 'Tim', 'bob']

for person in people: 
    print('Current person: ', person)

#iterate by seq index 
for i in range (len(people)):
    print("current person: ", people[i])

for i in range(0, 10):
    print(i)

#while loops 
count = 0

while count < 10:
    print('Count:', count)
    if count == 5: 
        break
    count = count + 1