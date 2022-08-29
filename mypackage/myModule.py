def top_n(items, n):
  '''Return the top n items in an array (list), in desc order
  
  Args:
    array: top n items, in desc order

  Egs:
    >>> top_n([3,5,2,6,5], 2)
    [5,5]
  '''

  for i in range(n):
    for j in range(len((items) - 1 -i)):
      if items[j] > items[j+i]:
        items[j], items[j+1] = items[j+1], items[j]
      
  top_n = items[-n:]

  return top_n[::-1] # return in desc order