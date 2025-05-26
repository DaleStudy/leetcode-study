class Solution {
    public:
        void dfs(Node* node, unordered_map<Node*, Node*>& map){
            if(map.count(node))
                return;
            
            map[node] = new Node(node->val);
    
            for(int i = 0; i < node->neighbors.size(); i++)
                dfs(node->neighbors[i], map);
        }
    
        Node* cloneGraph(Node* node) {
            if(node == NULL)
                return NULL;
    
            unordered_map<Node*, Node*> map;
    
            dfs(node, map);
    
            for(auto& x : map){
                Node* org = x.first;
                Node* dst = x.second;
                for(int i = 0; i < org->neighbors.size(); i++){
                    dst->neighbors.push_back(map[org->neighbors[i]]);
                }
            }
            
            return map[node];
        }
    };
