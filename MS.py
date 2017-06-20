
def MergeSort(A,p,r):
    q = (p+r)/2
    if p<r:
        MergeSort(A,p,q)
        MergeSort(A,q+1,r)
    n1 = q-p+1
    n2 = r-q
    B = []*(r-p+1)
    L = A[:q]
    R = A[q:]
    i = 0
    j = 0
    k = 0
    while(i<=n1) & (j<=n2):
        if(L[i] < R[j]):
            B[k] = L[i]
            i = i+1
        else:
            B[k] = R[j]
            j = j+1
        k = k+1
    if(i<=n1):
        B[k:] = L[i:n1+1]
    if(j<=n2):
        B[k:] = R[i:n2+1]
    return A

Arr = [3,5,1,2,9,3,5,1]
A = MergeSort(Arr, 0, len(Arr)-1)
print(A)
