# For Loop

obj = [2, 3, 5, 7, 9]
for i in obj:
    print(i)

for i in obj:
    print(i*2)

for j in range(1, 6):
    print(j)

summation = 0
for j in range(1, 6):
    summation = summation + j
print(summation)

for k in range(1, 10, 2):
    print(k)

for m in range(10):
    print(m)

# While loop
print("********************")

it = 10
while it > 1:
    if it == 9:
        it = it - 1
        continue
    if it == 3:
        break
    print(it)
    it = it - 1
print("While loop execution completed")
