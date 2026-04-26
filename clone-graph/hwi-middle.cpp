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
        if (node == nullptr)
        {
            return node;
        }

        if (nodeMap.contains(node))
        {
            return nodeMap[node];
        }

        Node* copied = new Node(node->val);
        nodeMap[node] = copied;
        for (auto n : node->neighbors)
        {
            copied->neighbors.push_back(cloneGraph(n));
        }

        return copied;
    }

private:
    unordered_map<Node*, Node*> nodeMap;
};
