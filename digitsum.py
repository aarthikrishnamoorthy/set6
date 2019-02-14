x=int(input())
ds=0
while x!=0:
	ds=ds+x%10
	x=x//10
print(ds)
