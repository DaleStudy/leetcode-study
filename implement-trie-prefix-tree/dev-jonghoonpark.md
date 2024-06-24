- https://leetcode.com/problems/implement-trie-prefix-tree/
- https://algorithm.jonghoonpark.com/2024/06/23/leetcode-208

## TC, SC

insert, search, startsWith 메소드의 경우 입력된 문자열의 길이를 n 이라 하였을 때 시간 복잡도는 `O(n)`이다. 공간 복잡도는 `insert된 문자열의 갯수` 를 `N` 이라 하고 `insert된 문자열의 길이의 평균` 를 `L`이라고 하였을 때 `O(N * L * 26)`이다. 26은 계수이기 때문에 생략할 수 있다.

## 풀이

```java
class Trie {

    Node root = new Node();

    public Trie() {

    }

    public void insert(String word) {
        Node currentNode = root;
        for(char c : word.toCharArray()) {
            if(currentNode.nodes[c - 97] == null) {
                currentNode.nodes[c - 97] = new Node();
            }
            currentNode = currentNode.nodes[c - 97];
        }
        currentNode.val = word;
    }

    public boolean search(String word) {
        Node currentNode = root;
        for(char c : word.toCharArray()) {
            if(currentNode.nodes[c - 97] == null) {
                return false;
            }
            currentNode = currentNode.nodes[c - 97];
        }

        return currentNode.val != null && currentNode.val.equals(word);
    }

    public boolean startsWith(String prefix) {
        Node currentNode = root;
        for(char c : prefix.toCharArray()) {
            if(currentNode.nodes[c - 97] == null) {
                return false;
            }
            currentNode = currentNode.nodes[c - 97];
        }
        return true;
    }
}

class Node {
    String val;
    Node[] nodes = new Node[26];
}
```
