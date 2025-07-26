from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # dict_num = {num: ocurrence_num,,,,,}
        
        # 1. Build the dict
        dict_num = defaultdict(int)
        for num in nums:
            dict_num[num] += 1

        # 2. Resequence in the descending order w.r.t the num of ocurrence using lambda function
        dict_num_desc = dict(sorted(dict_num.items(), key=lambda x: x[1], reverse=True))

        # 3. Extract top k frequent nums,,
        top_k = [num for i, (num, ocurrence) in enumerate(dict_num_desc.items()) if i < k]

        return top_k
