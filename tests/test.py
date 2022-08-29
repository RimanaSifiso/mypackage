from mypackage import myModule

def test_top_n():

  ''' 
  unit test for top_n function
  '''

  assert myModule.top_n([2,4,5,6,0], 2) == [6,5], 'incorrect'
  assert myModule.top_n([1,0,8,9], 3) == [9,8,1], 'incorrect'
  assert myModule.top_n([23,12,34,21], 2) == [34,23], 'incorrect'
  assert myModule.top_n([16,12,56,34,23,57,21], 4) == [57,56,34,23], 'incorrect'