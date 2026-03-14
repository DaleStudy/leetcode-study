class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        """
        nums에서 세 숫자를 골라 합이 0이 되는 조합을 구하는 함수
        세 숫자는 서로 다른 인덱스에 위치해야 함. 중복된 조합은 포함하지 않아야 함.

        방법
        1. brute force. 세 숫자를 모두 조합하여 합이 0이 되는지 확인. O(n^3) 시간복잡도 -> 너무 오래 걸림!
        2. 첫번째 값을 고정하고 나머지 두개의 합을 two sum 문제에서 해결한 것 처럼 dict에 저장하여 찾기. O(n^2) 시간복잡도, O(n) 공간복잡도
            -> 중복된 조합을 걸러내는 과정이 필요함
        3. 정렬을 해서, 첫번째 값을 고정하고, 나머지 두개의 합이 첫번째 값의 음수가 되는 경우를 찾음 - 포인터 방식.
            -> O(n^2) 시간복잡도, O(1) 공간복잡도. 2번 방법보다 정렬을 하지 않으니 효율적
        4. 3번 방법에 시간을 줄일 수 있는 예외 케이스 혹은 조건을 찾아 빠르게 종료하기
            - 첫번째 값이 양수인 경우, 나머지 두개의 합이 음수가 될 수 없으므로 종료
            - 첫번째 값이 이전 값과 같은 경우, 중복된 조합이 되니 건너뛰기
            - append 값을 찾은 후에 j+1, k-1을 하면서 중복된 값이 아닐때까지 이동하기

        Args:
            nums (list[int]): 정렬되지 않은 정수목록

        Returns:
            list[list[int]]: 합이 0이 되는 세 숫자의 조합 목록
        """
        answer = []
        s_nums = sorted(nums)
        n = len(s_nums)
        for i in range(n - 2):
            x = s_nums[i]
            if i > 0 and x == s_nums[i - 1]:
                continue
            if x > 0:
                break
            j, k = i + 1, n - 1
            while j < k:
                y, z = s_nums[j], s_nums[k]
                total = x + y + z
                if total == 0:
                    answer.append([x, y, z])
                    j += 1
                    k -= 1
                    while j < k and s_nums[j] == s_nums[j - 1]:
                        j += 1
                    while j < k and s_nums[k] == s_nums[k + 1]:
                        k -= 1
                elif total < 0:
                    j += 1
                else:
                    k -= 1
        return answer
