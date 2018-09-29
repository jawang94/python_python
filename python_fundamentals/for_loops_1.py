#1 Basic
for count in range(0,151):
    print(count)

#2 Multiples of Five
for count in range(0,1000001):
    if(count%5 == 0):
        print(count)

#3 Count, the Dojo Way
for count in range(0,101):
    if(count%10 == 0):
        print("Dojo")
    elif(count%5 == 0):
        print("Coding")
    else:
        print(count) 

#4 Whoa. That Sucker's Huge
sum = 0
for count in range(0,500000):
    if(count%2 != 0):
        sum += count
print(sum)

#5 Countdown by Fours
for count in range(2018,0,-4):
    print(count)

#6 Flexible Countdown
def flexibleCount(lowNum,highNum,mult):
    for count in range(lowNum,highNum,mult):
        print(count)
x = 5
y = 20
z = 2
flexibleCount(x,y,z)



