'''
풀이
- BFS와 방문 여부를 기록하는 방식을 이용하여 풀이할 수 있습니다
- 주어진 문자열 s의 길이 n보다 1 더 큰 크기의 배열 visit을 False로 초기화해줍니다
  n + 1로 설정하는 이유는 BFS 설계를 쉽게 하기 위함입니다
- queue 기능을 해줄 deque인 dq를 생성해주고 초기값으로 0을 삽입합니다
  dq의 원소 curr가 갖는 의미는 `현재 탐색 중인 substring의 시작 index, 즉 s[curr:]입니다`
- while문을 진행하며 dq에서 curr를 pop해줍니다
  만약 curr를 탐색한 적이 있다면 지나치고, 탐색한 적이 없다면 starts_with 함수를 실행하고
  그 여부에 따라 dq에 curr를 추가 및 visit을 갱신합니다

Big O
- N: 주어진 문자열 s의 길이
- M: 주어진 문자열 배열 wordDict의 모든 문자열의 길이의 합

- Time complexity: O(N * M)
  - visit 배열로 방문 여부를 관리하기 때문에 탐색은 최대 N번 이뤄집니다
  - 각 탐색마다 wordDict를 순회하며 starts_with를 실행하는데 이 실행 시간은 M이 증가함에 따라 선형적으로 증가합니다

- Space complexity: O(N)
  - visit 배열의 크기는 N이 증가함에 따라 선형적으로 증가합니다
  - deque에 담긴 원소의 수는 최대 N까지 증가할 수 있습니다
'''

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        visit = [False] * (n + 1)

        def starts_with(idx: int, word: str) -> bool:
            m = len(word)
            for i in range(m):
                if s[idx + i] != word[i]:
                    return False
            return True
        
        dq = deque([0])

        while dq:
            curr = dq.popleft()

            if curr == len(s):
                return True

            for word in wordDict:
                m = len(word)
                if curr + m <= n and not visit[curr + m] and starts_with(curr, word):
                    dq.append(curr + m)
                    visit[curr + m] = True
        
        return False
