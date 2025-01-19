/**
 * @problem
 * Trie를 구현합니다.
 * - 메모리 사용량을 최적화하면서 정확한 검색 결과를 보장해야 합니다.
 * 
 * @constraints
 * - word와 prefix의 길이는 최소 1, 최대 2000입니다.
 * - word와 prefix는 소문자 영어 알파벳(a-z)만으로 구성됩니다.
 * - insert, search, startsWith 함수 호출은 총 30,000번을 넘지 않습니다.
 * 
 * @example
 * const trie = new Trie();
 * trie.insert("apple");   // undefined
 * trie.search("apple");   // true
 * trie.search("app");     // false
 * trie.startsWith("app"); // true
 * trie.insert("app");     // undefined
 * trie.search("app");     // true
 * 
 * @complexity
 * - 시간복잡도:
 *   ㄴ insert: O(m) (m은 단어 길이)
 *   ㄴ search: O(m) (m은 단어 길이)
 *   ㄴ startsWith: O(m) (m은 접두사 길이)
 * - 공간복잡도: O(ALPHABET_SIZE * m * n)
 *   ㄴ ALPHABET_SIZE: 문자열의 알파벳 수 (영문의 경우 26)
 *   ㄴ m: 단어의 평균 길이
 */ 
class TrieNode {
    constructor() {
        // 각 문자를 키로 하고 자식 노드를 값으로 하는 객체
        this.children = {};
        // 현재 노드가 단어의 마지막 문자인지 표시하는 플래그
        this.isEndOfWord = false;
    }
}

class Trie {
    constructor() {
        // 빈 문자열을 나타내는 루트 노드 생성
        this.root = new TrieNode();
    }

    /**
     * 단어를 Trie에 삽입하는 메서드
     * @param {string} word - 삽입할 단어
     */
    insert(word) {
        // 루트 노드부터 시작
        let node = this.root;
        
        // 단어의 각 문자를 순회
        for (let i = 0; i < word.length; i++) {
            const char = word[i];
            // 현재 문자에 대한 노드가 없으면 새로 생성
            if (!(char in node.children)) {
                node.children[char] = new TrieNode();
            }
            // 다음 문자를 처리하기 위해 자식 노드로 이동
            node = node.children[char];
        }
        // 단어의 마지막 문자임을 표시
        node.isEndOfWord = true;
    }


    /**
     * 정확한 단어가 존재하는지 검색하는 메서드
     * @param {string} word - 검색할 단어
     * @returns {boolean} - 단어 존재 여부
     */
    search(word) {
        // 단어를 찾아 마지막 노드를 반환
        const node = this._traverse(word);
        // 단어가 존재하고 해당 노드가 단어의 끝인 경우에만 true 반환
        return node !== null && node.isEndOfWord;
    }

    /**
     * 주어진 접두사로 시작하는 단어가 존재하는지 검색하는 메서드
     * @param {string} prefix - 검색할 접두사
     * @returns {boolean} - 접두사로 시작하는 단어 존재 여부
     */
    startsWith(prefix) {
        // 접두사에 해당하는 노드가 존재하는지만 확인
        return this._traverse(prefix) !== null;
    }

    /**
     * 문자열을 따라가며 마지막 노드를 반환하는 내부 헬퍼 메서드
     * @param {string} str - 탐색할 문자열
     * @returns {TrieNode|null} - 마지막 문자에 해당하는 노드 또는 null
     * @private
     */
    _traverse(str) {
        // 루트 노드부터 시작
        let node = this.root;
        
        // 문자열의 각 문자를 순회
        for (let i = 0; i < str.length; i++) {
            const char = str[i];
            // 현재 문자에 대한 노드가 없으면 null 반환
            if (!(char in node.children)) {
                return null;
            }
            // 다음 문자를 처리하기 위해 자식 노드로 이동
            node = node.children[char];
        }
        // 마지막 노드 반환
        return node;
    }
}

const trie = new Trie();
console.log(trie.insert("apple"));   // undefined
console.log(trie.search("apple"));   // true
console.log(trie.search("app"));     // false
console.log(trie.startsWith("app")); // true
console.log(trie.insert("app"));     // undefined
console.log(trie.search("app"));     // true
