class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = dict()

        result = []

        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        sorted_freq = dict(sorted(freq.items(), key=lambda item: item[1], reverse=True))

        # print(freq)
        # print(sorted_freq)

        for key in sorted_freq:
            if k == 0:
                break
            
            result.append(key)
            k -= 1

        return result