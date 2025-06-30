/*
    p와 q의 공통조상을 찾는 문제
    왼쪽과 오른쪽에서 각각 p와 q를 찾고, 만약 좌우에서 모두 p와 q를 찾았다면 현재 노드가 공통 조상이다
    p와 q 중 하나만 존재한다면 존재하는 쪽의 노드에 공통조상이 존재한다
    모든 노드를 한번씩 방문하므로 시간복잡도는 O(n)이다. 공간복잡도는 트리의 높이에 비례하므로 O(h).
*/
class Solution {
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        if (!root)
            return nullptr;
        if (root->val == p->val)
            return p;
        if (root->val == q->val)
            return q;
        
        TreeNode* nl = lowestCommonAncestor(root->left, p, q);
        TreeNode* nr = lowestCommonAncestor(root->right, p, q);
        if (!nl && nr) // nl쪽이 비어있으면 nr쪽에 공통조상 존재
            return nr;
        else if (!nr) // nr쪽이 비어있으면 nl쪽에 공통조상 존재
            return nl;
        else // 그 외의 경우는 nr과 nl의 부모에 공통조상 존재
            return root;
    }
};
