/*
# Time Complexity: O(n * e), where e is the maximum number of edges of a node
  - 전체 node를 순회하면서, 그 이웃에 해당하는 복제본을 생성해서 복제본끼리 연결해준다.
  - 단, 중복 방문을 막기 위해, 복제본이 이미 이웃 복제본을 가지고 있는지 확인한다. 이 과정에서 O(e)만큼의 List 순회를 한다.

# Space Complexity: O(n)
  - 전체 Node 만큼의 메모리가 필요하다.
(Space Complexity를 계산하기 애매한 측면이 있네요. 저는 지금까지 출력은 space complexity에 포함하지 않고 계산했었는데, 그 이유는 "어떤 알고리즘을 구현하든 출력은 동일하기 때문"인데요. 이 문제의 경우에 출력은 Node 하나이지만, 실제로는 Node 전체만큼의 메모리를 반드시 생성해야 한다는 특수성이 있습니다. 그래서 "어떻게 구현하든 동일하게 사용해야만 하는 메모리는 Space Complexity에서 배제한다" 라는 논리로만 보자면 O(1)일 것 같고, "출력을 제외한 메모리 사용은 Space Complexity에 포함한다" 라는 논리대로라면 O(n)인 것 같습니다.)


전체 노드를 DFS로 순회하면서 이웃 노드의 복제본을 생성하여 현재 노드의 복제본과 연결을 맺어줍니다.
다만, 중복 방문을 막기 위해, 복제본이 이미 이웃 복제본을 가지고 있는지 확인한다.
또한 순환 참조(cycle 구조)를 막기 위해서, 복제본 노드를 생성시 단순히 new 키워드를 사용하지 않고, 별도의 map을 통해 싱글톤으로 생성한다. (각 노드의 val은 distinct하다는 점을 이용)


// Definition for a Node.
class Node {
    public int val;
    public List<Node> neighbors;
    public Node() {
        val = 0;
        neighbors = new ArrayList<Node>();
    }
    public Node(int _val) {
        val = _val;
        neighbors = new ArrayList<Node>();
    }
    public Node(int _val, ArrayList<Node> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
}
*/

class Solution {

    Map<Integer, Node> map = new HashMap<>();

    public Node cloneGraph(Node node) {
        if (node == null) {
            return null;
        }

        Node newNode = createNode(node.val);
        dfs(node);

        return newNode;
    }

    public Node createNode(int val) {
        if (!map.containsKey(val)) {
            map.put(val, new Node(val));
        }
        return map.get(val);
    }

    public void dfs(Node oldNode) {
        Node newNode = map.get(oldNode.val);

        for (Node oldNeighbor : oldNode.neighbors) {
            boolean hasIt = false;
            for (Node newNeighbor : newNode.neighbors) {
                if (newNeighbor.val == oldNeighbor.val) {
                    hasIt = true;
                    break;
                }
            }

            if (!hasIt) {
                Node newNeighbor = createNode(oldNeighbor.val);
                newNode.neighbors.add(newNeighbor);
                newNeighbor.neighbors.add(newNode);
                dfs(oldNeighbor);
            }
        }
    }
}
