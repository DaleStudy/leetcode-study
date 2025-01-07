class Solution(object):
    # 시간복잡도 nlog(n) sort
    # 공간복잡도 n 정렬시
    def missingNumber_1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sort_nums = sorted(nums)

        v = 0
        for i in sort_nums:
            if v != i:
                return v
            else:
                v += 1

        return v

    # hash를 사용
    # 모든 숫자를 dict에 입력
    # for문을 돌면서 해당 hash가 dict에 존재하는지 체크
    # 시간복잡도 n - for문
    # 공간복잡도 n - dict 생성
    def missingNumber(self, nums):
        hash_keys = dict()
        for i in range(len(nums) + 1):
            hash_keys[i] = 0
        for i in nums:
            hash_keys[i] = 1

        for i in range(len(nums) + 1):
            if hash_keys[i] != 1:
                return i

        return 0


