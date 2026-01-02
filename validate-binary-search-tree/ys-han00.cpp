/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

// class Solution {
// public:
//     bool isValidBST(TreeNode* root) {
//         queue<pair<TreeNode*, vector<pair<int, int>>>> que;
//         int val, dir, num;
        
//         que.push({root, vector<pair<int, int>> ()});
//         while(!que.empty()) {
//             TreeNode* node = que.front().first;
//             vector<pair<int, int>> path = que.front().second;
//             que.pop();
            
//             val = node->val;
        
//             for(int i = 0; i < path.size(); i++) {
//                 num = path[i].first;
//                 dir = path[i].second;
//                 if(dir == 0 && num <= val)
//                     return false;
//                 if(dir == 1 && val <= num)
//                     return false;
//             }
            
//             if(!node->left && !node->right) 
//                 continue;

//             if(node->left) {
//                 path.push_back({val, 0});
//                 que.push({node->left, path});
//                 path.pop_back();
//             }

//             if(node->right) {
//                 path.push_back({val, 1});
//                 que.push({node->right, path});
//                 path.pop_back();
//             }
//         }
        
//         return true;
//     }
// };

class Solution {
public:
    void inorder(TreeNode* root, vector<int>& ordered) {
        if(root==NULL)
            return;

        inorder(root->left, ordered);
        ordered.push_back(root->val);
        inorder(root->right, ordered);
    }

    bool isValidBST(TreeNode* root) {
        vector<int> ordered;
        
        inorder(root, ordered);
        
        for(int i = 1; i < ordered.size(); i++)
            if(ordered[i - 1] >= ordered[i])
                return false;
        
        return true;
    }
};

