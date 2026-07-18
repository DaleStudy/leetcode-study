from collections import defaultdict
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        pos = defaultdict(list)
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] in word:
                    tmp = pos.get(board[i][j], [])
                    tmp.append([i, j])
                    pos[board[i][j]] = tmp

        paths = pos.get(word[0], [])
        paths = [[path] for path in paths]

        for w in word[1:]:
            temp = []

            while len(paths) > 0:
                path = paths.pop()
                i , j = path[-1]
                if ([i, j+1] in pos[w]) and ([i, j+1] not in path):
                    temp.append(path[:] + [[i, j+1]])
                if ([i, j-1] in pos[w]) and ([i, j-1] not in path):
                    temp.append(path[:] + [[i, j-1]])
                if ([i+1, j] in pos[w]) and ([i+1, j] not in path):
                    temp.append(path[:] + [[i+1, j]])
                if ([i-1, j] in pos[w]) and ([i-1, j] not in path):
                    temp.append(path[:] + [[i-1, j]])
            paths.extend(temp)
        for path in paths:
            if len(path) == len(word):
                return True
        return False 
