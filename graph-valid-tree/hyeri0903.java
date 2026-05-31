public class Solution {
    /**
     * @param n: An integer
     * @param edges: a list of undirected edges
     * @return: true if it's a valid tree, or false
     */
    public boolean validTree(int n, int[][] edges) {
        /**
        1. n개의 노드 valid tree 검사
        2. constraints
        - no cycle
        - all nodes are connected
        3. Solution: DFS
        - 간선 개수 체크
        - 그래프 만들어서 cycle 없고 && 모두 방문했는지 체크
        너모 어려워요...
        */

        //간선 개수 체크
        if(edges.length != n-1) {
            return false;
        }

        //그래프 만들기
        List<List<Integer>> graph = new ArrayList<>();

        for(int i = 0; i < n; i++) {
            graph.add(new ArrayList<>());
        }
        for(int[] edge: edges) {
            int a = edge[0];
            int b = edge[1];
            graph.get(a).add(b);
            graph.get(b).add(a);
        }
        //check through DFS
        Set<Integer> visited = new HashSet<>();

        if(hasCycle(0, -1, graph, visited)) {
            return false;
        }
        if(visited.size() != n) {
            return false;
        }
        return true;
    }
    private boolean hasCycle(int node, int parent, List<List<Integer>> graph, Set<Integer> visited) {
        //이미 방문했으면 cycle
        if(visited.contains(node)) {
            return true;
        }
        visited.add(node);
        for(int neighbor: graph.get(node)) {
            if(neighbor == parent) {
                continue;
            }
            if(hasCycle(neighbor, node, graph, visited)) {
                return true;
            }
        }
        return false;
    }
}
