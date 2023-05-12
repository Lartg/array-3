'''
Given: reverse sorted array of ints with duplicate numbers
Task: remove nums in place
Out: Number of unique elements in the array

two pointer solution: 
while right pointer less than length of list
put two pointers together and traverse the list and pop
'''

def removeDuplicates(array):
  duplicates = 0
  leftPointer = 0
  rightPointer = 1

  while rightPointer < len(array):
    if array[leftPointer] == array[rightPointer]:
      array.pop(rightPointer)
      duplicates += 1
    else:
      leftPointer += 1
      rightPointer += 1
  
  return (duplicates, array)

if __name__ == "__main__":
  print(removeDuplicates([5,5,4,3,2,2,1,1,1]))