from collections import Counter

class Solution:
    """
        - TC
            - Counter(nums): O(n)
            - sorted(): O(n log n)
            - 슬라이싱 및 리스트 변환: O(k)
            - 전체: O(n log n)
        - SP
            - Counter 및 정렬된 딕셔너리 저장: O(n)
            - 반환 리스트: O(k)
            - 전체: O(n)
    """
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_nums = Counter(nums)
        count_nums = dict(sorted(count_nums.items(), reverse=True, key=lambda x: x[1])).keys()
        return list(count_nums)[:k]
