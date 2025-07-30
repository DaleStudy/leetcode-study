class Solution:
    # nums 에서 가장 빈도가 높은 k개의 요소를 찾는 문제
    # 딕셔너리와 정렬을 사용해 해결
    # 시간복잡도: O(n log n), 공간복잡도: O(n)
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = {}
        for num in nums:
            freq_map[num] = freq_map.get(num, 0) + 1

        sorted_nums = sorted(freq_map.items(), key=lambda x:x[1], reverse=True)
        return [num for num, _ in sorted_nums[:k]]

