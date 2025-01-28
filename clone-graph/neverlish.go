package main

import "testing"

func Test_cloneGraph(t *testing.T) {
	result1 := cloneGraph(&Node{
		Val: 1,
		Neighbors: []*Node{
			{
				Val: 2,
				Neighbors: []*Node{
					{
						Val: 4,
						Neighbors: []*Node{
							{
								Val: 3,
								Neighbors: []*Node{
									{
										Val: 1,
									},
									{
										Val: 4,
									},
								},
							},
							{
								Val: 1,
								Neighbors: []*Node{
									{
										Val: 3,
									},
									{
										Val: 2,
									},
								},
							},
						},
					},
					{
						Val: 1,
						Neighbors: []*Node{
							{
								Val: 4,
							},
							{
								Val: 2,
							},
						},
					},
				},
			},
			{
				Val: 3,
				Neighbors: []*Node{
					{
						Val: 4,
					},
					{
						Val: 1,
					},
				},
			},
		},
	})

	if result1.Val != 1 {
		t.Fatal(result1.Val)
	}
}

type Node struct {
	Val       int
	Neighbors []*Node
}

func dfs(node *Node, visited map[*Node]*Node) *Node {
	if node == nil {
		return nil
	}

	if _, ok := visited[node]; ok {
		return visited[node]
	}

	cloneNode := &Node{Val: node.Val}

	visited[node] = cloneNode

	for _, neighbor := range node.Neighbors {
		cloneNode.Neighbors = append(cloneNode.Neighbors, dfs(neighbor, visited))
	}

	return cloneNode
}

func cloneGraph(node *Node) *Node {
	if node == nil {
		return nil
	}

	visited := make(map[*Node]*Node)

	return dfs(node, visited)
}
