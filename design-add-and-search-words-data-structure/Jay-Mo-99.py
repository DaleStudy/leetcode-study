# 해석
# 0. TrieNode 클래스 정의:
#    - 각 TrieNode 인스턴스는 다음의 두 가지 속성을 가진다:
#        1) children: 현재 노드의 자식 노드들을 저장하는 딕셔너리 (문자 -> TrieNode 인스턴스).
#        2) is_end_of_word: 현재 노드가 단어의 끝인지 나타내는 Boolean 값.

# 1. WordDictionary 클래스 정의:
#    - WordDictionary 클래스는 Trie 자료구조를 사용하여 단어를 저장(addWord)하고 탐색(search)한다.

# 1-1. __init__ 함수:
#    - root는 TrieNode 클래스로 생성된 인스턴스를 가진다.
#    - Trie 자료구조의 시작점(루트 노드) 역할을 한다.

# 1-2. addWord 함수:
#        1) 루트 노드(self.root)에서 시작.
#        2) 단어의 각 문자를 순회하며:
#            - 현재 노드의 children에 문자가 없으면, 새 TrieNode를 생성해 추가.
#            - 현재 노드를 해당 문자의 자식 노드로 이동.
#        3) 단어의 마지막 문자를 처리한 후, 해당 노드의 is_end_of_word를 True로 설정.


# 1-3. search 함수:
#    - 주어진 단어가 Trie에 존재하는지 확인하는 함수.
#    - 와일드카드 문자(.)를 처리할 수 있다.
#    - 내부적으로 dfs(깊이 우선 탐색) 함수를 사용하여 트라이를 탐색.
#        - dfs(index, node):
#            1) 종료 조건: index가 단어 길이에 도달하면, 현재 노드의 is_end_of_word 반환.
#            2) 현재 문자가 '.'인 경우:
#                - 현재 노드의 모든 자식 노드에 대해 dfs를 호출.
#                - 하나라도 True를 반환하면 True 반환.
#            3) 현재 문자가 일반 문자인 경우:
#                - 자식 노드에 문자가 없으면 False 반환.
#                - 자식 노드로 이동해 dfs를 재귀 호출.



        #Big O
        # - N: 저장된 모든 단어의 총 문자 수 (Trie에 저장된 모든 문자의 개수).
        # - C: 알파벳의 개수 (영어 기준 최대 26).

        #Time Complexity: O(N) 
        #- addWord함수 : N에 기반하여 단어 추가 
        #- searchWord 함수: 
        #        - 일반 탐색: O(n), n은 단어의 길이.
        #        - 와일드카드 탐색: 최악의 경우 O(C^N), 
        #            - C는 알파벳 개수 (최대 26).
        #            - N은 단어의 길이. 와일드카드 문자가 많을수록 모든 경로를 탐색해야 할 수도 있음.

        # - Space Complexity: O(N × C)
        #
        # - 각 노드는:
        #   1) children 딕셔너리를 통해 자식 노드를 저장 (메모리 사용).
        #   2) is_end_of_word 변수 (Boolean 값, O(1)).
        # - Trie에 저장된 단어의 문자 수가 많을수록 메모리 사용량 증가.

class TrieNode:
    def __init__(self):
        self.children = {} #알파벳 a부터 z까지를 자식으로 가짐, 크기 26의 배열이나 딕셔너리를 사용.
        self.is_end_of_word = False #어떤 단어의 끝인지 나타내는 Boolean 값
        #예를 들어, "note"이라는 단어의 'e'에 해당하는 노드의 is_end_of_word가 True, 'n' 
        
class WordDictionary:
    def __init__(self):
        self.root = TrieNode() # WD로 생성된 인스턴스.root = TrieNode 인스턴스

    def addWord(self, word: str) -> None:
        node = self.root #node에 self.root를 부여 
        for char in word: # 매개변수 word를 하나씩 순회하며 char에 저장 (예: word="note" -> char="n", "o", "t", "e") 
            if char not in node.children: # 만약 char가 현재 노드의 자식 노드 목록에 없다면
                node.children[char] = TrieNode() 
                #node.children[char]을 TrideNode 인스턴스로 생성
                # self.root.children = {
						    # "n": TrieNode()  # "n" 키가 추가되고, 값으로 새로운 TrieNode 인스턴스가 들어감
								# }
								
								#Example1:
								#root
								#└── "n" (children={}, is_end_of_word=False)
								
								#Example2:
								#└── "n" (children={}, is_end_of_word=False)
								#      └── "o" (children={}, is_end_of_word=False)
            node = node.children[char] #node를 현 node의 children[char]로 이동 
            #Example1:
	          # node = node.children["n"]
  
						#Example2:
	          # node = node.children["o"]
        node.is_end_of_word = True 
        #After for loop, 끝 노드의 is_end_of_word를 True로 전환
        
        #Example 4:
        #root
				#└── "n"
				      #└── "o"
				            #└── "t"
				                  #└── "e" (children={}, is_end_of_word=True)

    def search(self, word: str) -> bool:
	       def dfs(index, node):  # DFS 함수 정의
            # 1) 종료 조건: 모든 문자를 탐색한 경우
                if index == len(word): 
                 return node.is_end_of_word # 단어 끝 여부 반환
            # 2) 현재 문자 처리
                char = word[index]
                if char == '.': # 2-1) 와일드카드인 경우
                    for child in node.children.values(): # 모든 자식 노드 탐색
                         if dfs(index + 1, child): #dfs를 재귀호출 하여 다음 노드로 탐색 재개 
                            return True #재귀 이후에 있으면 True
                    return False #없으면 False
                else: # 2-2) 일반 문자 처리
                    if char not in node.children: # 현재 문자가 자식 노드에 없는 경우 False
                        return False
                return dfs(index + 1, node.children[char]) # 다음 노드로 이동하여 탐색
        
                return dfs(0, self.root) 
                #1. def dfs를 self.root 위치에서 첫 호출. 
   


