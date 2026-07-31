"""
solution1: 직관적인 풀이
통과는 하지만 아주 느리다

Runetime: 5438ms, Beats 5.00%
Memory: 26.74MB, Beats 99.60%

접근법:
    addWord: `word_set`에 단어를 삽입한다.
    search: `.`은 a-z로 변환해서 데카르트 곱을 통해 가능한 모든 문자열의 조합인 `candidates`를 만든다. `candidates`를 순회하며 `word_set`에 단어가 있는지 확인한다.
"""
import string
import itertools

class WordDictionary:
    def __init__(self):
        self.word_set = set()
        print(string.ascii_lowercase)
        
    """
    L: `word`의 길이
    N: `word_set`에 저장된 단어의 개수

    Time: O(L), set.add() 메서드는 문자열 전체를 순회하며 해시 값을 계산해야 하므로
    Space: O(N*L)
    """
    def addWord(self, word: str) -> None:
        self.word_set.add(word)

    """
    L: `word`의 길이
    
    Time: O(L)
    Space: O(L)
    """
    def search(self, word: str) -> bool:
        candidates = []

        """예시
        word: "bad", candidates: ['b', 'a', 'd']
        word: ".ad", candidates: ['abcdefghijklmnopqrstuvwxyz', 'a', 'd']
        word: "b..", candidates: ['b', 'abcdefghijklmnopqrstuvwxyz', 'abcdefghijklmnopqrstuvwxyz']
        """
        for c in word:
            if c == '.':
                candidates.append(string.ascii_lowercase)
            else:
                candidates.append(c)

        # 데카르트 곱으로 가능한 조합 생성힌다
        for p in itertools.product(*candidates):
            if ''.join(p) in self.word_set:
                return True

        return False
