from collections import Counter
class Sol:
    def longest_harmounious_subsequence(self,nums):
        max_subarr=0
        freq=Counter(nums)
        for num,count in freq.items():
            if num+1 in freq:
                max_subarr=max(max_subarr,count+freq[num+1])
