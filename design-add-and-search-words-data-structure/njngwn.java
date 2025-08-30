class WordDictionary {
    private static class CharDictionary {
        HashMap<Character, CharDictionary> charMap;
        boolean isEnd;

        private CharDictionary() {
            this.charMap = new HashMap<>();
            this.isEnd = false;
        }
    }

    private CharDictionary rootNode;

    public WordDictionary() {
        this.rootNode = new CharDictionary();
    }

    public void addWord(String word) {
        CharDictionary currentNode = this.rootNode;

        for (char ch : word.toCharArray()) {
            if (!currentNode.charMap.containsKey(ch)) {
                currentNode.charMap.put(ch, new CharDictionary());
            }
            currentNode = currentNode.charMap.get(ch);
        }
        currentNode.isEnd = true;
    }

    public boolean search(String word) {
        return searchRecursive(word, this.rootNode, 0);
    }

    private boolean searchRecursive(String word, CharDictionary node, int index) {
        // Base case
        if (index == word.length()) {
            return node.isEnd;
        }

        char ch = word.charAt(index);

        if (ch == '.') {
            for (CharDictionary childNode : node.charMap.values()) {
                if (searchRecursive(word, childNode, index + 1)) {
                    return true;
                }
            }
            return false;
        } else {
            if (!node.charMap.containsKey(ch)) {
                return false;
            }
            return searchRecursive(word, node.charMap.get(ch), index + 1);
        }
    }
}

/**
 * Your WordDictionary object will be instantiated and called as such:
 * WordDictionary obj = new WordDictionary();
 * obj.addWord(word);
 * boolean param_2 = obj.search(word);
 */
