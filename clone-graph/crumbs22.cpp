#include <vector>
#include <iostream>

using namespace std;

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
/*
	std::vector<T> v;

	v.emplace_back(arg1, arg2, ...); // 생성자 인자를 바로 전달해 컨테이너 안에서 직접 T 객체를 생성
*/

#include <unordered_map>
#include <queue>

class Solution {
	public:
		Node* cloneGraph(Node* node) {
			if (!node)
				return (nullptr);
			unordered_map<Node*, Node*> m;
			queue<Node*> q;
			
			m[node] = new Node(node->val); // 시작 노드를 복제하고 맵과 큐에 등록
			q.push(node);

			// BFS
			while (!q.empty()) {
				Node* cur = q.front();
				q.pop();
				
				for (Node* nei : cur->neighbors) {

					// 아직 복제하지 않은 노드일 때
					if (!m.count(nei)) {
						m[nei] = new Node(nei->val);
						q.push(nei);
					}
					m[cur]->neighbors.push_back(m[nei]); // 현재 복제본에 이 이웃의 복제본을 연결
				}
			}
			return m[node];
		}
	};
