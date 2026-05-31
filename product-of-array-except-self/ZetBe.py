'''
문제: 해당 인덱스를 제외한 나머지 인덱스의 곱을 구하라
풀이: 0의 개수에 따라 경우를 나눠서 풀이
    1. 0이 2개 이상인 경우: 모든 인덱스의 곱이 0이므로, [0, 0, ..., 0] 반환
    2. 0이 1개인 경우: 0이 있는 인덱스에는 나머지 인덱스의 곱을, 나머지 인덱스에는 0을 반환
    3. 0이 없는 경우: 전체 곱을 각 인덱스의 값으로 나누어 반환
시간복잡도: O(n)
    nums 배열을 한 번씩 순회하며 곱을 계산하고, 다시 한 번씩 순회하며 결과를 계산하므로 전체 시간복잡도는 O(n)이다.
공간복잡도: O(n)
    같은 크기의 결과 배열을 반환하므로 전체 공간복잡도는 O(n)이다.
사용한 자료구조: 딕셔너리, 리스트
'''

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        d = {}
        now = 1
        answer = []
        for i in nums:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
            if i != 0:
                now *= i
                
        if 0 in d and d[0] > 1:
            return [0 for i in range(len(nums))]
        
        if 0 in d and d[0] == 1:
            for i in nums:
                if i == 0:
                    answer.append(now)
                else:
                    answer.append(0)
            return answer
        
        for i in nums:
            answer.append(now//i)
        return answer

