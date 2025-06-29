/*
    풀이 : 
        중위순회로 트리를 순회하면서 순서대로 vector에 담는다
        BST는 중위순회 시 크기 순서로 탐색되므로 vector에서 k번째인 요소를 return

    트리 개수 : N

    TC : O (N)
        모든 트리 dfs로 순회

    SC : O (N)
        배열 크기는 트리 개수에 비례
*/

#include <vector>
using namespace std;
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
        int kthSmallest(TreeNode* root, int k) {
            vector<int> v;
            dfs(root, v);
            return v[k - 1];
        }
        void dfs(TreeNode* root, vector<int>& v) {
            if (!root)
                return ;
            if (root->left)
                dfs(root->left, v);
            v.push_back(root->val);
            if (root->right)
                dfs(root->right, v);
        }
    };
