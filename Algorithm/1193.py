a = int(input())

num = 0
count = 0

while count < a:
    num +=1
    count +=num

b= count-a

if num%2==1:
    print("{0}/{1}".format(1+b,num-b))
else:
    print("{0}/{1}".format(num-b,1+b))