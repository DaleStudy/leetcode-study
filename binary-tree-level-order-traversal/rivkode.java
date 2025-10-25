/*
BFS를 사용한 이유는 depth 가 기준이 되어야 하기 때문이다.
depth 별로 value값을 넣어야하기 때문에 BFS로 탐색하며 해당하는 모든 값들을 List에 넣어주었다.
이때 포인트는 몇개의 값들을 depth 별로 나눌것인가 ? 인데 왜냐하면 queue는 자식 노드들을 탐색하며 지속적으로 추가되기 때문이다.
그래서 2중으로 loop를 돌아야 한다.
첫번째는 while문으로 queue가 empty될때까지 확인하는 loop이고
두번째는 queue 사이즈를 미리 계산하여 특정 level의 개수 만큼 도는 for loop 이다.
이렇게 2번 loop를 돌면 depth 별로 size를 알 수 있게된다.
*/

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
import java.util.*;

class Solution {
    public List<List<Integer>> levelOrder(TreeNode root) {
        Queue<TreeNode> queue = new LinkedList<>();
        List<List<Integer>> result = new ArrayList<>();

        if (root == null) {
            return new ArrayList<>();
        }

        queue.offer(root);

        while(!queue.isEmpty()) {
            List<Integer> levelList = new ArrayList<>();
            int queueSize = queue.size();

            for (int i=0; i<queueSize; i++) {
                TreeNode node = queue.poll();
                if (node == null) {
                    continue;
                }

                levelList.add(node.val);

                if (node.left != null) {
                    queue.offer(node.left);
                }

                if (node.right != null) {
                    queue.offer(node.right);
                }
            }
            result.add(levelList);
        }

        return result;
    }

    public class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    
    TreeNode() {}
    TreeNode(int val) { this.val = val; }
    TreeNode(int val, TreeNode left, TreeNode right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
 }
}




