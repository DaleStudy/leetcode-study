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
//     int maxDepth(TreeNode* root) {
//         if(root == nullptr)
//             return 0;
        
//         int ans = -1, depth;
//         queue<pair<int, TreeNode*>> que;

//         que.push({1, root});
//         while(!que.empty()) {
//             depth = que.front().first;
//             TreeNode* Node = que.front().second;
//             que.pop();

//             if(!Node->left && !Node->right) {
//                 ans = max(ans, depth);
//                 continue;
//             }
//             if(Node->left)
//                 que.push({depth + 1, Node->left});
//             if(Node->right)
//                 que.push({depth + 1, Node->right});
//         }

//         return ans;
//     }
// };

class Solution {
public:
    int maxDepth(TreeNode* root) {
        if(!root)
            return 0;
        return 1 + max(maxDepth(root->left), maxDepth(root->right));
    }
};

