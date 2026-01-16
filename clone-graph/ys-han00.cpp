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
        if(!node)
            return nullptr;
        
        
        Node* clone = new Node(node->val);
        map<Node*, Node*> clones;
        queue<Node*> que;
        
        clones[node] = clone;
        que.push(node);

        while(!que.empty()) {
            node = que.front();
            que.pop();

            for(auto neigh : node->neighbors) {
                if(clones.find(neigh) == clones.end()) {
                    que.push(neigh);
                    clones[neigh] = new Node(neigh->val);
                }
                clones[node]->neighbors.push_back(clones[neigh]);
            }
        }

        return clone;
    }
};

