# 글로벌 변수 테스트 
# 값이 일치하지만 않으면 밖에 있는 변수를 사용할 수 있다.

def solution(a,b):
    arr = [1,2,3,4]

    def function(a,b):
        # 여기서 보듯이 그냥 전역변수처럼만 쓰면된다.
        # 대신 변수 값이 동일하면 
        return arr

    print(function(a,b))
    
    return a+b


print(solution(1,2))