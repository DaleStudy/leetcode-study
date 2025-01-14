# 공간복잡도 O(n): dictionary 멤버로 set을 사용
# 시간복잡도 O(n*p): 삽입연산은 O(1)을 사용
import re

class WordDictionary:

    def __init__(self):
        self.dictionary = set()

    def addWord(self, word: str) -> None:
        self.dictionary.add(word)

    def search(self, word: str) -> bool:
        if '.' in word:
            pattern = re.compile(word)
            # O(n) times
            for item in self.dictionary:
                # O(p) times : 패턴의 길이(p)
                if pattern.fullmatch(item):
                    return True
            return False
        else:
            return word in self.dictionary
