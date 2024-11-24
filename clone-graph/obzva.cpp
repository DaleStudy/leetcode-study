/**
 * 풀이
 * - BFS와 해시맵을 사용하여 풀이합니다
 * 
 * Big O
 * - N: 주어진 노드의 개수
 * - E: 주어진 노드의 간선의 개수
 * 
 * - Time complexity: O(E)
 *   - 한 Node에서 다른 Node로 향하는 모든 edge를 두번씩 탐색합니다 (두 방향으로 연결되어 있기 때문)
 * - Space complexity: O(N) 
 *   - 해시맵에 최대 N개의 노드를 저장합니다
 */

/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> neighbors;
    Node() {
        val = 0;
        neighbors = vector<Node*>();
    }
    Node(int _val) {
        val = _val;
        neighbors = vector<Node*>();
    }
    Node(int _val, vector<Node*> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
};
*/

class Solution {
public:
    Node* cloneGraph(Node* node) {
        if (node == nullptr) return nullptr;

        unordered_map<Node*, Node*> node_map;
        node_map[node] = new Node(node->val);

        queue<Node*> q;
        q.push(node);

        while (!q.empty()) {
            Node* p = q.front();
            q.pop();

            for (Node* neighbor : p->neighbors) {
                // 방문한 적이 없는 노드일 경우
                if (node_map.find(neighbor) == node_map.end()) {
                    // node_map에 새로운 노드를 복제하여 추가
                    node_map[neighbor] = new Node(neighbor->val);

                    // 큐에 추가
                    q.push(neighbor);
                }

                node_map[p]->neighbors.push_back(node_map[neighbor]);
            }
        }

        return node_map[node];
    }
};
