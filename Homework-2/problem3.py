def findMinInitial(A):
  n = 0
  return findMin(A, n)

def findMin(A, n):
  if (A[n] < A[n+1]):
    return A[n]
  else:
    return findMin(A, n+1)

def main():

  A = [7, 6, 4, -1, -2, -9, -5, -3, 10, 13]

  print(findMinInitial(A))
