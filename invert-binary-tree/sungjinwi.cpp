/*
    풀이 : 
        left와 right을 스왑하는 과정을 dfs를 이용해서 끝까지 반복한다

    트리의 깊이 : N

    TC : O(2^N)
        깊이마다 2번씩 재귀함수 호출

    SC : O(2^N)
        깊이마다 2번씩 재귀함수 호출로 인한 스택 쌓임
*/

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
class Solution {
    public:
        TreeNode* invertTree(TreeNode* root) {
            if (!root)
                return nullptr;
    
            TreeNode* tmp = root->left;
    
            root->left = root->right;
            root->right = tmp;

            invertTree(root->left);
            invertTree(root->right);

            return root;
        }
    };

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};
