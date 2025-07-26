class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_dict = {}
        result = []
        temp_list = []

        # 딕셔너리 생성
        for data in nums:
            if data not in my_dict.keys():
                my_dict[data] = 0
            my_dict[data] = my_dict[data] + 1 
        
        # 딕셔너리를 리스트로 변환
        for data in my_dict.keys():
            temp_list.append([data, my_dict[data]])

        # 빈도수를 기준으로 정렬
        temp_list.sort(key=lambda a: a[1],reverse=True)

        # 상위 k개 요소 추출
        for i in range(k):
            result.append(temp_list[i][0])
        
        return result
        