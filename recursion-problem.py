'''
Given a sorted array of strings, write a recursive function to find the index of the first and last occurrence of a target string. 
If the target string is not found in the array, report that.

Example input:  
instructors = [Adriana, Adriana, Alan, Alan, Alan, Alan, Alan, Braus, Braus, Braus, Braus, Dan, Dan, Dan, Dan, Dan, Dani, Dani, Jess, Meredith, Milad, Milad, Mitchell, Mitchell, Mitchell, Mitchell]

Example execution:  find_indexes(instructors, 'Braus')  ⇒  (7, 10)
'''

'''
must be solved using recursion.
have to look at the whole list.

will return a list as that is mutable. 

'''

def instance_search(array, target, index=0, found_indeces=[]):
  if array[index] == target:
    found_indeces.append(index)
  index += 1
  if index != len(array):
    return instance_search(array, target, index, found_indeces)
  return found_indeces

if __name__ == "__main__":
  array = ['a','a','b','c','a']
  target = 'a'
  print(instance_search(array, target))
  pass