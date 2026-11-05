class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numbers = {}
        for num in nums:
            numbers[num] = numbers.get(num, 0) + 1

        arr = []
        for num, cnt, in numbers.items():
            arr.append([cnt, num])
        arr.sort()

        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        return res
        
            