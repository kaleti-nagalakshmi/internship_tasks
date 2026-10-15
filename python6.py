#Find the Runner-Up Score!
#https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    l =sorted(list(arr),reverse=True)
    sec_lar = []
    for i in l :
        if i not in sec_lar :
            sec_lar.append(i) 
    print(sec_lar[1])
