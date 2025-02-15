"""
    ** 실수로 예전 과제 수행 때 다른 과제폴더에 파일을 만들어서 파일 수정합니다!!

    풀이 : 
        nums의 구성요소 num에 따라 각각 후보1, 후보2, 후보3 중에 
            가장 큰 값은 새로운 max_res, 가장 작은 값은 새로운 min_res

        후보1: 이전 max_res * 현재 num (num이 양수일 경우 가장 클 가능성)
        후보2: 이전 min_res * 현재 num (num이 음수일 경우 가장 클 가능성)
        후보3: 현재 num (num이 양수일 경우 가장 클 가능성)

        새로운 max_res와 max_total을 비교해서 업데이트

        
        메모 :
        - 현재 num이 0일 경우 후보 셋 모두 0
        - 음수 양수 0 등으로 조건을 나누지 않고 min과 max로만 구분해도 충분하다
        - max_res와 min_res는 곱해지므로 초기화를 1로 한다 (또는 반복문을 인덱스로 반복하고 1부터 시작)
    
        
    nums의 길이 : n

    TC : O(N)

    SC : O(1)
"""

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_total, max_res, min_res = nums[0], 1, 1
        for num in nums :
            min_res, max_res = min(num, max_res * num, min_res * num), \
                max(num, max_res * num, min_res * num)
            max_total = max(max_total, max_res)
        return max_total
