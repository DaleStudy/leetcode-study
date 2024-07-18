// time: O(N^2)
// space: O(N)
class Solution {

    public boolean wordBreak(String s, List<String> wordDict) {
        Set<String> words = new HashSet<>(wordDict);
        Queue<Integer> que = new LinkedList<>();
        boolean[] visited = new boolean[s.length() + 1];
        que.add(0);

        while (!que.isEmpty()) {
            int start = que.remove();
            if (start == s.length()) {
                return true;
            }

            for (int i = start + 1; i <= s.length(); i++) {
                if (visited[i]) {
                    continue;
                }

                if (words.contains(s.substring(start, i))) {
                    que.add(i);
                    visited[i] = true;
                }
            }
        }

        return false;
    }
}
