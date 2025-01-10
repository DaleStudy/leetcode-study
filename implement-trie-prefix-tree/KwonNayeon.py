"""
Constraints:
1. 1 <= word.length, prefix.length <= 2000
2. word and prefix consist only of lowercase English letters.
3. At most 3 * 10^4 calls in total will be made to insert, search, and startsWith.

Time Complexity: 
- 

Space Complexity: 
- 

이해한 내용:
1. Prefix(접두사)의 의미
  - 문법적 접두사(un-, pre- 등)가 아님, 단순히 단어의 앞부분에 있는 문자열을 의미
  - 예: "apple"의 접두사 -> "a", "ap", "app", "appl", "apple"

2. 실행 방식
  - 입력으로 주어진 명령어를 순차적으로 실행
  - 예: ["Trie", "insert", "search"] 순서대로 실행
  - 각 명령어에 해당하는 인자값도 순서대로 적용

3. 자료구조 선택
  - Trie의 각 노드에서 자식 노드를 저장할 때 해시 테이블 사용
  - 키: 다음 문자, 값: 해당 문자의 TrieNode
  - 장점: 다음 문자 검색이 O(1)로 가능
"""
