'''
문제: 배열에서 가장 긴 연속된 수열의 길이를 찾는 문제
풀이: 딕셔너리의 키값을 기준으로 정렬 후, 연속된 수열의 길이를 계산
     (중복된 값은 딕셔너리로 제거 후 처리)

시간복잡도: O(k log k + N) (k는 딕셔너리의 키 개수, N은 nums의 길이)
공간복잡도: O(N) (공간의 크기는 nums의 길이에 비례)

사용한 자료구조: 딕셔너리, 리스트
'''


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        d = {}
        answ = 1
        if len(nums) > 0:
            for i in nums:
                if i not in d:
                    d[i] = 0
            
            a = sorted(d.keys())
            now = a[0]
            an = 1
            for i in range(1, len(a)):
                t = a[i]
                if now+1 == t:
                    an += 1
                else:
                    an = 1
                now = a[i]
                answ = max(answ, an)
            
            return answ
        return 0
    
    