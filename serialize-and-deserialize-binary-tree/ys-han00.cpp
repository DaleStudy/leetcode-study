/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Codec {
public:

    // Encodes a tree to a single string.
    string serialize(TreeNode* root) {
        queue<TreeNode*> que;
        string str = "root = [";
        
        if(root != nullptr) {
            que.push(root);
            str += to_string(root->val);
        }
        
        while(!que.empty()) {
            TreeNode* curr = que.front();
            que.pop();
            if(curr->left != nullptr) {
                que.push(curr->left);
                str += "," + to_string(curr->left->val);
            }
            else
                str += ",null";

            if(curr->right != nullptr) {
                que.push(curr->right);
                str += "," + to_string(curr->right->val);
            }
            else
                str += ",null";
        }
        str += "]";
        return str;
    }

    // Decodes your encoded data to tree.
    TreeNode* deserialize(string data) {
        int start = data.find('[') + 1;
        int end = data.find_last_of(']');
        
        if (start >= end) return nullptr; 

        string content = data.substr(start, end - start);

        vector<string> nodes;
        stringstream ss(content);
        string temp;
        while (getline(ss, temp, ','))
            nodes.push_back(temp);
        
        int idx = 0;
        TreeNode* root = new TreeNode(stoi(nodes[idx++]));
        queue<TreeNode*> que;
        que.push(root);

        while(!que.empty() && idx < nodes.size()) {
            TreeNode* curr = que.front();
            que.pop();

            if(nodes[idx] == "null") {
                curr->left = nullptr;
                idx++;
            } else {
                curr->left = new TreeNode(stoi(nodes[idx++]));
                que.push(curr->left);
            }

            if(nodes[idx] == "null") {
                curr->right = nullptr;
                idx++;
            } else {
                curr->right = new TreeNode(stoi(nodes[idx++]));
                que.push(curr->right);
            }
        }
        
        return root;
    }
};

// Your Codec object will be instantiated and called as such:
// Codec ser, deser;
// TreeNode* ans = deser.deserialize(ser.serialize(root));

