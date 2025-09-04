import sys
input = sys.stdin.read
def main():
    data=input().split()
    index=0
    n=int(data[index])
    index+=1
    vec=[]

    for i in range (index,index+n):
        vec.append(int(data[i]))
    p=[0]*n

    p[0]=vec[0]
    
    for i in range(1,n):
        p[i]=p[i-1]+vec[i]
    
    results=[]
    index=n+1

    while index<len(data):
        a=int(data[index])
        b=int(data[index+1])
        index+=2
        
        if a==0:
            result=p[b]
        else:
            result=p[b]-p[a-1]
        results.append(result)

    for i in results:
        print(i)

if __name__=="__main__":
    main()
# 文章讲解：https://www.programmercarl.com/kamacoder/0058.%E5%8C%BA%E9%97%B4%E5%92%8C.html
