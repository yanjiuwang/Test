import sys
lines=sys.stdin.readlines()
N,V=list(map(eval,lines[0].strip().split()))
li=[]
f=[[0]*(V+1)  for _ in range(N)]
print(f)
for line in lines[1:]:
    x=list(map(eval,line.strip().split()))
    li.append(x)
print(li)