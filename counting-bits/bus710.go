package hello

import (
	"fmt"
	"reflect"
	"strings"
	"testing"
)

func countBits(n int) []int {
	r := make([]int, 0)

	for i := range n + 1 {
		b := fmt.Sprintf("%b", i)
		cnt := strings.Count(string(b), "1")
		r = append(r, cnt)
	}

	return r
}

func Test_countBits(t *testing.T) {
	type args struct {
		n int
	}
	tests := []struct {
		name string
		args args
		want []int
	}{
		{
			name: "case 1",
			args: args{
				n: 2,
			},
			want: []int{0, 1, 1},
		},
		{
			name: "case 2",
			args: args{
				n: 5,
			},
			want: []int{0, 1, 1, 2, 1, 2},
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := countBits(tt.args.n); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("countBits() = %v, want %v", got, tt.want)
			}
		})
	}
}
