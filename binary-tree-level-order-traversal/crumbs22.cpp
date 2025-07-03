/*
	queue를 활용해서 자식 노드의 수를 세고, 그만큼 반복문을 돌면서
	각 노드의 값을 저장하는 방식으로 깊이순 트리 순회를 구현
	트리의 모든 노드를 한 번씩 방문하므로 O(n)의 시간복잡도,
	트리의 모든 노드를 저장하므로 O(n)의 공간 복잡도를 가진다.
*/
class Solution {
	public:
		vector<vector<int>> levelOrder(TreeNode* root) {
			queue<TreeNode*> q;
			vector<vector<int>> ans;
			if (!root)
				return ans;
	
			q.push(root);
			while (!q.empty()) {
				vector<int> tmp;
				int size = q.size();
				for (int i = 0; i < size; i++) {
					TreeNode* child = q.front();
					q.pop();
					tmp.push_back(child->val);
					if (child->left)
						q.push(child->left);
					if (child->right)
						q.push(child->right);
				}
				ans.push_back(tmp);
			}
			return ans;
		}
	};
