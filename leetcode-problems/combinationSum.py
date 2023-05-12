''' 
Given an array of distinct integers candidates and a target integer target, 
return a list of all unique combinations of candidates where the chosen numbers sum to target.
You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. 
Two combinations are unique if the frequency of at least one of the chosen 
numbers is different.

It is guaranteed that the number of unique combinations that sum up to target is less than 
150 combinations for the given input.

 

Example 1:

Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.
Example 2:

Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]
Example 3:

Input: candidates = [2], target = 1
Output: []
 

Constraints:

1 <= candidates.length <= 30
1 <= candidates[i] <= 200
All elements of candidates are distinct.
1 <= target <= 500

'''

'''

In: list of ints, target value
Out: list of lists of all possible combinations of ints taht sum to target

Solutions:
([1,2,3], (7))

while loop through list in reverse as the list is sorted.
  remove nums > target
  break once hit a num <= target

combinations = []  
total = target  //7
combination = [] // [3, 3, 1]

for num in list.reverse:  
  if num <= total
    while num <= total: //3
      total -= num //1
      combination.append(num)
    if total == 0:
      combinations.append(combination)
      total = target
      combination = [] 

// break down the largest combination
// get better at pseudocode and using diagrams
// learn recursion

'''

class Solution:
    def combinationSum(self, candidates: list, target: int) -> list:

        results = []

        def backtrack(remain, comb, start):
            if remain == 0:
                # make a deep copy of the current combination
                results.append(list(comb))
                return
            elif remain < 0:
                # exceed the scope, stop exploration.
                return

            for i in range(start, len(candidates)):
                # add the number into the combination
                comb.append(candidates[i])
                # give the current number another chance, rather than moving on
                backtrack(remain - candidates[i], comb, i)
                # backtrack, remove the number from the combination
                comb.pop()

        backtrack(target, [], 0)

        return results



solution = Solution()