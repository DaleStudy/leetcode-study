package leetcode_study

/*
* Graph Node 복사 문제
* queue를 사용해 문제 해결
* 새로 생성한 Node에 대해 방문처리를 하지 않을 경우 무한 Loop에 빠지게됨 -> 각 노드가 양방향을 가리키고 있기 때문.
* 따라서, Map 자료구조를 사용해 Map<기존 Node, 복사 Node>의 모습으로 Key-Value 쌍으로 방문처리를 표현
*
* 시간 복잡도: O(n)
* -> graph의 Node를 한 번씩 방문하여 복사하는 과정: O(n)
* 공간 복잡도:
* -> 복사된 Node를 매핑하는 Map 자료구조의 크기: O(n)
* -> BFS를 사용한 queue size: O(n)
* -> 새로 생성된 Node의 neighbor list: O(n)
* */
fun cloneGraph(node: Node?): Node? {
    if (node == null) return null
    if (node.neighbors.isEmpty()) return Node(1)

    // Map< 기존 Node, 복사 Node>
    val nodeMap = mutableMapOf<Node, Node>()

    val queue = ArrayDeque<Node>()
    queue.add(node)
    nodeMap[node] = Node(node.`val`)

    while (queue.isNotEmpty()) {
        val current = queue.removeFirst()
        val clonedNode = nodeMap[current]!! // 현재 노드의 복제본

        for (neighbor in current.neighbors) {
            if (neighbor == null) continue

            // 해당 이웃이 아직 복사되지 않았다면 복사하여 맵에 저장하고 큐에 추가
            if (!nodeMap.containsKey(neighbor)) {
                nodeMap[neighbor] = Node(neighbor.`val`)
                queue.add(neighbor)
            }

            // 복제된 현재 노드의 이웃 리스트에 복제된 이웃 노드를 추가
            // 양방향을 따질 필요 없이 내부 neighbor node list에 모든 노드가 있음
            clonedNode.neighbors.add(nodeMap[neighbor])
        }
    }
    return nodeMap[node]
}

