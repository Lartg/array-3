# sort the array and take the largest elements

def solution(array, k):
  if k <= len(array) and k > 0:
    sortedArray = sorted(array)
    largestNumbers = []
    for i in range ((k*-1), 0):
      largestNumbers.append(sortedArray[i])
    return largestNumbers
  else:
    return ('Input error')

if __name__ == '__main__':
  array = [4,5,3,7,1,9]
  k = 20
  print(solution(array,k))