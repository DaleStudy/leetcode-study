"""

시간복잡도: O(n)
공간복잡도: O(n)

슬라이딩 윈도우 기법을 사용해 문자열 s에서 t의 모든 문자를 포함하는 최소 윈도우를 찾는다.

Window 클래스는 타겟 문자열(t)에 구성된 각 문자별 필요한 개수를 카운트하고,
윈도우 내 해당 문자 개수를 관리하며, 현재 윈도우가 타겟을 만족하는지(check) 확인한다.

add 메서드는 윈도우에 문자를 추가하여 개수를 갱신하고,
  - 타겟의 문자 갯수와 같아지면 key_count를 증가시킨다.
remove 메서드는 윈도우에서 문자를 제거하여 개수를 줄인다.
  - 타겟의 문자 갯수보다 작아지면 key_count를 감소시킨다.

check 메서드는 윈도우에 타겟 문자가 필요한 만큼 모두 포함되어 있는지 검사한다.
  - key_count와 target_count가 같으면 True를 반환한다.
"""
class Window:
    def __init__(self, target: str):
        self.target = Counter(target)
        self.window = defaultdict(int)

        self.key_count = 0
        self.target_count = len(self.target)

    def check(self):
        return self.key_count == self.target_count

    def add(self, ch: str):
        self.window[ch] += 1

        if self.window[ch] == self.target[ch]:
            self.key_count += 1

    def remove(self, ch: str):
        self.window[ch] -= 1
        if self.window[ch] < self.target[ch]:
            self.key_count -= 1


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        window = Window(t)
        left = 0
        ans = (-float("inf"), float("inf"))

        for right, value in enumerate(s):

            window.add(value)
            if not window.check():
                continue

            while window.check():
                window.remove(s[left])
                left += 1

            if ans[1] - ans[0] > right - left:
                ans = (left - 1, right)

        if ans[0] == -float("inf"):
            return ""

        return s[ans[0] : ans[1] + 1]
