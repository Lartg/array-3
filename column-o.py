'''
input:
    Area = arrayElement*difBetweenIndex
    
Brute force:
    nest for loops check every area

largestArea = 0
counter = 0
for wall in height:
    take index of height to check width
    for wall 2 in height
        where its not the same index
            find the area
            check against largest area
                reassign if biggere
return largestArea
        compare against our counter
        
2 pointer solutions:
    leftPointer = 0
    rightPointer = length of the list -1
    
    
    while pointers are not at same index
        check the areas of every new rectangle against the largest found
        move the left pointer if smaller than right pointer, vice versa
    
    return the largest area when pointers meet
        
'''
class Solution:
    def maxArea(self, height):
        largestArea = 0
        leftPointer = 0
        rightPointer = len(height)-1
        while leftPointer != rightPointer:
            # get width
            width = rightPointer - leftPointer
            # get height
            wallHeight = height[leftPointer]
            if height[leftPointer] < height[rightPointer]:
                wallHeight = height[leftPointer]
            else:
                wallHeight = height[rightPointer]
            # calc area
            area = width*wallHeight
            # check area
            if largestArea < area:
                largestArea = area
            # change pointer
            if height[leftPointer] > height[rightPointer]:
                rightPointer -= 1
            else: 
                leftPointer += 1
        return largestArea