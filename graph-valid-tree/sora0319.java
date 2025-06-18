public class Solution {
    public boolean validTree(int n, int[][] edges) {
        Map<Integer, List<Integer>> graph = new HashMap<>();
        for (int i = 0; i < n; i++) {
            graph.put(i, new ArrayList<>());
        }

        for (int[] edge : edges) {
            int node = edge[0];
            int adj = edge[1];
            graph.get(node).add(adj);
            graph.get(adj).add(node);
        }

        Set<Integer> visited = new HashSet<>();
        if (inCycle(0, -1, graph, visited)) {
            return false;
        }

        return visited.size() == n;
    }

    private boolean inCycle(int node, int prev, Map<Integer, List<Integer>> graph, Set<Integer> visited) {
        if (visited.contains(node)) {
            return true;
        }

        visited.add(node);

        for (int neighbor : graph.get(node)) {
            if (neighbor == prev) continue;
            if (inCycle(neighbor, node, graph, visited)) {
                return true;
            }
        }

        return false;
    }
}

