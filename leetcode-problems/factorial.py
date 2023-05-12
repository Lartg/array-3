'''
Given and integer find its factorial. 

in: integer
out: integer

Steps: continually multiply a number by itself minus 1 until zero is hit

implement:
while loop or recursion not sure which is better
'''
def factorial_while(num):
  # can say answer = 1 because 0! == 1
  answer = 1
  while num >=1:
    answer = answer * num
    num -= 1
  return answer

def factorial_recursion(num, answer=1):    
  answer = answer * num

  if num > 1:
    num -= 1
    factorial_recursion(num, answer)

  return answer
