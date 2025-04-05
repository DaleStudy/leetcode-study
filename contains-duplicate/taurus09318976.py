#이 문제는 정수 배열이 주어졌을 대, 배열에 중복 값이 있으면 true, 모든 요소가 고유하면, false를 반환

class Solution:
    def containsDuplicate(self, nums: List[int]):
        #빈 집합 생성
        array = set()
        
        #배열의 각 요소를 순회하며, 현재 요소가 이미 집합에 있는지 확인.
        #있다면, 중복 값이 있으므로, True를 반환
        #없다면, 현재 요소를 집합에 추가 
        #Example 1의 경우 : 
        #1 -> 집합에 추가 / 2 -> 집합에 추가
        #3 -> 집합에 추가 / 1 -> 이미 집합에 있으므로 True 반환
        for i in range(len(nums)):
            if nums[i] in array:
                return True
            array.add(nums[i])

        #모든 요소를 검사한 후에도 중복이 발견되지 않았다면, False를 반환
        return False

        #이 코드는 시간 복잡도 O(n)과 공간 복잡도 O(n)으로 문제를 효율적으로 해결함