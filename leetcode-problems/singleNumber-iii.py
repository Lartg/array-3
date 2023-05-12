'''
given: array with doubled numbers and two single
output: the two singles

steps:
append the nums to a list instead of returning them,
return list at end of fxn

'''


class Solution():
  def singleNumber(self, nums) -> int:
    nums = sorted(nums)
    output = []
    step = 0
    for index in range(0, len(nums)-1, 2):
      index = index + step
      pointer = index + 1
      if nums[index] != nums[pointer]:
        output.append(nums[index])
        step = -1
      if len(output) == 2:
        return output
    if len(output) < 2:
      output.append(nums[-1])
    return output