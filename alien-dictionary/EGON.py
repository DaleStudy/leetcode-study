from collections import deque
from typing import List
from unittest import TestCase, main


class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        return self.solve_topological_sort(words)

    """
    LintCode 로그인이 안되어서 https://neetcode.io/problems/foreign-dictionary 에서 실행시키고 통과만 확인했습니다.

    Runtime: ? ms (Beats ?%)
    Time Complexity:
        #0. 복잡도 변수 정의 
        - words 배열의 길이를 n
        - words 배열을 이루는 단어들의 평균 길이를 l
        - words 배열을 이루는 단어를 이루는 문자들의 총 갯수를 c (= n * l)
        - words 배열을 이루는 단어를 이루는 문자들의 중복 제거 집합의 크기를 s라 하자
        
        #1. 초기화
        - words 배열을 이루는 단어를 이루는 문자들을 조회하며 char_set을 초기화하는데 O(c)
        - 위상정렬에 사용할 graph 딕셔너리 초기화를 위해 char_set의 크기만큼 조회하므로 O(s)
        - 마찬가지로 위상정렬에 사용할 rank 딕셔너리 초기화에 O(s)
        > O(c) + O(s) + O(s) ~= O(c + s)
        
        #2. 위상정렬 간선 초기화
        - words 배열을 조회하는데 O(n - 1)
            - 단어 간 접두사 관계인 경우, 체크하는 startswith 메서드 사용에 * O(l)
            - 단어 간 접두사 관계가 아닌 경우, first_char, second_char를 구하는데
                - zip 생성에 O(l)
                    - zip 조회에 * O(l)
        > O(n - 1) * (O(l) + O(l) * O(l)) ~= O(n) * O(l ^ 2) ~= O(c * l) ~= O(c)
        
        #3. 위상정렬 실행
        - dq 초기화에 rank 딕셔너리의 모든 키를 조회하는데 O(s)
        - dq를 이용해서 graph 딕셔너리의 모든 values를 순회하는데, #2에서 각 first_char, second_char마다 1회 value가 추가되었으므로, 중복이 없는 경우 최대 O(n), upper bound
        > O(s) + O(n) ~= O(s + n), upper bound
        
        #4. 최종 계산
        > O(c + s) + O(c) + O(s + n) ~= O(c + s) + O(s + n) = O(n * l + s) + O(n + s) ~= O(n * l + s), upper bound

    Memory: ? MB (Beats ?%)
    Space Complexity: O(s + c)
        - char_set의 크기에서 O(s)
        - graph의 keys는 최대 s개이고 values는 최대 c개이므로 O(s + c), upper bound
        - rank의 keys의 크기에서 O(s)
        - dq의 최대 크기는 rank의 크기와 같으므로 O(s)
        > O(s) + O(s + c) + O(s) + O(s) ~= O(s + c)
    """
    def solve_topological_sort(self, words: List[str]) -> str:
        if not words:
            return ""

        char_set = set([char for word in words for char in word])
        graph = {char: set() for char in char_set}
        rank = {char: 0 for char in char_set}
        for i in range(len(words) - 1):
            first_word, second_word = words[i], words[i + 1]

            if len(first_word) > len(second_word) and first_word.startswith(second_word):
                return ""

            first_char, second_char = next(((fc, sc) for fc, sc in zip(first_word, second_word) if fc != sc), ("", ""))
            if (first_char and second_char) and second_char not in graph[first_char]:
                graph[first_char].add(second_char)
                rank[second_char] += 1

        result = []
        dq = deque([char for char in rank if rank[char] == 0])
        while dq:
            curr_char = dq.popleft()
            result.append(curr_char)
            for post_char in graph[curr_char]:
                rank[post_char] -= 1
                if rank[post_char] == 0:
                    dq.append(post_char)

        if len(result) != len(rank):
            return ""
        else:
            return "".join(result)


class _LeetCodeTestCases(TestCase):
    def test_1(self):
        words = ["z","o"]
        output = "zo"
        solution = Solution()
        self.assertEqual(solution.foreignDictionary(words), output)

    def test_2(self):
        words = ["hrn","hrf","er","enn","rfnn"]
        output = "hernf"
        solution = Solution()
        self.assertEqual(solution.foreignDictionary(words), output)

    def test_3(self):
        words = ["wrt","wrf","er","ett","rftt","te"]
        output = "wertf"
        solution = Solution()
        self.assertEqual(solution.foreignDictionary(words), output)


if __name__ == '__main__':
    main()
