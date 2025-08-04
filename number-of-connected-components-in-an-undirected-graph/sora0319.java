public class Solution {
    public int countComponents(int n, int[][] edges) {
        List<List<Integer>> graph = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            graph.add(new ArrayList<>());
        }
        for (int[] edge : edges) {
            int node = edge[0];
            int adj = edge[1];
            graph.get(node).add(adj);
            graph.get(adj).add(node);
        }

        int count = 0;
        Set<Integer> visited = new HashSet<>();
        for (int node = 0; node < n; node++) {
            if (visited.contains(node)) {
                continue;
            }
            count++;
            Deque<Integer> queue = new ArrayDeque<>();
            queue.push(node);
            while (!queue.isEmpty()) {
                int cur = queue.pop();
                if (visited.contains(cur)) continue;
                visited.add(cur);
                for (int g : graph.get(cur)) {
                    if (!visited.contains(g)) {
                        queue.push(g);
                    }
                }
            }
        }
        return count;
    }
}

