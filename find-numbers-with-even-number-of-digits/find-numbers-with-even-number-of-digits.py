class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        total = 0
        for i in range(0, len(nums)):
            count = 0
            while nums[i] != 0:
                nums[i] //= 10
                count += 1
            if count%2 == 0:
                total += 1
            else:
                continue
        return total