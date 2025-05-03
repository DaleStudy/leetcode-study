'''
이 문제는 문자열을 효율적으로 저장하고 검색하는 트리 구조임 (예 : 자동완성 기능)
주요 기능 : 단어 추가(insert), 단어 검색(search), 접두사 확인(startsWith)

Example 1.의 단계별 동작

메서드 호출 순서 리스트	        인자 리스트	            실제 호출 예시
"Trie"	                   []	                Trie()          -> 빈 트라이를 만듬. 루트 노드가 생성되고, 아무 문자도 저장되어 있지 않음
"insert"	               ["apple"]	        insert("apple") -> 'a' 노드가 없으면 새로 만들고 이동
                                                                -> 'p' 노드가 없으면 새로 만들고 이동
                                                                -> 또 'p' 노드가 없으면 새로 만들고 이동
                                                                -> 'l' 노드가 없으면 새로 만들고 이동
                                                                -> 'e' 노드가 없으면 새로 만들고 이동
                                                                -> 마지막 'e' 노드에 is_end = True 표시 (여기까지가 "apple"이라는 단어임을 뜻함)

"search"	               ["apple"]	        search("apple") -> 루트부터 'a' → 'p' → 'p' → 'l' → 'e' 노드까지 차례로 이동
                                                                -> 마지막 'e' 노드가 is_end = True 이므로 True 반환

"search"	               ["app"]	            search("app")   -> 루트부터 'a' → 'p' → 'p' 노드까지 이동
                                                                -> 'p' 노드의 is_end 값이 False (아직 "app"이라는 단어가 완성되지 않았음)
                                                                -> 따라서 False 반환
"startsWith"	           ["app"]	            startsWith("app") -> 루트부터 'a' → 'p' → 'p' 노드까지 이동
                                                                  -> 노드가 존재하므로 True 반환 (접두사는 존재함)

"insert"	               ["app"]	            insert("app")     -> 루트부터 'a' → 'p' → 'p' 노드까지 이미 존재하므로 새 노드 생성 안 함
                                                                  -> 마지막 'p' 노드에 is_end = True 표시 (이제 "app"도 완성된 단어임)
                                                                  -> "app"은 처음에 is_end=False였기 때문에 검색 시 False가 나왔고, 삽입 후 True가 됨

"search"	               ["app"]	            search("app")     -> 루트부터 'a' → 'p' → 'p' 노드까지 이동
                                                                  -> 마지막 'p' 노드가 is_end = True 이므로 True 반환

<트라이 구조> 

루트
 └─ 'a'
     └─ 'p'
         └─ 'p' (is_end=True)  ← "app"
             └─ 'l'
                 └─ 'e' (is_end=True)  ← "apple"


'''

class TrieNode:  # 트라이의 각 노드를 표현하는 클래스
    def __init__(self):
        self.children = {}  # 현재 노드의 자식들을 {문자:노드} 형태로 저장 
        self.is_end = False  # 현재 노드가 단어의 끝인지 표시(기본값 False)

class Trie:
    def __init__(self):
        self.root = TrieNode()  # 트라이의 시작점인 빈 루트 노드 생성

    def insert(self, word: str) -> None:
        node = self.root    # 루트 노드에서 시작
        for char in word:   # 단어의 각 문자를 하나씩 처리
            if char not in node.children:   # 현재 노드의 자식에 문자가 없으면
                node.children[char] = TrieNode()  # 새로운 노드 생성 후 자식에 추가
            node = node.children[char]     # 다음 문자 노드로 이동
        node.is_end = True      # 단어의 마지막 문자 노드에 끝 표시

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:      # 단어의 각 문자를 따라 이동 
            if char not in node.children:  # 문자가 없으면 단어 존재 X -> False
                return False
            node = node.children[char]
        return node.is_end  # 모든 문자를 통과했다면, 마지막 노드가 단어 끝인지 확인


    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:     # 접두사의 각 문자를 따라 이동
            if char not in node.children:  # 문자 없으면 접두사 존재 X -> False
                return False    # 모든 문자가 존재 -> 접두사 O
            node = node.children[char]
        return True  # 7. 접두사 존재


