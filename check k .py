
n,k=map(int,input().split())
x=list(map(int,input().split()))
for i in range(0,n,1):
	if x[i]==k:
		if i>0:
			print("yes")
		else:
			print("no")
