'''
Given: two arrays of integers
Output: return an array of unique shared numbers

Brute force: nest for loops 

could shave off time for large sets by sorting list. Would have to do hard math to figure out when that would be efficient.
'''

def intersectOfTwoArrays(array1, array2):
  intersection = []
  for num1 in array1:
    for num2 in array2:
      if num1 == num2:
        if num1 not in intersection:
          intersection.append(num1)
  return intersection

if __name__ == "__main__":
  print(intersectOfTwoArrays([1,2,2,2,2,3,4,5], [2,3,3,5]))