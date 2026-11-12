class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        # 전체 시간 복잡도: O(n log n), 공간 복잡도: O(n)
        output=[]
        frequent={}

        # count로 하면 전체를 다 훑기 때문에 O(n^2)
        # dic 사용하여 공간 복잡도: O(n)
        for elem in nums:
            frequent[elem] = frequent.get(elem, 0) + 1 # dic에 기존 key가 없다면 value 1 저장
        #정렬 시 시간복잡도 최대 O(nlogn)
        result = dict(sorted(frequent.items(), key=lambda x: x[1], reverse=True)) #내림차순 정
        
        #빈도가 높은 원소 k개 추출: O(k)
        for key in result:
            output.append(key)
            if len(output)==k:
                break
        return output
        
