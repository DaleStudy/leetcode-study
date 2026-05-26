/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */

 // 그래야할 필요는 없다고 명시하지만, LeetCode 형식과 동일하게 직렬화/역직렬화 구현
class Codec {
public:
    // Encodes a tree to a single string.
    string serialize(TreeNode* root) {
        vector<string> tokens;
        queue<TreeNode*> q;
        q.push(root);
        while (!q.empty()) 
        {
            auto node = q.front();
            q.pop();
            if (node == nullptr) 
            {
                tokens.push_back("null");
                continue;
            }

            tokens.push_back(to_string(node->val));
            q.push(node->left);
            q.push(node->right);
        }

        // 굳이 지우지 않아도 역직렬화가 가능
        // 하지만 LeetCode와 동일하게 구현하기 위한 처리
        while (!tokens.empty() && tokens.back() == "null")
        {
            tokens.pop_back();
        }

        string s = "[";
        for (int i = 0; i < tokens.size(); i++) 
        {
            if (i)
            { 
                s += ",";
            
            }
            s += tokens[i];
        }

        s += "]";
        //cout << s;
        return s;
    }

    // Decodes your encoded data to tree.
    TreeNode* deserialize(string data) {
        if (data == "[]")
        {
            return nullptr;
        }

        data = data.substr(1, data.size() - 2); // '[', ']' 제거
        stringstream ss(data);
        string token;

        queue<string> v;
        while (getline(ss, token, ','))
        {
            v.push(token);
        }

        TreeNode* root = new TreeNode(stoi(v.front()));
        v.pop();
        queue<TreeNode*> q;
        q.push(root);
        while (!q.empty())
        {
            auto cur = q.front();
            q.pop();

            // 만약 직렬화 과정에서 null을 제거하지 않았다면 이러한 확인은 필요없어짐
            if (v.empty())
            {
                break;
            }

            string l = v.front();
            v.pop();
            if (l != "null")
            {
                cur->left = new TreeNode(stoi(l));
                q.push(cur->left);
            }

            if (v.empty())
            {
                break;
            }
            
            string r = v.front();
            v.pop();
            if (r != "null")
            {
                cur->right = new TreeNode(stoi(r));
                q.push(cur->right);
            }
        }
        return root;
    }
};

// Your Codec object will be instantiated and called as such:
// Codec ser, deser;
// TreeNode* ans = deser.deserialize(ser.serialize(root));
