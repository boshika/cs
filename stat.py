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
  
  class FiveNumberSummary(CentralTendency):
  """
  A class to represent Five Number Summary for collections

  ...

  Attributes
  ----------
  lst: list
     collection of numbers

  Methods
  -------
  min()
    returns the smallest value in the collection
  median()
     CentralTendency.median()
  quartile_1_3():
     calculates the median for Quartile 1 and Quartile 3 of collection
  max():
      returns the largest value in the collection
  __calculate_quartile(list):
     private method, calculates median for quartiles
  """
  
  def __init__(self, lst):
    CentralTendency.__init__(self, lst)
    self.lst = lst
  
  def min(self):
    smallest_value = min(self.lst)
    print(f'Minimum:\t{smallest_value}')

  def quartile_1_3(self):
    middle_element = len(self.lst)//2
    first_half = self.lst[:middle_element]
    second_half = self.lst[middle_element+1:]

    q1 = self.__calculate_quartile(first_half)
    q3 = self.__calculate_quartile(second_half)
    
    print(f'Quartile 1:\t{q1}\tQuartile 3:\t{q3}')
  
  def __calculate_quartile(self, sublst):
    lst_length = len(sublst) 
    middle_index = lst_length//2

    if lst_length%2==0:
      median =  (sublst[middle_index] + sublst[middle_index-1])/2
      return median
    else:
      median = sublst[middle_index]
      return median

  def max(self):
    largest_value = max(self.lst)
    print(f'Maximum:\t{largest_value}')
  

