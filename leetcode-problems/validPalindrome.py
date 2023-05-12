'''

In: string
Out: bool


check if string is a palindrome - spelled same way forwards and back

psuedocode:
normalize string
reverse order of string
check reverse order against original
return bool

or

check each letter against its counterpart to save time with a while loop.

'''
from string import punctuation
class Solution():
  def isPalindrome(self, string: str) -> bool:
    # stole that for edge cases, screw parsing text
    string = list(string.lower().replace(' ', '').translate(str.maketrans('', '', punctuation)))
    leftPointer = 0
    rightPointer = len(string) - 1

    while leftPointer < rightPointer:
      if string[leftPointer] != string[rightPointer]:
        return False
      leftPointer += 1
      rightPointer -= 1
    return True
    

solution = Solution()
print(solution.isPalindrome('race, car'))