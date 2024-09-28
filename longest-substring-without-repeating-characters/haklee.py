"""TC: O(n), SC: O(n)

아이디어:
투포인터로 문자열의 시작, 끝 인덱스를 관리한다. 그리고 문자열 안에 있는 문자를 set으로 관리한다.
- 시작~끝 사이에 모든 문자가 서로 다르면 끝 인덱스를 하나 뒤로 옮긴다.
- 새로운 문자열의 제일 끝에 있는 문자가 혹시 set 안에 있으면 시작 인덱스를 뒤로 옮기는 작업을
  해당 문자랑 같은 문자가 나올 때까지 진행한다. 즉, 끝을 고정하고 앞을 계속 옮겨서 새로운 문자열에
  있는 모든 문자들이 다른 문자가 되도록 만든다.
    - e.g.) abcdefd -> abcdefd
            ^     ^        ^ ^
            s     e        s e
- 위의 과정을 계속 반복하면서 문자열의 최대 길이 값을 갱신한다.

SC:
- 새로운 문자열의 시작과 끝 인덱스 값을 관리하는 데에 O(1).
- 새로운 문자열 안에 들어있는 문자를 set으로 관리하는 데에 최악의 경우 n개의 문자가 모두 다를때 O(n).
- 최대 문자열 길이를 관리하는 데에 O(1).
- 종합하면 O(n).

TC:
- s, e는 모두 문자열의 인덱스를 나타내므로 s, e값을 아무리 많이 업데이트 해도 각가 문자열 길이보다
  많이 업데이트 할 수는 없다. 즉, O(n).
- set에서 특정 문자가 들어있는지 체크하고 set에 문자를 더하거나 제거하는 데에 O(1). 이 작업을 아무리
  많이 해도 s, e를 업데이트 하는 회수 만큼 진행하므로 총 O(n).
- 최대 문자열 길이를 업데이트 하는 데에 O(1). 이 또한 아무리 많이 진행해도 O(n).
- 종합하면 O(n).
"""


class Solution:
    def lengthOfLongestSubstring(self, string: str) -> int:
        if len(string) < 1:
            return 0
        s = e = 0
        letter_set = set([string[0]])
        sol = 1
        while True:
            e += 1
            if e == len(string):
                break

            if string[e] in letter_set:
                while True:
                    letter_set.discard(string[s])
                    if string[s] == string[e]:
                        break
                    s += 1
                s += 1
            letter_set.add(string[e])
            sol = max(len(letter_set), sol)
        return sol
