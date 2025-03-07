/**
 * 모든 회의 참석할 수 있는지 확인하는 함수
 * @param {number[][]} intervals - [회의 시작시간, 회의 종료시간] 배열
 * @returns {boolean} - 전체 회의 참석 여부
 * 
 * 시간 복잡도: O(nlogn)
 *  - 모든 회의 시간을 정렬하는데 O(nlogn) 소요
 * 
 * 공간 복잡도: O(1)
 *  - 추가 공간 사용 X
 */
function canAttendMeetings(intervals: number[][]): boolean {
    // 회의 시작 시간 기준으로 오름차순 정렬
    intervals.sort((a,b) => a[0] - b[0]);

    for (let i=0; i < intervals.length -1; i++) {
        // 다음 회의 끝나는 시간이 햔제 회의 시작 시간보다 빠르면 false
        if (intervals[i][1] > intervals[i+1][0]) return false;
    }

    return true;
}

