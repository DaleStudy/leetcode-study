class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict_map = {}
        for a in nums:
            if a in dict_map:
                dict_map[a] += 1
            else:
                dict_map[a] = 1
        lst = sorted(dict_map.items(), key=lambda x: x[1], reverse=True)  # 공백 수정
        return [item[0] for item in lst[0:k]]