'''
Task: from scratch create an exponent calculator
Constraint: the power will be an integer

I should not use recursion here, as there are 3 ways the problem can go. While loops will be much easier to conceptualize, and will only need to make checks once.
'''

def pow(x, n):
  answer = 1
  while n < 0:
    answer = answer * (1/x)
    n += 1
  while n > 0:
    answer = answer * x
    n -= 1
  return answer
    
if __name__ == "__main__":
  print(pow(2, -2), pow(2, 0), pow(2,1), pow(2,3))