# Mencetac bilangan gangil dari 1-100
print(1)
print(3)
print (5) #9st

print()
print()

# cara 2
for j in range(100):
    if j % 2  == 0:
        continue
    print(j)

# cara 3
for j in range(1,100,2):
    print(j)

#cara 4
for j in range(100):
    if j % 2  != 0:
        print(j)

# cara 5
for j in range(1,100):
    if j/2 != int(j/2):
        print(j)
# bilangan prima
for i in range(2,100):
    prima = True
    for j in range(2,i):
        if i % j == 0:
            prima = False
            break
    if prima:
        print(i)