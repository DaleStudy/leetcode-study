/*
    풀이 :
        전위순회로 root 먼저 체크
            둘 다 null이면 true, 둘 중 하나만 null이면 false, val이 다르면 false 리턴
        left, right 노드에 재귀적으로 함수 호출하고 둘 중 false인 경우 있으면 false
        정상적으로 함수 끝에 다르면 true

    트리 일치하는 노드 개수 : min (P, Q) = M
    M은 P, Q중 하나에 비례

    TC : O (M)
        
    SC : O (M)
        재귀호출스택 메모리
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
        bool isSameTree(TreeNode* p, TreeNode* q) {
            if (!p || !q)
                return p == q;
            if (p->val != q->val)
                return false;
            if (!isSameTree(p->left, q->left))
                return false;
            if (!isSameTree(p->right, q->right))
                return false;
            return true;
        }
    };
