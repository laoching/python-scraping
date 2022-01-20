hap=0
chong=0
score={'A+':4.3, 'A0':4.0, 'A-':3.7, 'B+':3.3,'B0':3.0,'B-':2.7,'C+':2.3,'C0':2.0,'C-':1.7,'D+':1.3,'D0':1.0,'D-':0.7,'F':0.0}
n=int(input())
for i in range(n):
	sub,si,hak=input().split()
	si=int(si)
	chong+=si
	hap+=si*score[hak]
print("%.2f"%(round(hap/chong+10**-10,2)))