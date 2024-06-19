"""
79. Word Search
https://leetcode.com/problems/word-search/

Solution:
    To solve this problem, we think of the board as a graph. 
    We can use a depth-first search (DFS) to explore all possible paths starting from each cell.
    We can create a helper function that takes the current cell and the index of the current character in the word.

    - We can count the frequency of each character in the board.
    - We can check if all characters in the word exist in the board.
    - If we cannot find all characters in the board, we return False.

    - We can create a helper function that takes the current coordinates and the index in the word.
    - If the index is equal to the length of the word, 
        it means we have found all characters in the word, so we return True.
    - If the coordinates are out of bounds or the current character does not match,
        we return False.
    - We mark the current cell as visited and explore all possible directions.
    - If any direction returns True, we return True.
    - We unmark the current cell and return False.

    - We can find all indices of the first character in the word.
    - We can start the DFS from each index and return True if any DFS returns True.
    - If no DFS returns True, we return False.

Time complexity: O(m*n*4^l)
    - m and n are the dimensions of the board.
    - l is the length of the word.
    - We explore 4 directions at each cell, and the maximum depth is the length of the word.

Space complexity: O(l)
    - The recursive call stack has a maximum depth of the length of the word. 
    
"""


from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board or not word:
            return False

        m, n = len(board), len(board[0])
        
        # Step 1: Check if all characters in the word exist in the board
        char_count = {}
        for row in board:
            for char in row:
                if char in char_count:
                    char_count[char] += 1
                else:
                    char_count[char] = 1

        for char in word:
            if char not in char_count or char_count[char] == 0:
                return False
            char_count[char] -= 1

        # Helper function to check if the word can be found starting from (i, j)
        def dfs(i, j, word_index):
            if word_index == len(word):
                return True
            
            if i < 0 or i >= m or j < 0 or j >= n or board[i][j] != word[word_index]:
                return False

            temp = board[i][j]
            board[i][j] = "#"  # mark as visited

            # Explore all possible directions
            found = (dfs(i + 1, j, word_index + 1) or
                    dfs(i - 1, j, word_index + 1) or
                    dfs(i, j + 1, word_index + 1) or
                    dfs(i, j - 1, word_index + 1))

            board[i][j] = temp  # unmark
            return found

        # Step 2: Find all indices of the first character in the word
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0] and dfs(i, j, 0):
                    return True

        return False