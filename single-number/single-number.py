class Solution:
    def singleNumber(self, arr: List[int]) -> int:
        num = 0
        for i in arr:
            num ^= i
        return num
        