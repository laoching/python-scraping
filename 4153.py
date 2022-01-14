d=[]
while 1:
	a,b,c=map(int,input().split())
	d=[a,b,c]
	if a==b==c==0:
		exit()
	elif (d[0]**2+d[1]**2+d[2]**2)-(max(d)**2)==max(d)**2:
		print("right")
	else:
		print("wrong")
