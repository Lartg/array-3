'''
change the step of my loop to 3 from 1

'''


class Solution():
  def singleNumber(self, nums) -> int:
    nums = sorted(nums)
    for index in range(0, len(nums)-1, 3):
      pointer = index + 1
      if nums[index] != nums[pointer]:
        return nums[index]
    return nums[-1]

solution = Solution()