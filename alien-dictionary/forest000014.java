/*
# Time Complexity: O(wl)
  - w은 words의 길이, l은 words[i]의 길이
  - word 하나를 trie에 등록하는 과정 O(l)
  - 모든 word를 trie에 등록하는 과정 O(wl)
  - graph를 순회하면서 위상정렬하는 과정 O(26^2) = O(1)
# Space Complexity: O(wl)
  - trie의 공간복잡도 O(wl)
*/

class Solution {

    private class TrieNode {
        char ch;
        boolean ends;
        List<TrieNode> children;

        TrieNode(char ch) {
            this.ch = ch;
            children = new ArrayList<>();
        }
    }

    public String alienOrder(String[] words) {
        List<List<Integer>> graph = new ArrayList<>();
        for (int i = 0; i < 26; i++) {
            graph.add(new ArrayList<>());
        }
        boolean[] visited = new boolean[26];
        int[] inDegree = new int[26];
        int[] outDegree = new int[26];
        Queue<Character> queue = new LinkedList<>();

        TrieNode root = new TrieNode('.');

        for (int i = 0; i < words.length; i++) {
            TrieNode curr = root;

            for (int j = 0; j < words[i].length(); j++) {
                // 유효한 순서가 아님이 확실하면, 곧바로 false를 리턴한다.
                // 유효한 순서가 아님이 확실하지 않으면, trie에 추가하고, relation을 추가한다.
                // 단, words[i]의 마지막 글자라면, trie의 마지막에 ends = true를 세팅한다.

                char ch = words[i].charAt(j);
                visited[ch - 'a'] = true;

                if (curr.children.size() == 0) {
                    curr.children.add(new TrieNode(ch));
                    curr = curr.children.get(curr.children.size() - 1);
                    if (j == words[i].length()) curr.ends = true;
                    continue;
                }

                char lastCh = curr.children.get(curr.children.size() - 1).ch;
                if (lastCh == ch) {
                    curr = curr.children.get(curr.children.size() - 1);
                    if (j == words[i].length() - 1) {
                        if (!curr.children.isEmpty()) return "";
                        else curr.ends = true;
                    }
                    continue;
                }

                for (int p = 0; p < curr.children.size() - 1; p++) {
                    if (curr.children.get(p).ch == ch) return "";
                }

                addEdge(graph, inDegree, outDegree, lastCh, ch);
                curr.children.add(new TrieNode(ch));
                curr = curr.children.get(curr.children.size() - 1);
            }
        }

        for (int i = 0; i < 26; i++) {
            if (inDegree[i] == 0 && outDegree[i] != 0) queue.offer((char)('a' + i));
        }

        StringBuilder sb = new StringBuilder();

        for (int i = 0; i < 26; i++) {
            if (visited[i] && inDegree[i] == 0 && outDegree[i] == 0) sb.append((char)('a' + i));
        }

        while (!queue.isEmpty()) {
            char ch = queue.poll();
            sb.append(ch);

            for (int next : graph.get(ch - 'a')) {
                if (--inDegree[next] == 0) queue.offer((char)('a' + next));
            }
        }

        for (int i = 0; i < 26; i++) {
            if (inDegree[i] > 0) return "";
        }

        return sb.toString();
    }

    private boolean addEdge(List<List<Integer>> graph, int[] inDegree, int[] outDegree, char from, char to) {
        int sz = graph.get(from - 'a').size();
        for (int i = 0; i < sz; i++) {
            if (graph.get(from - 'a').get(i) == to - 'a') return false;
        }

        graph.get(from - 'a').add(to - 'a');
        outDegree[from - 'a']++;
        inDegree[to - 'a']++;
        return true;
    }
}
