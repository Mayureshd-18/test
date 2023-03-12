class Solution:
    def maxScore(self, nums: List[int]) -> int:
        nums.sort(reverse = True)
        match =0
        prefixSum =0
        for i in range(len(nums)):
            prefixSum += nums[i]
            if(prefixSum > 0):
                match+=1

        return match;

        