// Time Complexity: O(N + E) Node + Edge
// Space Complexity: O(N + E)

var cloneGraph = function (node) {
  // to keep track of all the nodes that have already been copied
  const map = new Map();

  // helper to perform the deep copy
  const dfs = (currentNode) => {
    if (!currentNode) return null;

    // if the node has already been copied, return the copied one
    if (map.has(currentNode)) return map.get(currentNode);

    // create a new node with the current node's value
    const newNode = new Node(currentNode.val);

    // store this new node in the map
    map.set(currentNode, newNode);

    // iterate through each neighbor of the current node
    for (const neighbor of currentNode.neighbors) {
      // clone the neighbors and add them to the new node's neighbors
      newNode.neighbors.push(dfs(neighbor));
    }

    // return the newly created node
    return newNode;
  };

  // start the deep copy from the given node
  return dfs(node);
};
