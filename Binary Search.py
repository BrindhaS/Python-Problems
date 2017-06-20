
def func search(A, key):
	n = len(A)
	low = A[1]
	high = A[n-1]
	while low < high:
		mid = (low + high)/2
		if mid > key:
			high = mid
		elif mid <key:
			low = mid
		elif mid == key:
			return true
		else:
			return false


A = [3, 5, 7, 9, 11, 16]
if search(A,4):
	print('Found')
else:
	print('Not found')
