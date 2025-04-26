/*
    풀이 :
        dfs를 이용해 모든 노드를 탐색하며 가장 하위노드에서 바텀업 방식으로 depth를 1씩 쌓아나가서
        최상위 노드의 depth를 구한다

    노드의 개수 : N

    TC : O(N)
        전체 노드를 순회하므로 O(N)

    SC : O(N)
        재귀호출 스택이 노드 개수만큼 쌓이므로 O(N)
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
        int maxDepth(TreeNode* root) {
            if (!root)
                return 0;
            return max(maxDepth(root->left) + 1, maxDepth(root->right) + 1);
        }
    };
