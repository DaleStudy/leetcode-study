/**
 * <a href="https://leetcode.com/problems/word-break/">week05-4.word-break</a>
 * <li>Description: return true if s can be segmented into a space-separated sequence of one or more dictionary words.</li>
 * <li>Topics: Array, Hash Table, String, Dynamic Programming, Trie, Memoization</li>
 * <li>Time Complexity: O(N³), Runtime 7ms        </li>
 * <li>Space Complexity: O(N+W), Memory 44.59MB     </li>
 */
class Solution {
    public boolean wordBreak(String s, List<String> wordDict) {
        Trie trie = new Trie();
        for (String str : wordDict) {
            trie.insert(str);
        }

        List<Integer> dp = new ArrayList<>();
        dp.add(-1);
        for (int i = 0; i < s.length(); i++) {
            for (int j = dp.size() - 1; j >= 0; j--) {
                int startIndex = dp.get(j);
                if (trie.search(s.substring(startIndex + 1, i + 1))) {
                    dp.add(i);
                    break;
                }
            }
        }

        return dp.contains(s.length() - 1);
    }

    class Trie {
        private boolean end;
        private final Map<Character, Trie> children = new HashMap<>();

        public void insert(String word) {
            Trie node = this;
            for (Character c : word.toCharArray()) {
                node = node.children.computeIfAbsent(c, k -> new Trie());
            }
            node.end = true;
        }

        public boolean search(String word) {
            Trie node = this;
            for (Character c : word.toCharArray()) {
                node = node.children.get(c);
                if (node == null) {
                    return false;
                }
            }
            return node.end;
        }
    }
}
