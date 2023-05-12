'''

Given: array of ints
Output: third maximum number
Challenge: in O(n) time, python sort is nlog(n)

Plan is to find the maximum in O(n) then add 2nd and third highest number.

'''

def thirdMaxNum(array):
  firstMax = array[0]
  secondMax = None
  thirdMax = None

  for index in range(1, len(array)):
    if firstMax < array[index]:
      thirdMax = secondMax
      secondMax = firstMax
      firstMax = array[index]
      continue
    if secondMax < array[index]:
      thirdMax = secondMax
      secondMax = array[index]
      continue
    if thirdMax < array[index]:
      thirdMax = array[index]
  
  return thirdMax

if __name__ == "__main__":
  print(thirdMaxNum([1,2,3,4,5]))

