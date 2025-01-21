// GPT가 거의 풀어준 Trie를 이용한 풀이. 알파벳의 존재 여부를 26개의 노드에 저장한다.
// 다음 노드를 찾아가는 방식은 재귀적으로 구성된다. 단어의 끝은 endOfWord로 관리됨.
// 혼자서는 절대 못 풀었을 문제
class WordDictionary {
    private TrieNode root;

    private static class TrieNode {
        private TrieNode[] children;
        private boolean isEndOfWord;

        public TrieNode() {
            this.children = new TrieNode[26];
            this.isEndOfWord = false;
        }
    }

    public WordDictionary() {
        root = new TrieNode();
    }

    public void addWord(String word) {
        TrieNode current = root;
        for (char ch : word.toCharArray()) {
            int index = ch - 'a';
            if (current.children[index] == null) {
                current.children[index] = new TrieNode();
            }
            current = current.children[index];
        }
        current.isEndOfWord = true;
    }

    public boolean search(String word) {
        return searchInNode(word, root, 0);
    }

    private boolean searchInNode(String word, TrieNode node, int index) {
        if (index == word.length()) {
            return node.isEndOfWord;
        }

        char ch = word.charAt(index);
        if (ch == '.') {
            for (TrieNode child : node.children) {
                if (child != null && searchInNode(word, child, index + 1)) {
                    return true;
                }
            }
            return false;
        } else {
            int charIndex = ch - 'a';
            TrieNode child = node.children[charIndex];
            if (child == null) {
                return false;
            }
            return searchInNode(word, child, index + 1);
        }
    }
}

// 내가 생각한 첫번째 풀이. 정규표현식을 이용하면 될거라 생각했는데..
class WordDictionary {
    private List<String> words;

    public WordDictionary() {
        words = new ArrayList<>();
    }

    public void addWord(String word) {
        words.add(word);
    }

    public boolean search(String word) {
        String regex = word.replace(".", "[a-z]");
        for (String w : words) {
            if (w.matches(regex)) {
                return true;
            }
        }
        return false;
    }
}
