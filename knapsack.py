n,m =list( map (int,input().split("")))

v=[]
w=[]
#파이썬 이차월 배열 주의.
dp = [[0]* n for _ in range(m*n)] 

for i in range(n) :
    
