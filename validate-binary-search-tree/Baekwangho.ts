/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     val: number
 *     left: TreeNode | null
 *     right: TreeNode | null
 *     constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.left = (left===undefined ? null : left)
 *         this.right = (right===undefined ? null : right)
 *     }
 * }
 */

/**
 1차 시도

function isValidBST(root: TreeNode | null): boolean {
  let result = true;

  function validate(node: TreeNode) {
    if (node.left) {
      if (node.val > node.left.val) {
        validate(node.left);
      } else {
        result = false;
      }
    }

    if (node.right) {
      if (node.val < node.right.val) {
        validate(node.right);
      } else {
        result = false;
      }
    }
  }

  validate(root);
  return result;
}
  */

interface TreeNode {
  val: number;
  left: TreeNode;
  right: TreeNode;
}

/** 2차 시도 실패 */
function isValidBST(root: TreeNode | null): boolean {
  let result = true;

  function validate(node: TreeNode, lstandard?: number, rstandard?: number) {
    if (node.left) {
      if (lstandard !== undefined && lstandard > node.left.val) {
        result = false;
      }

      if (rstandard !== undefined && rstandard < node.left.val) {
        result = false;
      }

      if (node.val > node.left.val) {
        validate(node.left, undefined, node.val);
      } else {
        result = false;
      }
    }

    if (node.right) {
      if (lstandard !== undefined && lstandard > node.right.val) {
        result = false;
      }

      if (rstandard !== undefined && rstandard < node.right.val) {
        result = false;
      }

      if (node.val < node.right.val) {
        validate(node.right, node.val, undefined);
      } else {
        result = false;
      }
    }
  }

  validate(root!);
  return result;
}
