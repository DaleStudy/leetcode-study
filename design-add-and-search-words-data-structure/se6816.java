/**
	Tries + BFS를 활용한 방식
	addWord()
	문자열 word의 길이 -> N
	시간 복잡도 : O(N) 
	공간 복잡도 : O(N)
	search()
	Tries 내부의 노드 개수 -> M
	시간 복잡도 : O(M)
	공간 복잡도 : O(M)
*/
class WordDictionary {
    public Map<Character, WordNode> wordMap;

    public WordDictionary() {
        wordMap = new HashMap<>();
    }
    
    public void addWord(String word) {
        WordNode wordNode = null;
        char ch = word.charAt(0);
        wordNode = wordMap.get(ch);

        if(wordNode == null) {
            boolean isFirstWord = word.length() == 1;
            wordNode = new WordNode(ch, isFirstWord);
            wordMap.put(ch, wordNode);
        }

        for(int idx = 1; idx < word.length(); idx++) {
            char target = word.charAt(idx);
            boolean isLeaf = word.length() - 1 == idx;
            wordNode = wordNode.next.computeIfAbsent(target, key -> new WordNode(key, isLeaf));
        }
        wordNode.isLeaf = true;
        
        
    }
    
    public boolean search(String word) {
        Queue<Node> que = new ArrayDeque<>();
        boolean result = false;
        char ch = word.charAt(0);
        WordNode wordNode = wordMap.get(ch);
        int len = word.length();

        if(ch == '.' && wordMap.size() != 0) {
            for(Map.Entry<Character, WordNode> entry : wordMap.entrySet()) {
                que.add(new Node(entry.getValue(), 1));
            }
        }

        if (wordNode != null) {
            que.add(new Node(wordNode, 1));
        }



        while(!que.isEmpty()) {
            Node node = que.poll();
            if(node.idx == len && node.wordNode.isLeaf) {
                result = true;
                break;
            }

            if(node.idx == len) {
                continue;
            }

            char target = word.charAt(node.idx);

            if(target == '.' && node.wordNode.next.size() != 0) {
                for(Map.Entry<Character, WordNode> entry : node.wordNode.next.entrySet()) {
                    que.add(new Node(entry.getValue(), node.idx + 1));
                }
                continue;
            }


            if (!node.wordNode.next.containsKey(target)) {
                continue;
            }

            que.add(new Node(node.wordNode.next.get(target), node.idx + 1));
        }

        return result;
        
    }
}

class Node {
    WordNode wordNode;
    int idx;
    public Node(WordNode wordNode, int idx) {
        this.wordNode = wordNode;
        this.idx = idx;
    }
}

class WordNode {
    char ch;
    Map<Character, WordNode> next;
    boolean isLeaf;

    public WordNode(char ch) {
        this(ch, false);
    }
    
    public WordNode(char ch, boolean isLeaf) {
        next = new HashMap<>();
        this.ch = ch;
        this.isLeaf = isLeaf;
    }

}
