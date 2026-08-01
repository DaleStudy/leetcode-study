"""
solution1: 직관적인 풀이 (PASS인데 엄청 느리다)

Runetime: 5438ms, Beats 5.00%
Memory: 26.74MB, Beats 99.60%

접근법:
    addWord: `word_set`에 단어를 삽입한다.
    search: 와일드카드(`.`)은 a-z로 변환해서 데카르트 곱을 통해 가능한 모든 문자열의 조합인 `candidates`를 만든다. `candidates`를 순회하며 `word_set`에 단어가 있는지 확인한다.
"""
import string
import itertools

class WordDictionary:
    def __init__(self):
        self.word_set = set()
        
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

        """Example:
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

"""
Soultion2: `word`와 길이가 같은 단어들만 탐색하는 방법
"""
from collections import defaultdict


class WordDictionary:
    def __init__(self):
        self.buckets: defaultdict[int, set[str]] = defaultdict(set)

    """
    L: `word`의 길이

    Time: O(L)
    Space: O(L)
    """
    def addWord(self, word: str) -> None:
        bucket = self.buckets[len(word)]

        if word not in bucket:
            bucket.add(word)

    """
    L: `word`의 길이
    N: 같은 길이를 가진 저장된 단어의 개수

    Time: O(L) - 와일드카드 없을 때 / O(N*L) - 와일드카드 있을 때
    Space: O(1)
    """
    def search(self, word: str) -> bool:
        # 글자수가 동일한 단어들만 탐색
        bucket: set[str] = self.buckets[len(word)]

        # 와일드카드 없을 때
        if '.' not in word:
            return word in bucket

        for candidate in bucket:
            if self._matches(word, candidate):
                return True

        return False

    def _matches(self, word: str, candidate: str) -> bool:
        for i, c in enumerate(word):
            if c != '.' and c != candidate[i]:
                return False

        return True

# wordDictionary = WordDictionary()
# wordDictionary.addWord("bad")
# wordDictionary.search("..d")