n=int(input("Enter a even number"))
if n%2==0:
    l=[]
    for i in range(1,n):
        for j in range(2,i):
            if i%j==0:
                break
        else:l.append(i)
    for k in l:
        if n-k in l:
            print(k,'+',n-k,'=' ,n)
            break
else:print("You've entered a wrong input")
