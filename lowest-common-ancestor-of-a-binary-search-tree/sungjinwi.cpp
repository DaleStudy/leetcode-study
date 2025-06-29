/* 
    풀이 : 
        현재 root를 기준으로 p, q가 어딨는지 판별
        p, q값이 모두 root 보다 작으면 왼쪽, 모두 root 보다 크면 오른쪽 노드로 이동
        그 외의 경우 (root 값이 p 또는 q와 같을 경우, p와 q사이에 있는 경우)에는
        현재 root가 LCA이므로 root 리턴

    트리 높이 : H
    
    TC : O (H)
        반복문이 트리 높이에 비례

    SC : O (1)
*/


#include <algorithm>
using namespace std;
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */

 class Solution {
    public:
        TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
            int small = min(p->val, q->val);
            int big = max(p->val, q->val);
            while (root) {
                if (root->val > big)
                    root = root->left;
                else if (root->val < small)
                    root = root->right;
                else
                    break;
            }
            return root;
        }
    };
