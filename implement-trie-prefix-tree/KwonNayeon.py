"""
Constraints:
1. 1 <= word.length, prefix.length <= 2000
2. word and prefix consist only of lowercase English letters.
3. At most 3 * 10^4 calls in total will be made to insert, search, and startsWith.

Time Complexity: 
- insert: O(m), m은 입력 단어의 길이
- search: O(m), m은 검색 단어의 길이
- startsWith: O(m), m은 접두사의 길이

Space Complexity: 
- O(N*M), N은 저장된 단어의 개수, M은 평균 단어 길이

이해한 내용:
1. Prefix(접두사)의 의미
  - 문법적 접두사(un-, pre- 등)가 아님
  - 단순히 단어의 앞부분에 있는 문자열을 의미
  - 예: "apple"의 접두사 -> "a", "ap", "app", "appl", "apple"

2. 실행 방식
  - 입력으로 주어진 명령어를 순차적으로 실행
  - 예: ["Trie", "insert", "search"] 순서대로 실행
  - 각 명령어에 해당하는 인자값도 순서대로 적용

3. 자료구조 선택 (Trie with Hash Table)
  - Trie의 각 노드에서 자식 노드를 저장할 때 해시 테이블 사용
  - 키: 다음 문자, 값: 해당 문자의 TrieNode
  - 장점: 다음 문자 검색이 O(1)로 가능

Notes:
- 혼자 구현하기 어려워서, 공부한 내용을 정리만 했습니다.
"""

# 트리의 각 "노드(마디)"를 표현하는 클래스
class TrieNode:
   def __init__(self):
       # children은 "다음 글자들을 저장하는 공간"
       # 예: 'a' 다음에 'p'가 올 수 있다면 children['p']에 저장
       self.children = {}  
       
       # is_end는 "여기까지가 하나의 단어가 되는지"를 표시
       # 예: "app"을 저장했다면, p노드의 is_end가 True
       self.is_end = False    

# 트리 전체를 관리하는 클래스
class Trie:
   def __init__(self):
       # 트리의 시작점 생성
       # 실제 글자들은 root 밑에서부터 시작
       self.root = TrieNode()
   
   # 새로운 단어를 트리에 추가하는 함수
   def insert(self, word: str) -> None:
       node = self.root
       for char in word:
           if char not in node.children:
               node.children[char] = TrieNode()
           node = node.children[char]
       node.is_end = True
   
   # 단어가 트리에 있는지 찾는 함수
   def search(self, word: str) -> bool:
       node = self.root
       for char in word:
           if char in node.children:
               node = node.children[char]
           else:
               return False
       return node.is_end
   
   # 해당 접두사로 시작하는 단어가 있는지 확인하는 함수
   def startsWith(self, prefix: str) -> bool:
       node = self.root
       for char in prefix:
           if char in node.children:
               node = node.children[char]
           else:
               return False
       return True

"""
사용 예시:
trie = Trie()
trie.insert("apple")      # "apple" 저장
trie.search("apple")      # True 반환 (apple이 있음)
trie.search("app")        # False 반환 (app은 없음)
trie.startsWith("app")    # True 반환 (app으로 시작하는 단어가 있음)
"""
