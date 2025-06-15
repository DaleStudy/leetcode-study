class Solution {
	public:
		int maxPathSum(TreeNode* root) {
			int res = INT_MIN;
	
			dfs(root, res);
			return res;
		}
	
		int dfs(TreeNode* root, int& res) {
			if (!root)
				return 0;
	
			// 좌측 부분트리, 우측 부분트리를 각각 계산할 때 dfs의 '반환값'을 활용
			// 음수값이 나올 경우는 0으로 대체함
			int left = max(0, dfs(root->left, res));
			int right = max(0, dfs(root->right, res));
	
			// 최종 반환할 값 업데이트
			// 좌측 트리, 우측 트리, 루트 노드를 모두 통과하는 경로가 현재까지 최댓값인지 비교해서 갱신
			res = max(res, root->val + left + right);
	
			// 상위 노드로 전달되는 값은 root의 값을 포함하는 경로의 값이다
			// 따라서 좌측 트리 혹은 우측 트리 중 하나의 경로만을 선택해서 통과할 수 있다
			return root->val + max(left, right);
		}
	};
