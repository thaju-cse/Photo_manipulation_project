def spiral_matrix():
    arr=[]
    n=int(input())
    m=int(input())
    for i in range(n):
        arr.append(list(map(int,input().split())))
    out=[]
    while arr:
        out+=arr.pop(0)
        arr=(list(zip(*arr)))[::-1]
    return out
print(" ".join(map(str,spiral_matrix())))