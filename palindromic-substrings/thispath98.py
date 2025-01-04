class Solution:
    def countSubstrings(self, s: str) -> int:
        """
        Intuition:
            2중 루프를 돌면서 각 substring에 대해
            palindrome인지 아닌지 확인한다.
            한번 palindrome인지 확인했으면, set에 추가하여
            중복 확인을 한다.

        Time Complexity:
            O(N^2 x s.length):
                2중 루프는 N^2만큼 소요되고,
                각 루프에 palindrome을 체크하는 것은
                s.length만큼 소요된다.

        Space Complexity:
            O(N^2):
                palindrome이 모두 중복되지 않을 경우 set에
                s의 substring 개수만큼 저장한다.
                이는 대략 N^2이다.
        """
        def is_palindrome(s):
            return s == s[::-1]

        palindrome_set = set()
        answer = 0
        for i in range(1, len(s) + 1):
            for j in range(0, len(s) - i + 1):
                substr = s[j: j + i]
                if substr in palindrome_set or is_palindrome(substr):
                    palindrome_set.add(substr)
                    answer += 1
        return answer


class SolutionDPSet:
    def countSubstrings(self, s: str) -> int:
        """
        Intuition:
            위 solution에서 중복을 제거할 수 있는 방법은,
            start : end 길이를 갖는 substring에서
            s[start] == s[end]이고, start + 1 : end - 1의
            substring이 palindrome이라면, 이 substring은
            palindrome이라고 볼 수 있다.

        Time Complexity:
            O(N^2):
                DP로 인해 palindrome을 찾는 함수가 대략
                상수의 시간복잡도가 걸린다고 볼 수 있다.
                따라서 substring을 만드는 이중 루프에서의
                시간복잡도가 걸릴 수 있다고 보면 된다.

        Space Complexity:
            O(N^2):
                dp set에 index set을 저장하는데, 최악의 경우
                index set은 N^2개만큼 저장될 수 있다.

        Key takeaway:
            dp를 이용해서 푸는 방식에 대해 익숙해져야겠다.

            의문점은 leetcode에서 bruteforce보다 시간이 더 소요되었다는 것이다.
            아마 list 크기를 초과할 경우에 append를 할 경우,
            리스트 크기를 2배만큼 늘리는 list doubling 방식이
            set에도 적용이 되어 느려진 것으로 보인다.
        """
        dp = set()


        def is_palindrome(start, end):
            while start < end:
                if s[start] != s[end]:
                    return False
                if (start, end) in dp:
                    return True
                start += 1
                end -= 1

            return True


        answer = 0
        for length in range(1, len(s) + 1):
            for start in range(0, len(s) - length + 1):
                end = start + length - 1
                if (start, end) in dp or is_palindrome(start, end):
                    dp.add((start, end))
                    answer += 1
        return answer


class SolutionDPList:
    def countSubstrings(self, s: str) -> int:
        """
        Intuition:
            DP solution에서 set로 저장하지 않고,
            이중 리스트로 저장하는 것으로 수정했다.
            length = 2인 경우에는 start와 end만 동일하면
            palindrome으로 판단할 수 있어 조건을 추가했다.

        Time Complexity:
            O(N^2):
                DP로 인해 palindrome을 찾는 함수가 대략
                상수의 시간복잡도가 걸린다고 볼 수 있다.
                따라서 substring을 만드는 이중 루프에서의
                시간복잡도가 걸릴 수 있다고 보면 된다.

        Space Complexity:
            O(N^2):
                dp 리스트에 substring 이중 리스트를 저장하므로
                N^2개만큼 저장될 수 있다.

        Key takeaway:
            이 방법이 가장 빠르게 동작했다.
        """
        dp = [[False for _ in s] for _ in s]
        answer = 0

        for i in range(len(s)):
            dp[i][i] = True
            answer += 1

        for length in range(2, len(s) + 1):
            for start in range(len(s) - length + 1):
                end = start + length - 1
                if s[start] == s[end]:
                    if length == 2 or dp[start + 1][end - 1]:
                        dp[start][end] = True
                        answer += 1

        return answer
