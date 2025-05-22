#Dado um array de números inteiros nums e um alvo inteiro, retorne os índices dos dois números de forma que a soma deles resulte no alvo.
def twoSum(self, nums, target):
        numMap = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in numMap:
                return [numMap[complement], i]
            numMap[num] = i
        return []