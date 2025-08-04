/**
 * trie는 효율적으로 데이터를 저장하고 키를 통해 문자열 데이터 셋을 검색할 수 있는 트리 구조이다.
 * 해당 구조를 활용해 자동완성이나 스펠링 체크를 만들 수 있다.
 trie 클래스는 다음과 같이 구현할 수 있다.
 Trie() 클래스 생성자
 void insert(String word) : trie로 문자열 word를 삽입
 boolean search(String word) : 문자열 word가 trie에 있다면 true를 반환
 boolean startsWith(String prefix) : prefix가 trie에 있다면 true를 반환
 */
class Trie {

    private Node root;

    public Trie() {
        root = new Node();
    }

    public void insert(String word) {
        Node current = root;
        for (char c : word.toCharArray()) {
            if (!current.getNodeCharacters().containsKey(c)) {
                current.getNodeCharacters().put(c, new Node());
            }
            current = current.getNodeCharacters().get(c);
        }
        current.setEnd();
    }

    public boolean search(String word) {
        Node current = root;
        for (char c : word.toCharArray()) {
            if (!current.getNodeCharacters().containsKey(c)) {
                return false;
            }
            current = current.getNodeCharacters().get(c);
        }
        return current.getEnd();
    }

    public boolean startsWith(String prefix) {
        Node current = root;
        for (char c : prefix.toCharArray()) {
            if (!current.getNodeCharacters().containsKey(c)) {
                return false;
            }
            current = current.getNodeCharacters().get(c);
        }
        return true;
    }

    static class Node {

        // 문자열 끝 여부
        private boolean isEnd;

        // 키 추출을 위한 맵 구조
        private Map<Character, Node> nodeCharacters;

        Node() {
            nodeCharacters = new HashMap<>();
            isEnd = false;
        }

        public boolean getEnd() {
            return this.isEnd;
        }

        public void setEnd() {
            this.isEnd = true;
        }

        public Map<Character, Node> getNodeCharacters() {
            return this.nodeCharacters;
        }

    }
}

/**
 * Your Trie object will be instantiated and called as such:
 * Trie obj = new Trie();
 * obj.insert(word);
 * boolean param_2 = obj.search(word);
 * boolean param_3 = obj.startsWith(prefix);
 */

