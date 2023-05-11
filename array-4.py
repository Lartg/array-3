'''
brute force n^2

hash the first array, loop through the second array and check the hash map.
n

sorted pointer solution
'''

def Solution(array1, array2, target):
  hash = {}
  for num in array1:
    key = target - num
    hash[key] = num
  for num in array2:
    if hash.get(num) != None:
      return (hash[num], num)
  return None

if __name__ == "__main__":
  array1 = (1,2,4,5)
  array2 = (1,2,4,5)
  target = 10
  print(Solution(array1, array2, target))