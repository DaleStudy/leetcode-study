/*
풀이
- DFS를 이용하여 풀이합니다
Big O
- N: 노드의 수
- Serialize
  - Time complexity: O(N)
    - 모든 노드를 최대 1번 조회합니다
  - Space complexity: O(N)
    - buildString의 재귀 호출 스택의 깊이는 노드의 높이에 비례하여 증가하며, 노드의 높이는 최대 N입니다
    - 결과 string의 크기 또한 N에 비례하는 형태로 증가합니다
- Deserialize
  - Time complexity: O(N)
    - 모든 노드를 최대 1번 조회합니다
  - Space complexity: O(N)
    - data를 split한 배열의 크기가 N에 비례하여 증가합니다
	- buildTree의 재귀 호출 스택의 깊이는 노드의 높이에 비례하여 증가하며, 노드의 높이는 최대 N입니다
*/

import (
	"strconv"
	"strings"
)

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
const (
	DELIMITER = "|"
)

type Codec struct {
}

func Constructor() Codec {
	codec := Codec{}
	return codec
}

// Serializes a tree to a single string.
func (this *Codec) serialize(root *TreeNode) string {
	if root == nil {
		return ""
	}
	var sb strings.Builder
	buildString(&sb, root)
	return sb.String()
}

// Deserializes your encoded data to tree.
func (this *Codec) deserialize(data string) *TreeNode {
	if data == "" {
		return nil
	}
	splitData := make([]string, 0, len(data)/2)
	splitData = strings.Split(data, DELIMITER)
	splitData = splitData[:len(splitData)-1]
	return buildTree(&splitData)
}

// ----- Helpers -----
func buildString(sb *strings.Builder, node *TreeNode) {
	if node == nil {
		sb.WriteString(DELIMITER)
		return
	}
	sb.WriteString(strconv.Itoa(node.Val))
	sb.WriteString(DELIMITER)
	buildString(sb, node.Left)
	buildString(sb, node.Right)
}

func buildTree(splitData *[]string) *TreeNode {
	val := (*splitData)[0]
	*splitData = (*splitData)[1:]
	if val == "" {
		return nil
	}
	node := &TreeNode{}
	intVal, _ := strconv.Atoi(val)
	node.Val = intVal
	node.Left = buildTree(splitData)
	node.Right = buildTree(splitData)
	return node
}

/**
 * Your Codec object will be instantiated and called as such:
 * ser := Constructor();
 * deser := Constructor();
 * data := ser.serialize(root);
 * ans := deser.deserialize(data);
 */
