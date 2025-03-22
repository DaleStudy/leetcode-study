from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n, m, word_length = len(board), len(board[0]), len(word)
        
        def search(row, col, word_idx, visited):
            # 경계 체크
            if not (0 <= row < n and 0 <= col < m):
                return False
            # 이미 방문했거나, 문자가 일치하지 않는 경우
            if (row, col) in visited or board[row][col] != word[word_idx]:
                return False
            
            # 모든 문자를 찾은 경우
            if word_idx == word_length - 1:
                return True

            # 현재 셀을 방문한 것으로 표시
            visited.add((row, col))

            # 인접한 셀 확인
            found = (
                search(row - 1, col, word_idx + 1, visited) or
                search(row + 1, col, word_idx + 1, visited) or
                search(row, col - 1, word_idx + 1, visited) or
                search(row, col + 1, word_idx + 1, visited)
            )
            # 현재 셀 방문 해제 (백트래킹)
            visited.remove((row, col))

            return found

        # 모든 셀에서 탐색 시작
        for row in range(n):
            for col in range(m):
                if board[row][col] == word[0]:
                    if search(row, col, 0, set()):
                        return True
        
        return False

# 풀이 1: 방문 기록을 Set으로 관리하는 방식
# 시간 복잡도:
#   - 각 셀에서 DFS를 시작하며, 각 DFS는 최대 네 방향으로 이동하며 word의 길이만큼 재귀 호출을 진행함.
#   - 최악의 경우 O(n * 4^k), 여기서 n은 전체 셀의 개수, k는 word의 길이.
# 공간 복잡도:
#   - visited Set 사용: O(k), 여기서 k는 word의 길이.
#   - 재귀 호출 스택: O(k), word의 길이만큼 재귀 호출이 쌓임.
#   => 총 공간 복잡도: O(k)


from collections import Counter

class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        n, m = len(board), len(board[0])
        word_length = len(word)
        
        # 조기 종료: board에 word를 구성할 충분한 문자가 있는지 확인
        board_counter = Counter(char for row in board for char in row)
        word_counter = Counter(word)
        if any(word_counter[char] > board_counter[char] for char in word_counter):
            return False

        def search(row, col, idx):
            # 기본 조건: 모든 문자가 일치한 경우
            if idx == word_length:
                return True
            
            # 경계 조건 및 문자 일치 여부 확인
            if row < 0 or row >= n or col < 0 or col >= m or board[row][col] != word[idx]:
                return False
            
            # 현재 셀을 방문한 것으로 임시 표시
            temp = board[row][col]
            board[row][col] = "#"
            
            # 모든 방향 탐색
            found = (
                search(row - 1, col, idx + 1) or
                search(row + 1, col, idx + 1) or
                search(row, col - 1, idx + 1) or
                search(row, col + 1, idx + 1)
            )
            
            # 탐색 후 셀 복원
            board[row][col] = temp
            return found

        # 첫 번째 문자와 일치하는 모든 셀에서 DFS 시작
        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0] and search(i, j, 0):
                    return True
        
        return False

# 풀이 2: Board를 직접 수정해 방문 기록 관리
# 시간 복잡도:
#   - 각 셀에서 DFS를 시작하며, 최대 네 방향으로 이동하며 word의 길이만큼 재귀 호출을 진행함.
#   - 최악의 경우 O(n * 4^k), 여기서 n은 전체 셀의 개수, k는 word의 길이.
# 공간 복잡도:
#   - 추가 공간 사용 없이 Board를 직접 수정: O(1).
#   - 재귀 호출 스택: O(k), word의 길이만큼 재귀 호출이 쌓임.
#   => 총 공간 복잡도: O(k)
