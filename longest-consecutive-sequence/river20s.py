class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        >> nums에서 연속된 수열 중 가장 긴 수열의 길이를 반환합니다.
        (전체 풀이 과정은 다음 링크를 참고하시면 됩니다: https://blog.naver.com/kanosekai/223823200575)
        - Time Complexity: O(n)
          nums를 set으로 변환하는 데 O(n) 시간이 소요됩니다.
        - Space Complexity: O(n)
          모든 원소가 고유한 경우 전부 set에 저장하므로 
          O(n)의 공간을 추가로 사용할 수 있습니다.
        """
        num_set = set(nums)
        longest = 0
        
        for num in num_set:
            # num이 연속 구간의 시작점인지 판단
            if num - 1 not in num_set:
                current = num
                current_streak = 1

                # 현재 숫자에서 연속된 값들이 set에 있는지 확인하며 수열 확장
                while current + 1 in num_set:
                    current += 1
                    current_streak += 1
                
                # 가장 긴 수열의 길이를 반환
                longest = max(longest, current_streak)

        return longest
