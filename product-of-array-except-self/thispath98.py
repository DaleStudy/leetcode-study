class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Intuition:
            i번째 인덱스의 값을 계산하기 위해서는
            0 ~ i-1 까지의 값과 i+1 ~ N 까지의 값을 모두 곱해야 한다.
            이의 누적곱을 저장하여, 계산한다.

        Time Complexity:
            O(N):
                리스트를 1번 순회하며 답을 찾으므로,
                O(N)의 시간복잡도가 소요된다.

        Space Complexity:
            O(N):
                forward 배열과 backward 배열에 N개의 원소를 저장하므로
                O(N)의 공간복잡도가 소요된다.

        Key takeaway:
            스캔하여 값을 저장해두는 방식을 숙지하자.
        """
        for_val = 1
        back_val = 1
        forward = []
        backward = []
        for i in range(len(nums)):
            forward.append(for_val)
            backward.append(back_val)

            for_val *= nums[i]
            back_val *= nums[-(i + 1)]
        backward = backward[::-1]

        answer = [forward[i] * backward[i] for i in range(len(nums))]
        return answer
