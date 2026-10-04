class Solution:
    def alienOrder(self, words: List[str]) -> str:
        # 단어 개수 저장
        N = len(words)

        # 그래프와 진입차수 저장 구조 초기화
        graph = defaultdict(list)
        indegree = defaultdict(int)

        # 단어 쌍을 차례로 비교하며 그래프와 진입차수 정보 구축
        for i in range(1, N):
            prev = words[i - 1]
            curr = words[i]

            # 예외: 앞 단어가 더 길고, 뒷 단어의 접두사라면 잘못된 사전 순서임
            if len(prev) > len(curr) and prev.startswith(curr):
                return ""

            # 첫 번째로 다른 글자 쌍 찾아서 순서 규칙 추가
            for prev_char, curr_char in zip(prev, curr):
                if prev_char != curr_char:
                    if curr_char not in graph[prev_char]:  # 중복 방지
                        graph[prev_char].append(curr_char)
                        indegree[curr_char] += 1
                    break  # 한 쌍만 비교

        # 등장하는 모든 글자 모음
        characters = set("".join(words))

        # 진입차수 0인 글자를 큐에 넣어 시작 노드로 설정
        starts = deque([])
        for char in characters:
            if indegree[char] == 0:
                starts.append(char)

        ans = []

        # 위상정렬(BFS) 진행
        while starts:
            node = starts.popleft()
            ans.append(node)

            # 현재 글자가 가리키는 다음 글자들의 진입차수 감소 및 0이 되면 큐에 추가
            for dest in graph[node]:
                indegree[dest] -= 1
                if indegree[dest] == 0:
                    starts.append(dest)

        # 모든 글자를 위상정렬 결과에 포함 못하면 순환이 존재 → 빈 문자열 반환
        if len(ans) != len(characters):
            return ""

        # 위상정렬 결과를 문자열로 반환
        return "".join(ans)
