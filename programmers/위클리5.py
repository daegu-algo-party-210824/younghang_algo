# 모음 사전 
# 모든 경우에 대해서 모두 구한다.
# 중복을 없애기 위해서 set을 이용 
# 그 나머지는 소팅을 이용

def solution(word):
    ret = []
    def function(arr, cnt,value):
        if cnt == 5:
            ret.append(value)
        else :
            for i in range(5):
                function(arr,cnt+1,value+arr[i])
            function(arr,cnt+1,value)

    function(['A','E','I','O','U'],0,'')
    ret = set(ret)
    ret = list(ret)
    ret.sort()
    for i in range(len(ret)) :
        #print(ret[i])
        if ret[i] == word :
            return i
    
    answer = 0
    return answer