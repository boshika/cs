'''Implement Central Tendency, Five number summary, Variance and STD
'''
class CentralTendency:
  """
  A class to represent Central Tendency for collections

  ...

  Attributes
  ----------
  lst: list
     collection of numbers

  Methods
  -------
  mean()
     calculates and return the mean for a collection
  median()
     calculates the median for a collection
  mode()
     calculates the mode of a collection
  """

  def __init__(self, lst):
    self.lst = lst
    if len(self.lst) == 0:
      raise ValueError (f'List cannot be empty')
  
  def mean(self):
    return sum(self.lst)/len(self.lst)
  
  def median(self):
    lst_length = len(self.lst) 
    middle_index = lst_length//2

    if lst_length%2==0:
      return (self.lst[middle_index] + self.lst[middle_index-1])/2
    else:
      return self.lst[middle_index]
  
  def mode(self):
    dict = {}

    for idx, value in enumerate(self.lst):
      if value in dict:
        dict[value] += 1
      else:
        dict[value] = 1
    
    max_freq = max(list(dict.values()))

    mode = [key for key, value in dict.items() if value == max_freq]
        
    return mode
