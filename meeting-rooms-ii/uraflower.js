/**
 * @param {number[][]} intervals
 * @return {number}
 */
const minMeetingRooms = function(intervals) {
    const starts = intervals.map(i => i[0]).sort((a, b) => a - b);
    const ends = intervals.map(i => i[1]).sort((a, b) => a - b);

    let rooms = 0;
    let endIdx = 0;

    for (let i = 0; i < starts.length; i++) {
        if (starts[i] < ends[endIdx]) {
            rooms++; // 새로운 방이 필요
        } else {
            endIdx++; // 기존 방 재사용 가능
        }
    }

    return rooms;
};

// 시간복잡도: O(n * log n) (정렬)
// 공간복잡도: O(n)
