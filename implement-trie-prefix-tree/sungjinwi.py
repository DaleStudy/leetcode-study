"""
	풀이 : 딕셔너리를 통해 트리구현
		- 생성자 함수는 맨 처음 노드를 만드는 역할, search("")를 위해 "ending":True로 초기화
        - insert함수를 수행하면 노드는 다음 문자에 대해서도 각각 노드를 가지고 있음
            ex) insert("a"); insert("b")
            {
                "ending":True,
				"a" :{"ending":True},
                "b" :{"ending":True}
            }
		- insert(): word의 순서대로 다음 문자의 노드(존재하지 않으면 {"ending":False}로 초기화)로 이동함
			for문 끝난 후 마지막 문자에서는 해당 노드로 끝나는 단어가 있다는 의미로 "ending":True로 수정
        
        - search(): word 다음 문자의 노드로 이동하면서 존재하지 않으면 return False
			문자의 끝에 도달하면 끝나는 단어가 있는지 node["ending"] return
            
		- startsWith(): prefix 다음 문자의 노드로 이동하면서 존재하지 않으면 return False
			문자의 끝에 도달하면 return True

    TC : O(N)
        단어의 길이(N)에 비례한다
    SC : O(N)
        insert할 단어의 길이(N)에 비례해서 노드가 생성된다

    - 딕셔너리가 아닌 class로 풀이할 수도 있다
"""

class Trie:

    def __init__(self):
        self.root = {"ending":True}

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node:
                node[char] = {"ending": False}
            node = node[char]
        node["ending"] = True

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char in node:
                node = node[char]
            else:
                return False
        return node["ending"]
        

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if char in node:
                node = node[char]
            else:
                return False
        return True    


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
