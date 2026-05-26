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

// 재귀를 통해 동일한 트리인지 확인
class Solution {
public:
    bool isSameTree(TreeNode* p, TreeNode* q) {
        if (p == nullptr || q == nullptr)
        {
            return p == q;
        }

        bool l = isSameTree(p->left, q->left);
        bool r = isSameTree(p->right, q->right);
        bool cur = p->val == q->val;

        return l && r && cur;
    }
};
