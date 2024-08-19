TC: O(n log n) 왜냐하면, heap에 push연산이 log n이고 각 노드마다 실행하므로.
SC: O(n) queue가 n까지 커질수 있음.

    int kthSmallest(TreeNode* root, int k) {
        priority_queue<int, vector<int>, greater<int>> minHeap;

        // bfs
        queue<TreeNode*> q;
        if (root != nullptr) {
            q.push(root);
        };
        while (!q.empty()) {
            minHeap.push(q.front()->val);
            if (q.front()->left != nullptr) {
                q.push(q.front()->left);
            }
            if (q.front()->right != nullptr) {
                q.push(q.front()->right);
            }
            q.pop();
        }

        for (int i = 0; i < k - 1; i++) {
            minHeap.pop();
        }
        return minHeap.top();
    }
