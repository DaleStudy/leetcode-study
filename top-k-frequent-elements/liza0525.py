from collections import defaultdict

# 7기 풀이
# 시간 복잡도: O(n log n)
# - sorting 로직으로 인해 n log n만큼(n: nums의 길이)의 시간 소요
# 공간 복잡도: O(n)
# - nums 내에 distinct 요소의 개수만큼 count_map으로 공간 소요
# - 최대 값: distinct요소 개수가 nums의 길이 값(n)과 동일할 때
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_map = defaultdict(int)

        # 각 요소(num)의 개수를 저장
        for num in nums:
            count_map[num] += 1

        # count 기준으로 내림차순 정렬한 수 k만큼 list를 잘라준다.
        return [
            num for num, _ in sorted(
                [(num, count) for num, count in count_map.items()],
                key=lambda x: -x[1]
            )
        ][:k]
