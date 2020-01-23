55. Jump Game

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        distance = 1000000
        first = True
        for n in reversed(nums):
            if n >= distance:
                distance = 1
                continue
            if first is True:
                distance = 1
                first = False
                continue
            distance = distance + 1    
        if distance == 1:
            return True
        else:
            return False
