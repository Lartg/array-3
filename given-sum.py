'''
loop through the array and store complements
while in the loop, compare against my compliments
n^2

pointer solution, works if sorted
n*ln(n)
'''
# inputs: unsorted array, target number
def solution(array, target):
  sortedArray = sorted(array)
  leftPointer = 0
  rightPointer = len(array) - 1

  '''
  if the dart is above target move rightPointer
  if below move the left pointer
  '''

  dart = None
  while leftPointer <= rightPointer:
    dart = sortedArray[leftPointer] + sortedArray[rightPointer]
    if dart < target:
      leftPointer += 1
    elif dart > target:
      rightPointer -= 1
    elif dart == target:
      return (sortedArray[leftPointer], sortedArray[rightPointer])
  return ('Pair not found')

if __name__ == '__main__':
  array = [3,4,5,67,7,5,1]
  target = 10
  print(solution(array, target))

# diction could be cleaner, less ramble more intentional speech