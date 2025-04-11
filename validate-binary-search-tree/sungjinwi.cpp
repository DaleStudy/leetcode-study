/*
    풀이 :
        중위순회로 BST를 탐색하면 오름차순으로 탐색
            ->중위순회 했을 떄 오름차순이 아니면 BST가 아니다
        현재 node의 val이 last_val보다 더 큰지 확인하면서 탐색한다

        초기값은 INT_MIN이 있을경우를 생각해서 그보다 작은 값과 비교하기 위해 LONG_MIN사용

    node 갯수 N

    TC : O(N)
        노드 전체 순회
    
    SC : O(N)
        재귀 호출스택이 N에 비례
*/

#include <limits.h>

// Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution {
public:
    bool isValidBST(TreeNode* root) {
        long min = LONG_MIN;
        return dfs(root, &min);
    }

    bool dfs(TreeNode* node, long* last_val){
        if (!node)
            return true;

        if (!dfs(node->left, last_val))
            return false;

        if (*last_val >= node->val)
            return false;
        *last_val = node->val;

        if (!dfs(node->right, last_val))
            return false;

        return true;
    }
};
