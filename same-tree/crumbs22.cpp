/*
	전위순회 하면서 두 트리가 같은지 비교
	재귀적으로 탐색하므로 
	두 트리의 자식노드 중 하나라도 없다면 탈출한다
	p->val == q->val 조건이 아닌 p->val != q->val 조건을 판단해야 
	p->val과 q->val이 같을 때 그 다음 자식노드로 내려가는 return문으로 빠질 수 있다
	(p->val == q->val 조건을 사용하면 true가 반환되므로 중간에 종결된다)
	시간복잡도는 트리의 높이와 같다
	다른 추가적 공간은 사용하지 않으므로 공간복잡도는 O(1)이다
*/
class Solution {
public:
    bool isSameTree(TreeNode* p, TreeNode* q) {

        if (!p && !q)
            return (true);
        if (!p || !q)
            return (false);
        if (p->val != q->val)
            return (false);

        return (isSameTree(p->left, q->left) && isSameTree(p->right, q->right));
    }
};
