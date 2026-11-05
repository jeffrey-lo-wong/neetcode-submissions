class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = {}         
        counter = 0
        longest = 0

        seen = set(nums)

        for i in seen:
            if i - 1 not in seen:      
                counter = 0
                while i in seen:
                    counter += 1
                    i += 1
                    if counter > longest:
                        longest = counter
 
        return longest
                    

