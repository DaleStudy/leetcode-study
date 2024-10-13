from collections import Counter, deque
class Solution:
    # 시간복잡도: O(S+T)
    # 공간복잡도: O(T)
    def minWindow(self, s: str, t: str) -> str:
        counter = Counter(t)

        index = deque()
        tot = 0
        m = len(s)
        st, en = 0, m - 1
        for idx, ch in enumerate(s):
            if ch not in counter:
                continue

            counter[ch] -= 1
            index.append(idx)

            if counter[ch] == 0:
                tot += 1

            while index:
                if counter[s[index[0]]] < 0:
                    counter[s[index[0]]] += 1
                    index.popleft()
                else:
                    break

            if tot == len(counter):
                a = index[0]
                b = idx
                if b - a + 1 < m:
                    st, en = a, b
                    m = en - st + 1

        if tot != len(counter):
            return ""

        return s[st:en + 1]
