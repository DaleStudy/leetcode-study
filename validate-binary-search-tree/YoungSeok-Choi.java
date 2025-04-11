import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

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
// NOTE: 답지를 보고 풀었던 문제.. 정확하게 이해하는 과정이 필요하다.
// TODO: 별도 블로그로 풀이과정을 정리할 것.
class Solution {
    public boolean isValidBST(TreeNode root) {
        return dfs(root, Long.MIN_VALUE, Long.MAX_VALUE);
    }

    public boolean dfs(TreeNode cur, long min, long max) {
        if(cur == null) return true;

        if(cur.val <= min || cur.val >= max) return false;

        return dfs(cur.left, min, cur.val) && dfs(cur.right, cur.val, max);
    }          
}

class WrongSolution {
    public boolean isValidBST(TreeNode root) {
        return dfs(root, new ArrayList<>(Arrays.asList(root.val)));
    }

    public boolean dfs(TreeNode cur, List<Integer> path) {
        
        if(cur.left != null) {
            int lVal = cur.left.val;
            for(int i = 0; i < path.size(); i++) {
                if(i == path.size() - 1) {

                    if(lVal >= path.get(i)) {
                        return false;
                    }
                    
                } else {
                    if(lVal < path.get(i)) {
                        return false;
                    }
                }
            }
            
            path.add(cur.left.val);
            if(!dfs(cur.left, path)) return false;
            path.remove(Integer.valueOf(cur.left.val));
        }

        if(cur.right != null) {
            int rVal = cur.right.val;
            for(int i = 0; i < path.size(); i++) {
                if(i == path.size() - 1) {

                    if(rVal <= path.get(i)) {
                        return false;
                    }
                    
                    
                } else {
                    if(rVal > path.get(i)) {
                        return false;
                    }
                }
            }

            path.add(cur.right.val);
            if(!dfs(cur.right, path)) return false;
            path.remove(Integer.valueOf(cur.right.val));
        }

        return true;
    }   
}
