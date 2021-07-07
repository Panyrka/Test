import math

def Sort(A,p,r):
  if p < r:
    q = math.floor((p+r)/2)
    Sort(A,p,q)
    Sort(A,q+1,r)
    merge(A,p,q,r)

def merge(A, p, q, r):
  left_part_of_array=A[(p-1):q] # Берём левую часть массива от p-1 до q 
  right_part_of_array=A[(q):(r)] # Берём правую часть массива от q до r
  # Определяем индексы для левого и правого массива, и общий индекс
  index_of_left_array=0
  index_of_right_array=0
  general_index=p-1

  # Пока один из индексов не будет равен размеру, соответствующего ему массива, будет выполнятся следующий цикл
  while index_of_left_array<len(left_part_of_array) and index_of_right_array<len(right_part_of_array):
    if(left_part_of_array[index_of_left_array]<=right_part_of_array[index_of_right_array]):
      A[general_index]=left_part_of_array[index_of_left_array]
      index_of_left_array=index_of_left_array+1

    else:
      A[general_index]=right_part_of_array[index_of_right_array]
      index_of_right_array=index_of_right_array+1
    general_index=general_index+1

  #Обрабатываем левый или правый оставшийся индекс
  while index_of_left_array<len(left_part_of_array):
    A[general_index]=left_part_of_array[index_of_left_array]
    index_of_left_array=index_of_left_array+1
    general_index=general_index+1

  while index_of_right_array<len(right_part_of_array):
    A[general_index]=right_part_of_array[index_of_right_array]
    index_of_right_array=index_of_right_array+1
    general_index=general_index+1

A = [5,2,4,6,1,3,2,6]
Sort(A,1,len(A))
print(A)

B = [33, 42, 9, 37, 8, 47, 5, 29, 49, 31, 4, 48, 16, 22, 26]
Sort(B,1,len(B))
print(B)
