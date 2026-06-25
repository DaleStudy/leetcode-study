# 2차 풀이
class Solution2:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = [[] for _ in range(len(nums) + 1)]

        count = Counter(nums)
        for num, freq in count.items():
            bucket[freq].append(num)

        result = []
        for freq in range(len(bucket) -1, -1, -1):
            for num in bucket[freq]:
                result.append(num)

                if len(result) == k:
                    return result

# 1차 풀이
class Solution1:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = sorted(Counter(nums).items(), key=lambda n: n[1], reverse=True)
        
        answer = []
        for v, freq in c:
            answer.append(v)

            if len(answer) == k:
                break
            
        return answer
