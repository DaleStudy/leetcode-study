class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        """
        Intuition:
            주어진 리스트의 개수를 얻어 범위를 구한다.
            이후 세트를 이용해서 범위 내의 정수가
            세트 안에 없으면 그 수를 리턴한다.

        Time Complexity:
            O(N):
                세트(해시)는 접근하는 데에 상수의 시간이 걸리므로
                최대 N + 1번의 접근을 하므로
                O(N)의 시간복잡도가 소요된다.

        Space Complexity:
            O(N):
                리스트를 해시로 변환하여 저장하고 있으므로
                O(N)의 공간복잡도가 소요된다.
        """
        num_set = set(nums)
        for i in range(len(nums) + 1):
            if i not in num_set:
                return i
