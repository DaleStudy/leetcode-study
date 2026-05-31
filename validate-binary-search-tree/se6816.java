/**
    풀이 :
        루트에서부터 DFS를 통해 내려가면서, 조상노드에 대한 값을 저장하고 비교하면서 검증하는 방식

    복잡도 계산 :
        TreeNode의 개수 -> N
        시간 복잡도 : O(N^2)
        공간 복잡도 : O(N)
*/

class Solution1 {
    enum Direction {
        LEFT, RIGHT;
    }

    class Node{
        int val;
        Direction direction;
        Node(int val, Direction d) {
            this.val = val;
            this.direction = d;
        }
    }

    public boolean isValidBST(TreeNode root) {

        return validateTree(root, true, new ArrayList<Node>());
    }

    public boolean validateTree(TreeNode node, boolean isRoot, List<Node> grandParents) {
        if (node == null) {
            return true;
        }

        if (!isRoot) {
            if (!isValid(node.val, grandParents)) {
                return false;
            }
        }

        Node left = new Node(node.val, Direction.LEFT);
        grandParents.add(left);
        boolean isLeftValidate = validateTree(node.left, false, grandParents);
        grandParents.remove(left);
        Node right = new Node(node.val, Direction.RIGHT);
        grandParents.add(right);
        boolean isRightValidate = validateTree(node.right, false, grandParents);
        grandParents.remove(right);
        return isLeftValidate && isRightValidate;
    }

    public boolean isValid(int value, List<Node> grandParents) {
        for (Node gpNode : grandParents) {
            if (gpNode.direction == Direction.LEFT) {
                if (!(value < gpNode.val)) {
                    return false;
                }
            } else {
                if (!(value > gpNode.val)) {
                    return false;
                }
            }
        }
        return true;
    }
}

/**
    풀이 :
        루트에서부터 DFS를 통해 내려가면서, 조상노드에 대한 값을 저장하고 비교하면서 검증하는 방식

    복잡도 계산 :
        TreeNode의 개수 -> N
        시간 복잡도 : O(NlogN)
        공간 복잡도 : O(N)
*/
class Solution2 {
    enum Direction {
        LEFT, RIGHT;
    }

    class Parents {
        PriorityQueue<Integer> left;
        PriorityQueue<Integer> right;

        public Parents() {
            left = new PriorityQueue<>();
            right = new PriorityQueue<>(Collections.reverseOrder());
        }
    }

    public boolean isValidBST(TreeNode root) {

        return validateTree(root, true, new Parents());
    }

    public boolean validateTree(TreeNode node, boolean isRoot, Parents parents) {
        if (node == null) {
            return true;
        }

        if (!isRoot) {
            if (!isValid(node.val, parents)) {
                return false;
            }
        }

        parents.left.add(node.val);
        boolean isLeftValidate = validateTree(node.left, false, parents);
        parents.left.remove(node.val);
        parents.right.add(node.val);
        boolean isRightValidate = validateTree(node.right, false, parents);
        parents.right.remove(node.val);

        return isLeftValidate && isRightValidate;
    }

    public boolean isValid(int value, Parents parents) {
        if(!parents.left.isEmpty()) {
            if(!(value < parents.left.peek())) {
                return false;
            }
        }

        if(!parents.right.isEmpty()) {
            if(!(value > parents.right.peek())) {
                return false;
            }
        }
        return true;
    }
}


/**
    풀이 :
        루트에서부터 DFS를 통해 내려가면서, 범위를 비교하면서 검증하는 방식

    복잡도 계산 :
        TreeNode의 개수 -> N
        시간 복잡도 : O(N)
        공간 복잡도 : O(N)
*/
class Solution {

    public boolean isValidBST(TreeNode root) {

        return validateTree(root, true, Long.MIN_VALUE, Long.MAX_VALUE);
    }

    public boolean validateTree(TreeNode node, boolean isRoot, long min, long max) {
        if (node == null) {
            return true;
        }

        if (!isRoot) {
            if (!isValid(node, min, max)) {
                return false;
            }
        }

        return validateTree(node.left, false, min, node.val) && validateTree(node.right, false, node.val, max);
    }

    public boolean isValid(TreeNode node, long min, long max) {
        
        if(!(node.val > min)) {
            return false;
        }

        if(!(node.val < max)) {
            return false;
        }

        return true;
    }
}

