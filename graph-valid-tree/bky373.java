/*
    time: O(n + m), where n is the number of nodes and m is the number of edges in the graph.
    space: O(n + m)
 */
class Solution {

    public boolean validTree(int n, int[][] edges) {

        if (edges.length != n - 1) {
            return false;
        }

        List<List<Integer>> adjList = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            adjList.add(new ArrayList<>());
        }
        for (int[] edge : edges) {
            adjList.get(edge[0])
                   .add(edge[1]);
            adjList.get(edge[1])
                   .add(edge[0]);
        }

        Stack<Integer> stack = new Stack<>();
        Set<Integer> visited = new HashSet<>();
        stack.push(0);
        visited.add(0);

        while (!stack.isEmpty()) {
            int curr = stack.pop();
            for (int adj : adjList.get(curr)) {
                if (visited.contains(adj)) {
                    continue;
                }
                visited.add(adj);
                stack.push(adj);
            }
        }

        return visited.size() == n;
    }
}
