class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        """
        nums의 각 원소에 대해서, 그 원소를 제외한 나머지 원소들의 곱을 구하는 함수
        시간제약은 O(n)이고, 나눗셈을 사용하지 않아야 함

        방법:
        1. brute-force. 각 원소마다, 나머지 원소들의 곱을 구하기. O(n)의 시간 제약을 만족하지 못함
        2. 전체 곱을 구해두고, 각 원소마다 자기 자신의 값으로 나누기. 나눗셈 제약에 걸려 사용 불가
        3. 루프에서 자신의 원소를 빼고 앞의 값들의 곱과 뒤의 곱들의 값을 구하기.
            - 앞에서부터 곱을 구해나가면서, 배열에 저장하기. 초기 값은 1로 설정
            - 뒤에서부터 곱을 구해나가면서, 배열에 저장하기. 초기 값은 1로 설정
            - 현 위치 기준 앞의 곱과 뒤의 곱을 곱해서 최종 답을 구하기
            -> 앞의 곱과 뒤의 곱의 목록을 유지하니 공간 복잡도가 O(n), 더 효율화 할 수 없을까?
        4. 별도의 배열을 만들지 않고, 앞에서부터 곱하며 배열에 저장한 후, 뒤에서부터 다시 곱하며 동일 배열에 업데이트.
            -> 시간복잡도 O(n), 공간복잡도 O(1) (답 배열 제외)

        Args:
            nums (list[int]): 정수 목록

        Returns:
            list[int]: 각 원소에 대해서, 그 원소를 제외한 나머지 원소들의 곱을 담은 목록
        """
        answer = [1] * len(nums)
        nxt = 1
        for idx, num in enumerate(nums):
            answer[idx] = nxt
            nxt *= num
        nxt = 1
        for idx in range(len(nums) - 1, -1, -1):
            answer[idx] *= nxt
            nxt *= nums[idx]
        return answer
