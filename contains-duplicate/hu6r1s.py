from collections import Counter

class Solution:
    # 시간복잡도: O(n) - Counter(nums)는 n번 순회하며 각 원소의 개수를 세고, cnt.items()는 최대 n개의 (key, value) 쌍을 포함하므로 최대 n번 순회
    # 공간복잡도: O(n) - Counter는 입력 배열에 있는 각 고유 원소를 키로 저장하므로 최악의 경우 n개의 키를 저장함
    def containsDuplicate(self, nums: List[int]) -> bool:
        cnt = Counter(nums)
        for _, v in cnt.items():
            if v >= 2:
                return True
        else:
            return False
        