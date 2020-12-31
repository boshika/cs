class SetTheory:
  '''
  This class encapsulates the fundamental methods in set theory and probability

  ...
  Attributes
  ----------
      unpack_args: tuple of *args 
           
  Methods
  -------
      union():
      returns union of sets
          
  '''
  
  def __init__(self, *args):
    self.unpack_args = args
  
  def __str__(self):
    return f' {self.unpack_args}'

  def union(self):
    return set().union(*self.unpack_args)
      
A={'HHH','HHT','HTH','THH'}
B={'HHH','HHT','THT','THH'}

set_theory = SetTheory(A,B)
print(set_theory)
print(set_theory.union())
