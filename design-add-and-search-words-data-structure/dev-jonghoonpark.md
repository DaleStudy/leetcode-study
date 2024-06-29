- https://leetcode.com/problems/design-add-and-search-words-data-structure
- https://algorithm.jonghoonpark.com/2024/06/30/leetcode-211

## brute force

아슬아슬하게 통과한다.

```java
class WordDictionary {

    Set<String> wordSet;

    public WordDictionary() {
        wordSet = new HashSet<>();
    }

    public void addWord(String word) {
        wordSet.add(word);
    }

    public boolean search(String word) {
        Deque<String> queue = new ArrayDeque<>();
        queue.push(word);

        while (queue.getFirst().contains(".")) {
            String _word = queue.removeFirst();
            String pre = _word.substring(0, _word.indexOf("."));
            String post = _word.substring(_word.indexOf(".") + 1);

            for (char c = 'a'; c <= 'z'; c++) {
                queue.addLast(pre + c + post);
            }
        }

        while (!queue.isEmpty()) {
            String _word = queue.removeFirst();
            if (wordSet.contains(_word)) {
                return true;
            }
        }

        return false;
    }
}
```

### TC, SC

- `.` 이 없을 때
  - 시간 복잡도 : `O(1)`
  - 공간 복잡도 : `O(1)`
- `.` 이 있을 때
  - 시간 복잡도 : `O(26^N)`
  - 공간 복잡도 : `O(26^N)`
  - 여기서 N은 `.` 의 수

## trie

[208. Implement Trie (Prefix Tree)](https://leetcode.com/problems/implement-trie-prefix-tree/) 문제 에서 사용한 Trie 재사용.

```java
class WordDictionary {

    Trie trie; // Trie 구현은 생략

    public WordDictionary() {
        trie = new Trie();
    }

    public void addWord(String word) {
        trie.insert(word);
    }

    public boolean search(String word) {
        if (word.contains(".")) {
            String pre = word.substring(0, word.indexOf("."));
            String post = word.substring(word.indexOf(".") + 1);

            if (trie.startsWith(pre)) {
                for (char c = 'a'; c <= 'z'; c++) {
                    if (search(pre + c + post)) {
                        return true;
                    }
                }
            }

            return false;
        }

        return trie.search(word);
    }


}
```

### TC, SC

입력된 문자열의 길이를 `L`, `.` 의 수를 `N` 이라고 하였을 때

addWord 메소드의 경우 시간 복잡도는 `O(L)`이다.
search 메소드의 경우 입력된 문자열의 길이를 n 이라 하였을 때 시간 복잡도는 `O(L * 26 ^ N)`이다.

공간 복잡도는 Trie 구조를 만드는데 사용된 공간이다. `insert된 문자열 길이의 평균` 를 `avg(L)`이라고 하였을 때 `O(avg(L) * 26)`이다. 26은 계수이기 때문에 생략할 수 있다.

## trie 개선

이 문제에 적합하도록 search를 수정하였다.

```java
class WordDictionary {

    Trie trie;

    public WordDictionary() {
        trie = new Trie();
    }

    public void addWord(String word) {
        trie.insert(word);
    }

    public boolean search(String word) {
        return trie.search(word);
    }


}

class Trie {

    Node root = new Node();

    public Trie() {

    }

    public void insert(String word) {
        Node currentNode = root;
        for (char c : word.toCharArray()) {
            if (currentNode.nodes[c - 97] == null) {
                currentNode.nodes[c - 97] = new Node();
            }
            currentNode = currentNode.nodes[c - 97];
        }
        currentNode.val = word;
    }

    public boolean search(String word) {
        return search(root, word, 0);
    }

    public boolean search(Node node, String word, int index) {
        if (node == null) {
            return false;
        }

        if (node.val != null && node.val.length() == word.length()) {
            return true;
        }

        if (index >= word.length()) {
            return false;
        }

        char c = word.charAt(index);

        if (c == '.') {
            for (char _c = 'a'; _c <= 'z'; _c++) {
                if (search(node.nodes[_c - 97], word, index + 1)) {
                    return true;
                }
            }
            return false;
        } else if (node.nodes[c - 97] == null) {
            return false;
        }

        return search(node.nodes[c - 97], word, index + 1);
    }
}

class Node {
    String val;
    Node[] nodes = new Node[26];
}
```

### TC, SC

입력된 문자열의 길이를 `L`, `.` 의 수를 `N` 이라고 하였을 때

addWord 메소드의 경우 시간 복잡도는 `O(L)`이다.
search 메소드의 경우 입력된 문자열의 길이를 n 이라 하였을 때 시간 복잡도는 `O(L * 26 ^ N)`이다.
개선 전과 비교해봤을 때 표기상으로는 차이가 없으나, 불필요한 과정을 제거하게되어서 시간이 매우 단축된다.
(`trie.startsWith(pre)`이 사라졌고, search의 호출 횟수가 줄어듬.)

공간 복잡도는 Trie 구조를 만드는데 사용된 공간이다. `insert된 문자열 길이의 평균` 를 `avg(L)`이라고 하였을 때 `O(avg(L) * 26)`이다. 26은 계수이기 때문에 생략할 수 있다.
