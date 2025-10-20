/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

type Codec struct {
    
}

func Constructor() Codec {
    return Codec{}
}

// Serializes a tree to a single string.
func (this *Codec) serialize(root *TreeNode) string {
    if root == nil {
        return ""
    }
    type Pair struct {
        node *TreeNode
        path string
    }
    queue := []Pair{{node: root, path: "1"}}
    var tokens []string
    for len(queue) != 0 {
        u := queue[0]
        queue = queue[1:]
        tokens = append(tokens, fmt.Sprintf("%s:%d", u.path, u.node.Val))
        if u.node.Left != nil {
            queue = append(queue, Pair{node: u.node.Left, path: u.path + "0"})
        }
        if u.node.Right != nil {
            queue = append(queue, Pair{node: u.node.Right, path: u.path + "1"})
        }
    }
    return strings.Join(tokens, ",")
}

// Deserializes your encoded data to tree.
func (this *Codec) deserialize(data string) *TreeNode {
    if data == "" {
        return nil
    }
    nodes := map[string]*TreeNode{}
    for _, token := range strings.Split(data, ",")  {
        values := strings.Split(token, ":")
        path := values[0]
        nodeVal, _ := strconv.Atoi(values[1])
        nodes[path] = &TreeNode{Val: nodeVal}
        if path == "1" {
            continue
        }
        if path[len(path) - 1] == '0' {
            nodes[path[: len(path) - 1]].Left = nodes[path]
        } else {
            nodes[path[: len(path) - 1]].Right = nodes[path]
        }
    }
    return nodes["1"]
}


/**
 * Your Codec object will be instantiated and called as such:
 * ser := Constructor();
 * deser := Constructor();
 * data := ser.serialize(root);
 * ans := deser.deserialize(data);
 */
