#Dado um array de números inteiros nums e um alvo inteiro, retorne os índices dos dois números de forma que a soma deles resulte no alvo.

#Example 1:
#Input: nums = [2,7,11,15], target = 9
#Output: [0,1]
#Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

def twoSum(self, nums, target):
        numMap = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in numMap:
                return [numMap[complement], i]
            numMap[num] = i
        return []