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
시간복잡도: O(NlogN)
  - 세그먼트 트리 한 번 업데이트: O(logN)
  - 슬라이딩 윈도우 오른쪽 포인터 한 번씩 전진: O(N)
공간복잡도: O(N)
  - 세그먼트 트리 크기: O(N) (알파벳 26개에 대해 4N+1 노드)

[세그먼트 트리 개요]
- 각 알파벳(A~Z)의 빈도수를 표현하는 세그먼트 트리를 구현함.
- 각 트리 노드는 구간 내 현재 알파벳 빈도 총합과 그 구간 내 최빈값(가장 많이 등장한 알파벳의 빈도)을 저장함.
- 이진 트리 구조로 각 알파벳 인덱스를 리프 노드(0~25)에 매핑.

[핵심 동작 설명]
- window.update(문자, ±1): 현재 윈도우에 새 문자를 추가/제거할 때 해당 알파벳의 빈도수를 O(logN)에 갱신.
- window.tree[1][0]: 세그먼트 트리 루트의 첫 번째 값으로, 현재 윈도우 내 전체 문자 개수(윈도우 길이)를 의미.
- window.tree[1][1]: 루트의 두 번째 값으로, 현재 윈도우 내에서 가장 많이 등장한 문자의 등장 횟수를 의미.
- (윈도우 전체길이 - 최빈값) > k 를 만족할 때까지 왼쪽 포인터를 옮기며(=왼쪽 문자 제거), 윈도우가 k개 이하의 문자만 바꾸면 모두 동일하게 만들 수 있는 범위로 축소.
- 매 반복마다 ans를 최대 윈도우 크기로 갱신.

※ 세그먼트 트리 사용은 이 문제에 최적해는 아니나, 자료구조 학습에는 좋은 연습 예제.
"""
class SegTree:
    def __init__(self):
        # summation, largest
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

            while window.tree[1][0] - window.tree[1][1] > k:
                window.update(s[left], -1)
                left += 1

            ans = max(ans, right - left + 1)

        return ans
