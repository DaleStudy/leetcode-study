# idea
# 1. 빈도수를 dict 에 저장한다.
# 2. 빈도수 내림차순으로 정렬한다.
# 3. 2에서 정렬한 entry 중 1번째, 2번째, ... k 번째 key 값을 모아서 List 로 반환한다.
# time : O(nlogn)
# space : O(n)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_dict = {}

        for num in nums:
            if num in count_dict:
                count_dict[num] = count_dict[num] + 1
            else:
                count_dict[num] = 1
        
        tuple_list = []

        for (count_key, count_value) in count_dict.items():
            tuple_list.append((count_key, count_value))
        
        sorted_tuple_list = sorted(tuple_list, key=lambda x: x[1], reverse=True)
        answer = []
    
        for i in range(k):
            answer.append(sorted_tuple_list[i][0])

        return answer
        

        
