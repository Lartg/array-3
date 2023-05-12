'''
Given: 
  A set of roman numerals
Output: 
  The numerical value






Psuodocode:
  Create a dict of roman numeral values
  
  total = 0
  while 
    if not last char in string check for subtractive pair:
      add the value of pair to the total
      traverse string by two chars
    else: 
      add the value to total traverse by one char
    if last char in list:
      endwhile
  print(total)


'''



values = {
  "I": 1,
  "V": 5,
  "X": 10,
  "L": 50,
  "C": 100,
  "D": 500,
  "M": 1000,
  "IV": 4,
  "IX": 9,
  "XL": 40, 
  "XC": 90,
  "CD": 400,
  "CM": 900
}


class Solution:
  def romanToInt(self, s: str) -> int:
    total = 0
    index = 0
    while index < len(s):
      # This is the subtractive case.
      if index < len(s) - 1 and s[index:index+2] in values:
        total += values[s[index:index+2]] 
        print(s[index:index+2])
        index += 2
              
      else:
        total += values[s[index]]
        print(values[s[index]])
        index += 1
      #add error catch
    return total
solution = Solution()

print(solution.romanToInt('CMX'))