'''

Given: a string
Return: the average letter at alphabet index

in: az
out: m

Create a tuple letters
for every letter in the string 
  total index (where I add the index of each letter in the string)
  count number letters (to find average index)
divide the total index by the number of letters
round down
find the letter at the average index 
return it

'''

letterBank = ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')

def AverageLetter(string):
  letters_count = 0
  index_count = 0
  for letter in string:
    letters_count += 1
    index_count += letterBank.index(letter)
  average_index = index_count/letters_count
  average_index = int(average_index)
  averageLetter = letterBank[average_index]
  return averageLetter

if __name__ == "__main__":
  print(AverageLetter('abcde'))
