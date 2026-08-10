"""
시간복잡도 : O(N)
공간복잡도 : O(1)

1. freq 딕셔너리를 초기화한다.
2. s의 각 문자(value)에 대해 루프를 돈다.
3. freq[value]를 1 증가시킨다.
4. maxima를 현재 윈도우에서 가장 빈도가 높은 문자 빈도로 갱신한다.
5. 윈도우 크기에서 maxima의 값만큼을 뺀 값이 k보다 크면,
6. freq[s[left]]를 1 감소시키고 left를 1 증가시킨다.
7. ans를 윈도우의 최대 길이로 갱신한다.
8. 마지막으로 ans를 반환한다.
"""
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = defaultdict(int)
        # maxima : 현재 윈도우 내에서 가장 많이 등장한 문자의 빈도수
        maxima = left = ans = 0

        for right, value in enumerate(s):
            freq[value] += 1
            maxima = max(maxima, freq[value])

            while (right - left + 1) - maxima > k:
                freq[s[left]] -= 1
                left += 1

            ans = max(ans, right - left + 1)

        return ans

"""
시간복잡도 : O(log N)
공간복잡도 : O(N)

### 세그먼트 트리 구현 ### (윈도우 내 전체만 사용하므로 query 구현 없음)

#### 세그먼트 트리 원리
- 각 알파벳 빈도 합과 빈도가 가장 높은 문자의 빈도를 저장하는 세그먼트 트리를 사용한다.

#### 코드 설명
- window.update로 알파벳 개수를 갱신하며,
- window.tree[1][0]에서 현재 윈도우 내 전체 문자 수,
- window.tree[1][1]에서 윈도우 내 등장 빈도가 가장 높은 문자의 개수를 구한다.
- 윈도우 크기 - 최대 빈도가 k를 초과하면 left를 옮기며 윈도우를 줄인다.

> 불필요하게 복잡한 구현이지만, 세그먼트 트리를 공부하기엔 좋은 예제가 될 수 있다.
"""
class SegTree:
    def __init__(self):
        # [문자 개수 합, 최대값]
        self.tree = [[0, 0] for _ in range(26 * 4 + 1)]

    def _update(
        self,
        node_index: int,
        target_index: int,
        target_update: int,
        seg_left: int,
        seg_right: int,
    ):
        if seg_left == seg_right:
            self.tree[node_index][0] += target_update
            self.tree[node_index][1] += target_update
            return

        mid = (seg_left + seg_right) // 2

        if target_index <= mid:
            self._update(node_index * 2, target_index, target_update, seg_left, mid)
        else:
            self._update(
                node_index * 2 + 1, target_index, target_update, mid + 1, seg_right
            )

        self.tree[node_index][0] = (
            self.tree[node_index * 2][0] + self.tree[node_index * 2 + 1][0]
        )
        self.tree[node_index][1] = max(
            self.tree[node_index * 2][1], self.tree[node_index * 2 + 1][1]
        )

    def update(self, target: str, update: int):
        self._update(1, ord(target) - ord("A"), update, 0, 25)


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        window = SegTree()
        ans = 0

        for right, value in enumerate(s):
            window.update(value, 1)

            while window.tree[1][0] > 0 and window.tree[1][0] - window.tree[1][1] > k:
                window.update(s[left], -1)
                left += 1

            ans = max(ans, right - left + 1)

        return ans
