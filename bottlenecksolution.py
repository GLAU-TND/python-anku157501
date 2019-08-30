n=int(input())
ar=list(map(int,input().split(" ")))

print(max([ar.count(i) for i in  ar]))
