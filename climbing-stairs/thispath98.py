class Solution:
    def climbStairsFact(self, n: int) -> int:
        """
        Intuition:
            1 + 1 + ... + 1 는 2가 0개일 때 n을 만들 수 있는 경우의 수 = 1.
            1 + 2 + ... + 1 는 2가 1개일 때 n을 만들 수 있는 경우의 수 = (n-1)C1.
            2 + 2 + ... + 1 는 2가 2개일 때 n을 만들 수 있는 경우의 수 = (n-2)C2.
            ...
            즉, n이 0부터 최대로 놓을 수 있는 값(two_cnt)까지
            1로 놓여져 있는 배열에서 2의 위치를 선택(조합)하는 것과 같다.

        Time Complexity:
            O(N^2 log N):
                (n-i)Ci는 O((N - i) log i)이고, i가 0부터 two_cnt까지 증가할 경우
                대략 O(N log N)로 계산한다.
                이를 two_cnt(N//2) 까지 반복하므로, O(N^2 log N).

        Space Complexity:
            O(1):
                answer를 업데이트 해가며 값 계산.
        """
        import math

        two_cnt = n // 2
        answer = 1

        for i in range(1, two_cnt + 1):
            # (n - i)Ci
            # 여기서 int로 형변환 할 경우 수치적 불안정 발생
            answer += math.factorial(n - i) / math.factorial(n - 2 * i) / math.factorial(i)

        return int(answer)  # int로 형변환 하지 않을 경우 TypeError

    def climbStairsComb(self, n: int) -> int:
        """
        Intuition:
            `climbStairsFact`에서 Factorial은 수치적 불안정성으로 인해
            더욱 안정적인 math.comb를 사용한다.

        Time Complexity:
            O(N^2 log N):
                (n-i)Ci는 O((N - i) log i)이고, i가 0부터 two_cnt까지 증가할 경우
                대략 O(N log N)로 계산한다.
                이를 two_cnt(N//2) 까지 반복하므로, O(N^2 log N).

        Space Complexity:
            O(1):
                answer를 업데이트 해가며 값 계산.
        """
        import math

        two_cnt = n // 2
        answer = 1

        for i in range(1, two_cnt + 1):
            # (n - i)Ci
            # math.comb 메소드는 수치적으로 안정적으로 계산해준다
            answer += math.comb(n - i, i)
        return answer

    def climbStairsFib(self, n: int) -> int:
        """
        Intuition:
            climb stairs 문제는 대표적인 피보나치 수열 문제이다.
            실제로 경우의 수를 계산해보면,
            1 -> 1
            2 -> 2
            3 -> 3
            4 -> 5
            5 -> 8
            ...
            로 피보나치 수열을 따르는 것을 알 수 있다.

        Time Complexity:
            O(N):
                N번 순회하여 피보나치 수열 구현.

        Space Complexity:
            O(N):
                N개 만큼 해시 key-value 쌍을 저장.
        """
        fib_dict = {1: 1, 2: 2, 3: 3}
        for i in range(1, n + 1):
            if i not in fib_dict:
                fib_dict[i] = fib_dict[i - 1] + fib_dict[i - 2]
            if i == n:
                return fib_dict[i]
