class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        # Edge case
        if not nums:
            return 0

        # 1. HashSet
        table = set(nums)

        logest_seq = 0

        # 2. 연속 시퀀스의 시작점 탐색
        for num in table:
            if (num - 1) not in table:  # !!
                current_num = num
                seq = 1

                # 시퀀스 확장
                while (current_num + 1) in table:
                    current_num += 1
                    seq += 1

            # 시퀀스 길이 업데이트
            logest_seq = max(logest_seq, seq)

        return logest_seq


"""
Time complexity : O(N)
- step 1 (iteration) : O(N)
  - 모든 숫자를 해시셋(set)에 저장
  - 해시셋 사용 이유 : 중복을 제거하고 O(1) 탐색 가능
    - 요소의 추가, 삭제, 존재 여부 확인에 평균적으로 O(1) 시간이 걸리는 자료구조
    - 이 성질 덕분에 하단의 풀이가 간단해질 수 있음
- step 2 (iteration) : O(N)
  - 각 요소는 for, while 에서 최대 두번 처리됨

Space Complexity)
- 해시셋(딕셔너리): O(N) (최악의 경우, 모든 숫자가 고유할 때)
"""


""" 첫번째 풀이 
- 시간복잡도 고려 X. O(NlogN)
- Edge case 대응 필요
- 연속된 요소 시퀀스가 하나가 아닐 경우 고려 필요

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        nums.sort()  # 오름차순

        cnt = 1
        tmp = nums[0]

        for i in range(1, len(nums)):
            if nums[i] == tmp + 1:
                cnt += 1
                tmp = nums[i]

        return cnt
"""
