
# coding: utf-8

# In[6]:

def InsSort(A):
    n = len(A)
    for i in range(1,n):
        key = A[i]
        j = i-1
        while (j > -1) & (A[j]>key):
            A[j+1] = A[j]
            j = j-1
        A[j+1] = key
    return A


# In[7]:

Arr = [7,5,3,10,7,4]
A = InsSort(Arr)
print(A)


# In[ ]:



