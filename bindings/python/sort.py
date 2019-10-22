# Selection sort implimentation in python
import sys 
A = [12, 14, 9, 7] 

for i in range(len(A)): 
	min_idx = i 
	for j in range(i+1, len(A)): 
		if A[min_idx] > A[j]: 
			min_idx = j 
      
	A[i], A[min_idx] = A[min_idx], A[i] 

# Main
print ("Array is sorted, given below") 
for i in range(len(A)): 
	print("%d" %A[i]), 
