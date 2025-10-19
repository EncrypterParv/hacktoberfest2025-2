n= int(input())
place= 1

sum=0
while n>0:
    a= n%10
    a= (a+1)%10
    sum += a*place
    place *= 10
    n= n//10
print(sum)
