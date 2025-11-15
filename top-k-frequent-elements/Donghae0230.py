# 시간 복잡도
# 입력 list를 정렬해서 사용 -> 최대 O(n log n)
# 공간 복잡도
# 입력 list를 set으로 변환 -> 최대 O(n)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums.sort()
        items = {}
        n = nums[0]
        cnt = 1
        if len(nums) > 1:
            for i in range(1, len(nums)):
                if n != nums[i]:
                    items[n] = cnt
                    n = nums[i]
                    cnt = 1
                else:
                    cnt += 1
            items[n] = cnt
        else:
            items[n] = 1
        sorted_items_desc = sorted(items.items(), key=lambda item: item[1], reverse=True)
        result = []
        for i in sorted_items_desc[:k]:
            result.append(i[0])
        return result
