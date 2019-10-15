
for i in range(1,6) :
    if i == 3 :
        continue
    else:
        print(i)

sum = 0

print()
print()

for i in range (1,51) :
    sum += i
    i +=1 
    if i == 50 :
        print(sum)

print()
print()

fibonacci = [0,1]
i=0
limit = int(input("set the limit for fibonacci :"))
while i <= limit :
    numnext = fibonacci[i+1] + fibonacci[i]
    fibonacci.append(numnext)
    i += 1
    print(numnext)

print(fibonacci)
print()
print()


for i in range(1,31):
    if i%5 == 0 and i%3 == 0 :
        print("fizzbuzz")
    elif i%5 == 0 :
        print("buzz")
    elif i%3 == 0 :
        print("fizz")
    else :
        print(i)
