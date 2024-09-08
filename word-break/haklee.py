"""TC: O(n * l * log(l)), SC: O(n * l)

쪼개고자 하는 단어의 길이 s, wordDict에 들어가는 단어 개수 w, wordDict에 들어가는 단어 최대 길이 l

아이디어:
- trie를 구현하는 문제에서 만든 클래스를 여기서 한 번 사용해보자.
- 주어진 단어들을 전부 trie에 집어넣는다.
- 쪼개려고 하는 단어를 trie를 통해서 매칭한다. (`Trie` 클래스의 `find_prefix_indices` 메소드)
    - 단어를 앞에서부터 한 글자씩 매칭하면서
        - 중간에 end가 있는 노드를 만나면 `prefix_indices`에 값을 추가한다. "이 단어는 이 index
          에서 쪼개질 수 있어요!" 하는 의미를 담은 index라고 보면 된다.
        - 글자 매칭이 실패하면 매칭 종료.
    - 매칭이 끝나고 나서 `prefix_indices`를 리턴한다.
    - e.g.) wordDict = ["leet", "le", "code"], s = "leetcode"일때
        - 첫 글자 l 매칭. 아무 일도 일어나지 않음.
        - 다음 글자 e 매칭. 이 노드는 end가 true다. "le"에 대응되기 때문. prefix_indices에 2 추가.
        - 다음 글자 e 매칭. 아무 일도 일어나지 않음.
        - 다음 글자 t 매칭. 이 노드는 "leet"에 대응되어 end가 true다. prefix_indices에 4 추가.
        - 다음 글자 c 매칭. 매칭 실패 후 종료.
        - prefix_indices = [2, 4]를 리턴.
- 위의 매칭 과정이 끝나면 주어진 단어를 쪼갤 수 있는 방법들이 생긴다.
    - 쪼개진 단어에서 뒷 부분을 취한다.
    - e.g.) wordDict = ["leet", "le", "code"], s = "leetcode", prefix_indices = [2, 4]
        - prefix_indices의 각 아이템을 돌면서
            - s[2:]를 통해서 "le/etcode" 중 뒷 부분 "etcode"를 취할 수 있다.
            - s[4:]를 통해서 "leet/code" 중 뒷 부분 "code"를 취할 수 있다.
    - 만약 뒷 부분이 빈 문자열("")이 될 경우 탐색에 성공한 것이다.
        - 코드 상에서는 빈 문자열로 탐색을 시도할 경우 탐색 성공의 의미로 true 반환.
    - 만약 prefix_indices가 빈 리스트로 온다면 쪼갤 수 있는 방법이 없다는 뜻이므로 탐색 실패다.
    - 그 외에는 취한 뒷 부분들에 대해 각각 다시 쪼개는 것을 시도한다.
- 위의 과정에서 쪼개는 것을 이미 실패한 단어를 fail_list라는 set으로 관리하여 중복 연산을 막는다.
    - 즉, memoization을 활용.

SC:
- trie 생성. 최악의 경우 O(w * l)
- fail list에 들어갈 수 있는 단어 길이
    - 1, 2, ..., s
    - O(s^2)
    - 이걸 전체 단어를 저장하는 것 대신 맨 앞 글자의 index를 저장하는 식으로 구현하면 O(s)가 될 것이다.
      여기에서는 구현 생략.
- find함수의 호출 스택 최악의 경우 한 글자씩 앞에서 빼면서 탐색 시도, O(s)
- 종합하면 O(w * l) + O(s^2) + O(s) = O(w * l + s^2)

TC:
- ???
"""


class Trie:
    def __init__(self):
        self.next: dict[str, Trie] = {}
        self.end: bool = False

    def insert(self, word: str) -> None:
        cur = self

        for c in word:
            cur.next[c] = cur.next.get(c, Trie())
            cur = cur.next[c]

        cur.end = True

    def find_prefix_indices(self, word: str) -> list[str]:
        prefix_indices = []
        ind = 0
        cur = self

        for c in word:
            ind += 1
            if c not in cur.next:
                break
            cur = cur.next[c]
            if cur.end:
                prefix_indices.append(ind)

        return prefix_indices


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # init
        trie = Trie()
        for word in wordDict:
            trie.insert(word)

        fail_list = set()

        # recursive find
        def find(word: str) -> bool:
            # 단어의 앞에서 쪼갤 수 있는 경우를 전부 찾아서 쪼개고
            # 뒤에 남은 단어를 다시 쪼개는 것을 반복한다.
            if word == "":
                return True

            if word in fail_list:
                return False

            cut_indices = trie.find_prefix_indices(word)
            result = any([find(word[i:]) for i in cut_indices])
            if not result:
                fail_list.add(word)

            return result

        return find(s)
