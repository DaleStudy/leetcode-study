// Time complexity : O(n)
// Space complexity : O(n)

var isSameTree = function(p, q) {
    // initialize two queues for BFS.
    let queue1 = [p];
    let queue2 = [q];
    
    while (queue1.length > 0 && queue2.length > 0) {
        let node1 = queue1.shift();
        let node2 = queue2.shift();
        
        // if both nodes are null, continue to the next pair of nodes.
        if (node1 === null && node2 === null) {
            continue;
        }
        
        // if one of the nodes is null or their values are different, return false.
        if (node1 === null || node2 === null || node1.val !== node2.val) {
            return false;
        }
        
        // enqueue the left and right children of both nodes.
        queue1.push(node1.left);
        queue1.push(node1.right);
        queue2.push(node2.left);
        queue2.push(node2.right);
    }
    
    // if both queues are empty, the trees are the same
    return queue1.length === 0 && queue2.length === 0;
};
