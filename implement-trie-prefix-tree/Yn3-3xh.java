/**
[문제풀이]
- Node를 만들자
time: O(N), space: O(N)

[회고]
노드를 만드는 접근은 맞았는데, 그 뒤로 안풀려서 해설을 보니 노드의 길이를 26으로 한다.
이 부분에서 이해하기가 어려웠는데 아래를 보고 이해됐다.
(root)
 ├── c
 │   ├── a
 │   │   ├── t (end)
 │   │   └── r (end)
 └── d
     └── o
         └── g (end)

주어진 문자열을 핸들링하는 역할은 노드가 가지도록 노드 안에 솔루션을 구현했다.
 */
class Trie {
    Node root;

    public Trie() {
        root = new Node();
    }
    
    public void insert(String word) {
        root.insert(word);
    }
    
    public boolean search(String word) {
        return root.search(word);
    }
    
    public boolean startsWith(String prefix) {
        return root.startsWith(prefix);
    }
}

class Node {
    Node[] nodes;
    boolean isEnd;

    Node() {
        nodes = new Node[26];
    }

    void insert(String word) {
        Node current = this;
        for (char ch : word.toCharArray()) {
            int index = ch - 'a';
            if (current.nodes[index] == null) {
                current.nodes[index] = new Node();
            }
            current = current.nodes[index];
        }
        current.isEnd = true;
    }

    boolean search(String word) {
        Node current = this;
        for (char ch : word.toCharArray()) {
            int index = ch - 'a';
            if (current.nodes[index] == null) {
                return false;
            }
            current = current.nodes[index];
        }

        if (current.isEnd) {
            return true;
        }
        return false;
    }

    boolean startsWith(String prefix) {
        Node current = this;
        for (char ch : prefix.toCharArray()) {
            int index = ch - 'a';
            if (current.nodes[index] == null) {
                return false;
            }
            current = current.nodes[index];
        }
        return true;
    }
}

/**
 * Your Trie object will be instantiated and called as such:
 * Trie obj = new Trie();
 * obj.insert(word);
 * boolean param_2 = obj.search(word);
 * boolean param_3 = obj.startsWith(prefix);
 */

