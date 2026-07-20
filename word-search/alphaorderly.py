
"""
Time Complexity: O(N * 4^L)
Space Complexity: O(L)

### Classic Backtracking Solution ###

1. Initialize a set to store the cells that have been visited
2. Define a helper function to check if the cell is within the bounds of the board
3. Define a helper function to perform the backtracking
4. If the current index is equal to the length of the word, return True
5. If the cell is out of bounds or the cell does not match the current character, return False
6. Add the cell to the set ( to prevent revisiting the same cell )
7. Recursively call the helper function for the four possible directions
8. Remove the cell from the set ( backtracking )
9. Return False ( if the current path does not lead to the target word )
"""
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        check = set()
        ROW, COL = len(board), len(board[0])

        def bound(r: int, c: int) -> bool:
            return 0 <= r < ROW and 0 <= c < COL

        def backtracking(row: int, col: int, n: int) -> bool:
            nonlocal check

            if n == len(word):
                return True

            if not bound(row, col) or board[row][col] != word[n] or (row, col) in check: 
                return False

            check.add((row, col))
            if backtracking(row + 1, col, n + 1):
                return True
            if backtracking(row, col + 1, n + 1):
                return True
            if backtracking(row - 1, col, n + 1):
                return True
            if backtracking(row, col - 1, n + 1):
                return True
            check.remove((row, col))

            return False

        for row in range(len(board)):
            for col in range(len(board[row])):
                if backtracking(row, col, 0):
                    return True

        return False

"""
Time Complexity: O(N * 4^L)
Space Complexity: O(L)

### Optimized Backtracking Solution ###

1. Check if the board is larger than the word size itself
2. Check if the board can assemble the word
3. Make the word to search sparse character first
4. Start the backtracking
5. Check if the cell is within the bounds of the board
6. Check if the cell matches the current character
7. Check if the cell has been visited
8. Mark the cell as visited
9. Recursively call the helper function for the four possible directions
10. Unmark the cell as visited
11. Return False ( if the current path does not lead to the target word )


### Optimizing point ###
1. Check board is larger than word size itself
2. Check board can assemble word
3. Make word to search sparse character first
4. Use check as 2D matrix not set for better performance
"""
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROW, COL = len(board), len(board[0])
        N = len(word)

        ### 1. Check board is larger than word size itself
        if ROW * COL < len(word):
            return False

        ### 2. Check board can assemble word
        board_counter = Counter(board[r][c] for r in range(ROW) for c in range(COL))
        word_counter = Counter(word)

        for ch, freq in word_counter.items():
            if board_counter[ch] < freq:
                return False

        ### 3. Make word to search sparse character first
        if word_counter[word[0]] > word_counter[word[-1]]:
            word = word[::-1]

        ### -> START BACKTRCKING <- ###
        
        ### Prevent overlapping
        check = [[False] * COL for _ in range(ROW)]

        ### Define the four possible directions
        DIR = [
            [-1, 0],
            [1, 0],
            [0, -1],
            [0, 1]
        ]

        ### Helper function to check bound
        def bound(r: int, c: int) -> bool:
            return 0 <= r < ROW and 0 <= c < COL

        def backtracking(r: int, c: int, n: int) -> bool:
            ### If the current index is equal to the length of the word, return True
            if n == N:
                return True

            ### If the cell is out of bounds, return False
            if not bound(r, c):
                return False

            ### If the cell does not match the current character, return False
            if word[n] != board[r][c]:
                return False

            ### If the cell has been visited, return False
            if check[r][c]:
                return False

            check[r][c] = True
            for dr, dc in DIR:
                if backtracking(r + dr, c + dc, n + 1):
                    return True
            check[r][c] = False

        for r in range(ROW):
            for c in range(COL):
                if board[r][c] == word[0]:
                    if backtracking(r, c, 0):
                        return True

        return False
