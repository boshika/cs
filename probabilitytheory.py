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
    return set.union(*self.unpack_args)
  
  def intersection(self):
    return set.intersection(*self.unpack_args)
  
  def theorem_of_absorption(self):
    '''The theorem of absorption states that:
       A∪(A∩B)=A
       A subset which contains an intersection, and is in union with one of its supersets the intersection is "absorbed".
    '''

    intersection = set.intersection(*self.unpack_args)
    absorption_A = intersection.union(self.unpack_args[0])

    return absorption_A
 
# ----------------------------------------------
# Implementation 
# ----------------------------------------------
A={'HHH','HHT','HTH','THH'}
B={'HHH','HHT','THT','THH'}

set_theory = SetTheory(A,B)
print(set_theory)
print(set_theory.union())
print(set_theory.interesction())
print(set_theory.theorem_of_absorption())

def calculate_probability(n):
  '''Calulate probability student attends atleast one courtse'''

  stat = []
  computer_science = []
  data_science = []
  for i in range(1,n+1):
    if i%2==0:
      stat.append(i)
    if i%3==0:
      computer_science.append(i)
    if i>20:
      data_science.append(i)
      
  stat = set(stat)
  computer_science = set(computer_science)
  data_science = set(data_science)

  set_theory = SetTheory(stat, computer_science,data_science)
  atleast_one_course = set_theory.union()
  return atleast_one_course

print(calculate_probability(30))
