class Solution {
    public boolean isValidBST(TreeNode root) {
        if(root==null||(root.left==null&&root.right==null)) return true;
        return isvalid(root,Long.MIN_VALUE,Long.MAX_VALUE);
    }
    public boolean isvalid(TreeNode root,long min,long max)
    {
        if(root==null) return true;
        if(root.val<=min||root.val>=max) return false;
        return isvalid(root.left,min,root.val)&&isvalid(root.right,root.val,max);
    }
}

