l=[]
t=0
u=0
n=input("Enter money in the houses with space ' ' between them:")
l=n.split()
for i in range(0,len(l)):
    l[i]=int(l[i])
print(l)
for i in range(0,len(l),2):
    t+=l[i]
    
# print(t)
for i in range(1,len(l),2):
    u+=l[i]
# print(u)
print("maximum money you can rob:"+ str(u if u>t else t))
