/**
    Tries 자료구조를 구현하고, 이를 통해 단어를 탐색하는 방식
    visited[] 방문 배열을 추가하여, 이전에 방문했던 인덱스에 대해서는 무시
 */
class WordMap {
    public Map<Character, WordNode> wordMap;

    public WordMap() {
        wordMap = new HashMap<>();
    }

    public List<Integer> search(String word, int idx) {
        List<Integer> idxList = new ArrayList<>();

        WordNode wordNode = null;
        char ch = word.charAt(idx);
        wordNode = wordMap.get(ch);
        if (wordNode == null) return idxList;

        if(wordNode.isLeaf) {
            idxList.add(idx + 1);
        }
        idx++;

        for(; idx < word.length(); idx++) {
            char target = word.charAt(idx);
            if (!wordNode.next.containsKey(target)) {
                break;
            }
            wordNode = wordNode.next.get(target);
            if (wordNode.isLeaf) {
                idxList.add(idx + 1);  
            }
        }

        return idxList;
    }

    public void add(String word) {
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

class Solution {
    public static WordMap wordMap;
    public boolean wordBreak(String s, List<String> wordDict) {
        boolean[] visited = new boolean[s.length()];
        initWordMap(wordDict);
        if(s.length() == 1) return wordMap.wordMap.containsKey(s.charAt(0)) && wordMap.wordMap.get(s.charAt(0)).isLeaf;

        Queue<Integer> que = new LinkedList<>();
        boolean result = false;
        que.add(0);
        visited[0] = true;
        loop:
        while(!que.isEmpty()) {
            int idx = que.poll();
            List<Integer> idxList = wordMap.search(s, idx);
            for(int i : idxList) {
                if(i == s.length()) {
                    result = true;
                    break loop;
                }

                if(!visited[i]) {
                    que.add(i);
                    visited[i] = true;
                }
            }
        }

        return result;



    }
    
    public void initWordMap(List<String> wordDict) {
        wordMap = new WordMap();
        for(String word : wordDict) {
            wordMap.add(word);
        }
    }
}

