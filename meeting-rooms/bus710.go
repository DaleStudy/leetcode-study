package hello

import "log"

// Definition of Interval:
type Interval struct {
	Start, End uint64
}

func CanAttendMeetings(intervals []*Interval) bool {
	if len(intervals) == 0 {
		return true
	} else if len(intervals) == 1 {
		return true
	}

	// The mask is used to store the occupied time as binary.
	mask := make([]uint64, len(intervals))

	// The accumulator is used to store the accumulated occupied time.
	// If there is any non-0 value after the bit AND operation, it means there is an overlap.
	acc := uint64(0)

	for i, interval := range intervals {
		mask[i] = GetDifferenceMask(*interval)

		// Print the mask in binary format.
		log.Printf("%d - %40b\n", i, mask[i])

		// If it is the first interval, set the accumulator to the mask.
		if i == 0 {
			acc = mask[0]
			continue
		}

		// Check if there is any overlap.
		if acc&mask[i] != 0 {
			return false
		}

		// Accumulate the occupied time.
		acc |= mask[i]
	}

	return true
}

// GetDifferenceMask returns a number to be used as the occupied time.
// Example 1, if the interval is from 0 to 4, the mask will be 11111.
//
//	2^0 + 2^1 + 2^2 + 2^3 + 2^4 = 31 = 11111
//	But the start time is 0, so no bit shift is needed.
//
// Example 2, if the interval is from 1 to 4, the mask will be 11110.
//
//	2^1 + 2^2 + 2^3 + 2^4 = 30 = 11110
//	But the start time is 1, so the mask will be shifted to the left by 1.
//
// Let's say if we want to check if there is any overlap between 0 to 4 and 1 to 4, the mask values are 11111 and 11110.
// Bit AND operation will return 11110, which is not 0. So there is an overlap.
func GetDifferenceMask(interval Interval) uint64 {
	mask := uint64(0)
	for i := interval.Start; i < interval.End; i++ {
		mask |= 1
		mask <<= 1
	}
	mask <<= interval.Start
	return mask
}

// ==================== Test ====================

import "testing"

func TestCanAttendMeetings(t *testing.T) {
	type args struct {
		intervals []*Interval
	}
	tests := []struct {
		name string
		args args
		want bool
	}{
		{
			name: "test1",
			args: args{
				intervals: []*Interval{
					{Start: 0, End: 30},
					{Start: 5, End: 10},
					{Start: 15, End: 20},
				},
			},
			want: false,
		},
		{
			name: "test2",
			args: args{
				intervals: []*Interval{
					{Start: 5, End: 8},
					{Start: 9, End: 15},
				},
			},
			want: true,
		},
		{
			name: "test3",
			args: args{
				intervals: []*Interval{
					{Start: 0, End: 8},
					{Start: 8, End: 10},
				},
			},
			want: true,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := CanAttendMeetings(tt.args.intervals); got != tt.want {
				t.Errorf("CanAttendMeetings() = %v, want %v", got, tt.want)
			}
		})
	}
}
