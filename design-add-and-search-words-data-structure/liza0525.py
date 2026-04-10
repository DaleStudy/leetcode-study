# 7기 풀이

# 클래스 공간 복잡도: O(W * L)
#  - W는 word의 개수, L는 word의 평균 길이.

# addWord 메서드
# 시간 복잡도: O(L)
# - L는 word의 길이. word의 길이만큼 탐색하며 insert함
# 공간 복잡도: O(L)
# - L는 word의 길이. 길이만큼 재귀 스택이 쌓임

# search 메서드
# 시간 복잡도: O(W * L)
# - W는 이미 삽입된 단어의 개수, L는 word의 평균 길이.
# - 최악인 조건은 word의 모든 문자들이 '.'일 때
# 공간 복잡도: O(L)
# - L는 word의 길이. 길이만큼 재귀 스택이 쌓임


DELIMITER = "$"  # 끝맺음을 나타내는 DELIMITER로 "$"를 사용


class WordDictionary:
    def __init__(self):
        self.word_dict = {}

    def addWord(self, word: str) -> None:
        # 재귀를 이용해 단어를 각 문자별로 insert
        def _add_word(curr_dict, word):
            if not word:
                # 끝맺음을 나타내는 DELIMITER로 "$"를 사용
                curr_dict[DELIMITER] = {}
                return

            s = word[0]  # word의 첫번째 문자
            if s not in curr_dict:  # curr에 없는 경우에는 새로 key를 만든다.
                curr_dict[s] = {}

            # 다음 문자를 저장하기 위한 dictionary와
            # 해당 depth에서 확인한 문자를 제외한 나머지 문자열을 가지고 다음 작업 수행
            _add_word(curr_dict[s], word[1:])

        _add_word(self.word_dict, word)


    def search(self, word: str) -> bool:
        # 재귀를 이용해 단어를 각 문자별로 뎁스를 타고 내려가 search
        def _search(curr_dict, word): 
            if not word:
                # 더이상 검색할 문자열이 없을 땐
                # DELIMITER의 존재 여부를 보고 return
                return DELIMITER in curr_dict

            s = word[0]
            if s != '.' and s not in curr_dict:
                # 와일드 카드 문자가 아니면서, 찾으려는 문자가 dictionary에 없으면
                # insert가 된 적이 없는 단어이므로 False로 early return
                return False
            elif s == '.':
                # 와일드 카드 문자이면 curr_dict에 있는 모든 문자열을 가지고 다음 depth를 확인한다.
                for k in curr_dict.keys():
                    is_valid = _search(curr_dict[k], word[1:])
                    if is_valid:
                        # 하나라도 True라면 search 결과가 유효하기 때문에 
                        # True로 early return
                        return True
                # 모든 문자열을 탐색하고도 결과가 없다면 False return
                return False
            else:
                # 그 외의 경우는 일반 문자열 탐색을 해야 하므로
                # 자식 문자열이 있는 curr_dict[s]와
            # 해당 depth에서 확인한 문자를 제외한 나머지 문자열을 가지고 다음 작업 수행
                return _search(curr_dict[s], word[1:])

        return _search(self.word_dict, word)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)