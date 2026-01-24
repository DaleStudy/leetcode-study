class Solution {
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        int[] inDegree = new int[numCourses];
        Deque<Integer> queue = new ArrayDeque<>();
        int visitCount = 0;

        List<List<Integer>> graph = new ArrayList<>();
        for (int i = 0; i < numCourses; i++) {
            graph.add(new ArrayList<>());
        }

        for (int[] node: prerequisites) {
            int toNode = node[0];
            int fromNode = node[1];
            graph.get(fromNode).add(toNode);
        }

        for (List<Integer> neighbor: graph) {
            for (int node: neighbor){
                inDegree[node] ++;
            }
        }

        for (int i = 0; i < numCourses; i++) {
            if (inDegree[i] == 0) queue.add(i);
        }

        while (!queue.isEmpty()) {
            int curNode = queue.poll();
            visitCount += 1;

            for (int node: graph.get(curNode)) {
                inDegree[node] -= 1;
                if (inDegree[node] == 0) {
                    queue.add(node);
                }
            }
        }
        return visitCount == numCourses;
    }
}


