n,k=map(int,input().split())
x=list(map(int,input().split()))
c=0
for i in range(0,n):
	if x[i]==k:
		 c=c+1
print(c)
