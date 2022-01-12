import sys
input = sys.stdin.readline

c=int(input())
for i in range(c):
	tot=map(int,input().split())
	tot=list(tot)
	stu=tot[0]

	cnt=0
	score=tot[1:]

	avg=sum(score)//len(score)
	for j in score:
		if j > avg:
			cnt+=1
	print("{:.3f}".format(round(float((cnt/stu)*100),3)),'%',sep='')
