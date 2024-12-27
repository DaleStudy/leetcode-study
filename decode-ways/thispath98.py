class Solution:
    def numDecodings(self, s: str) -> int:
        """
        Intuition:
            문자를 쪼개서 디코드 조합을 얻는다.
            이후, 디코드 조합에서 2개씩 묶을 경우 26보다 큰 수가 있을 수 있으므로
            다시 한번 쪼갠다.
            마지막으로 각 디코드 조합에서 값을 얻는 경우는
            피보나치 수열을 따른다.

        Time Complexity:
            O(N):
                문자를 쪼개고, 묶는 문자 조합을 구하고,
                피보나치 수열에서 값을 찾는 것은 모두 O(N)만큼 소요된다.

        Space Complexity:
            O(1):
                최악의 경우 N개에 대한 피보나치 수열을 구해야 하고,
                N은 최대 100이므로 O(1)이다.
        """
        if s[0] == "0":
            return 0

        # 문자열에서 0 앞에 1 혹은 2가 붙는지 확인
        # 그렇지 않다면, 디코드 할 수 없으므로 return 0
        # O(N)
        splitted_s = []
        start = 0
        for i in range(len(s)):
            if s[i] == "0":
                if s[i - 1] in "12":
                    splitted_s.append(s[start: i - 1])
                    start = i + 1
                else:
                    return 0
        splitted_s.append(s[start:])

        # 쪼개진 문자에서 두 문자를 보고, 묶을 수 있는지
        # (26 이하인지)를 확인한다.
        # 묶을 수 없다면, 문자를 다시 한번 쪼갠다.
        # O(N)
        interval = []
        for splitted in splitted_s:
            start = 0
            for i in range(1, len(splitted)):
                if int(splitted[i - 1: i + 1]) > 26:
                    interval.append(i - start)
                    start = i

            interval.append(len(splitted) - start)

        answer = 1
        fib_dict = {0: 1, 1: 1, 2: 2}


        def get_fib(n):
            if n not in fib_dict:
                fib_dict[n] = get_fib(n - 1) + get_fib(n - 2)
            return fib_dict[n]


        # 쪼개진 문자에서 디코드 조합은
        # 문자 개수를 피보나치 수열에 넣은 값이다.
        # 이 값들은 쪼개진 문자들에 대하여 곱셈으로 계산된다.
        # O(N)
        get_fib(max(interval))
        for n in interval:
            answer *= fib_dict[n]
        return answer
