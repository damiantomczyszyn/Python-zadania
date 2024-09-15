def solution(A, B, F):
    sum=0
    indeks=0
    N=len(A)
    NF=N-F
   # print (N)
   # print(NF)
    #find maximum until one team isn't full
    for x in range (N):
        #print(x)
        if(max(A)>=max(B) and F!=0):
            sum+=max(A)
            #print(A.index(max(A)))
            indeks=A.index(max(A))
            del B[indeks]
            del A[indeks]
            F-=1
        else:
            NF-=1
            
            #if NF==0:
                
            sum+=max(B)
            indeks=B.index(max(B))
            del B[indeks]
            del A[indeks]
            if NF==0:
                for x in range (len(B)):
                    B[x]=0
    return sum
            
    
print(solution([4, 2, 1], [2, 5, 3]  , 2))
