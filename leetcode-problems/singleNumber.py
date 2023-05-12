'''
given: non empty array of ints, every element appers twice except one

output: the non repeated number

pseudocode:
sort list, check by index
'''
class Solution():
  def singleNumber(self, nums) -> int:
    nums = sorted(nums)
    for index in range(0, len(nums)-1, 2):
      pointer = index + 1
      if nums[index] != nums[pointer]:
        return nums[index]
    return nums[-1]

solution = Solution()
print(solution.singleNumber([2,1,2,1,6,5,4,5,4]))