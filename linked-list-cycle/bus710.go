package hello

import "testing"

type ListNode struct {
	Val  int
	Next *ListNode
}

// // Version 1
// func hasCycle(head *ListNode) bool {
// 	if head == nil {
// 		return false
// 	}
// 	return call(head, make(map[*ListNode]int, 0))
// }
//
// func call(h *ListNode, m map[*ListNode]int) bool {
// 	if h.Next == nil {
// 		return false
// 	}
// 	if _, ok := m[h]; ok {
// 		return true
// 	}
// 	m[h] = 1
// 	return call(h.Next, m)
// }

// Version 2
func hasCycle(head *ListNode) bool {
	if head == nil {
		return false
	}
	m := map[*ListNode]int{}
	for head.Next != nil {
		if _, ok := m[head]; !ok {
			m[head] = 1
		} else {
			return true
		}
		head = head.Next
	}
	return false
}

func Test_hasCycle(t *testing.T) {
	// Case 0 list
	c0_3 := &ListNode{Val: -4}
	c0_2 := &ListNode{Val: 0, Next: c0_3}
	c0_1 := &ListNode{Val: 2, Next: c0_2}
	c0_0 := &ListNode{Val: 3, Next: c0_1}
	c0_3.Next = c0_1

	// Case 1 list
	c1_1 := &ListNode{Val: 2}
	c1_0 := &ListNode{Val: 1, Next: c1_1}
	c1_1.Next = c1_0

	// Case 2 list
	c2_0 := &ListNode{Val: 1}

	type args struct {
		head *ListNode
	}
	tests := []struct {
		name string
		args args
		want bool
	}{
		{
			name: "case 0",
			args: args{head: c0_0},
			want: true,
		},
		{
			name: "case 1",
			args: args{head: c1_0},
			want: true,
		},
		{
			name: "case 2",
			args: args{head: c2_0},
			want: false,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			got := hasCycle(tt.args.head)
			if got != tt.want {
				t.Errorf("hasCycle() = %v, want %v", got, tt.want)
			}
		})
	}
}
