def fib(x):
	if(x==0):
		global ax
		ax=0
		return 0
	elif(x==1):
		global bx
		bx=1
		return 1
	else:
		global cx
		cx=ax+bx
		ax=bx
		bx=cx
		return (cx)

ax=bx=cx=0
n=int(input("enter any number"))
leave=tempx=numa=numb=finalanswer=x=finaldigit=0
a=[]
finaldigit=[]
while(leave==0):
	a.append((fib(x)%n))
	if((x+1)%2==0):
		tempx=int(x/2)
		if(a[0:(tempx+1)]==a[(tempx+1):len(a)]):
			leave=1
			finalanswer=tempx
			finaldigit=a[0:(tempx+1)]
	x=x+1
	numa=numb=0
print("The frequency of repeatation is ",finalanswer+1)
print("the repeating sequence is")
print(finaldigit)
