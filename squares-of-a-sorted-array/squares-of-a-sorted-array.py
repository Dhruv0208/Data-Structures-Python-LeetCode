class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        nums.sort()
        squared = list(map(lambda n:n**2, nums))
        squared.sort()
        return squared
            
        