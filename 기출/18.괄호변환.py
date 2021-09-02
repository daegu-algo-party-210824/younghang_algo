def solution(p):
    # 균형잡힌 괄호 판단 방법.
    # 올바른 괄호 판단 방법.
    def make_uv(p) :
        r = 0
        l = 0
        for i in range(len(p)) :
            if p[i] == '(':
                l +=1
            else :
                r +=1
            if l == r :
                break      
        return p[:i+1], p[i+1:]
    #균형 잡힌 괄호 문자열임을 판단하는 것.
    def check(s) :
        temp = 0
        for i in range(len(s)):
            if s[i] == '(' :
                temp+=1
            else :
                temp -=1
            if temp < 0 :
                return False
        
        return temp == 0 
    
    
    if  not p : #1번
        return ''
    else :
        #2번
        u,v = make_uv(p)
        #3번
        if check(u) == True :
            return u + solution(v)
        #4번
        else :
            temp = '('
            temp += solution(v)
            temp += ')'
            
            u = u [1:-1]      #잘 짤랐네 
            for i in range(len(u)):
                if u[i] == '(' :
                    temp += ')'
                else :
                    temp += '('
            return temp