
# coding: utf-8

# In[8]:

def selsort(A):
    n = len(A)
    for i in range(0,n) :
        k=i
        for j in range(i+1,n):
            if (A[j] < A[i]) & (A[j] < A[k]):
                k = j
        temp = A[i]
        A[i] = A[k]
        A[k] = temp
    return A


# In[9]:

Arr = [11,5,6,23,15,7,1,9,10]
A = selsort(Arr)
print(A)


# In[ ]:



