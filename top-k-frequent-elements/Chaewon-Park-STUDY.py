from collections import defaultdict #defaultdict 사용 위함

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        # 전체 시간 복잡도: O(n log n), 공간 복잡도: O(n)
        output=[]
        frequent=defaultdict(int) # 없는 key에 접근할시  0 생성 (리뷰 반영! )

        # count로 하면 전체를 다 훑기 때문에 O(n^2)
        # dic 사용하여 공간 복잡도: O(n)
        for elem in nums:
            frequent[elem] +=1 # get 대신 
        #정렬 시 시간복잡도 최대 O(nlogn)
        result = dict(sorted(frequent.items(), key=lambda x: x[1], reverse=True)) #내림차순 정렬
        
        #빈도가 높은 원소 k개 추출: O(k)
        for key in result:
            output.append(key)
            if len(output)==k:
                return output
        return output
        
