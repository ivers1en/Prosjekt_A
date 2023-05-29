
start = 1
end = 100
countersteps = 1

for i in range(start, end, countersteps):

    if i % 3 == 0:
        print(str(i) + " Fizz halleluja")
    
    if i % 5 == 0:
        print(str(i) + " Buzz madafakka")

    else:
        print(i)