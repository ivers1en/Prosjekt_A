
start = 1
end = 100
countersteps = 1

for i in range(start, end, countersteps):

    if i % 3 == 0:
        print(str(i) + " Fizz alfred yoyooyo")
    
    if i % 5 == 0:
        print(str(i) + " Buzz stein yoyoyoyo")

    else:
        print(i)