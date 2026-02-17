lower=int(input("Enter a lower range:"))
higher=int(input("Enter a higher range:"))
print("Prime numbers between",higher,"and",lower,"are:")
for num in range(lower,higher+1):
    if num>1:
        for i in range(2,num):
          if(num%i)==0:
            break
        else:
           print(num)