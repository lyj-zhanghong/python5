def calculate(n,left,right):
    L = left
    R = right
    while L>=0 and R<n and s[L] == s[R]:
        L = L-1
        R = R+1
    return R-L-1;

if __name__ == '__main__':
    s = input()
    n = len(s)
    if(n<1):
        print(s)
    start = 0
    end =0
    for i in range(n):
        lengths1 = calculate(n,i,i)
        lengths2 = calculate(n,i,i+1)
        len = max(lengths1,lengths2)
        if len > end - start:
            start = i - (len-1)/2
            end = i + len/2
    print(s.strtime(start,end-start+1))


