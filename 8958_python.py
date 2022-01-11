n=int(input())
score=0
for i in range(n):
    score = 0
    t=input()
    cnt=1
    for j in t:
        if j=='O':
            score+=cnt
            cnt+=1
        else:
            cnt=1
    print(score)