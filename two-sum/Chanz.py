class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        ## 공간 복잡도 : O(n)
        ## - n 개수 만큼의 hashmap 공간만을 사용하므로 공간복잡도가 O(n)이라고 생각합니다.

        ## 시간 복잡도 : O(n)
        ## - hashmap에 값과 idx를 매칭하는 작업을 n번 수행합니다.
        ## - 이후 다시 nums를 순회하면서 target이 되는 짝을 찾습니다.
        ## - 따라서 Worst N번 이므로, 2n = O(n)이라고 생각합니다.

        hashmap = dict()
        for idx, num in enumerate(nums):
            hashmap[num] = idx
        
        for idx, num in enumerate(nums):
            matched_num_idx = hashmap.get(target-num)
            if matched_num_idx and matched_num_idx != idx:
                return [idx, matched_num_idx]
        
