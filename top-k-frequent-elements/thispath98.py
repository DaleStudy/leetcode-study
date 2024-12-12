"""
# Time Complexity: O(N log N)
- Counter 생성: N번 순회
- most common 연산: N log N
# Space Compelexity: O(N)
- 최악의 경우 (중복된 값이 없을 경우) N개 저장
"""
from collections import Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_dict = Counter(nums)
        top_k_list = count_dict.most_common(k)
        answer = [key for key, value in top_k_list]
        return answer
