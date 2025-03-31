/**
 * 배열의 각 인덱스에서 가능한 점프를 통해 마지막 인덱스에 도달할 수 있는지 확인하는 문제
 * @param {number[]} nums - 각 인덱스에서 이동할 수 있는 최대 거리
 * @returns {boolean} - 마지막 인덱스에 도달할 수 있으면 true, 아니면 false
 * 
 * 시간 복잡도: O(2^n)
 *  - DFS 기반의 탐색이므로 최악의 경우 모든 경우 탐색
 * 
 * 공간 복잡도: O(n) (재귀 호출 스택과 방문 배열 사용)
 *  - `visited` 배열이 nums.length 크기를 차지
 */
function canJump(nums: number[]): boolean {
    const visited = new Array(nums.length).fill(false);

    const dfs = (idx: number): boolean => {
        if (idx >= nums.length - 1) return true; // 마지막 인덱스 이상 도달하면 성공
        if (visited[idx]) return false; // 이미 방문한 경우 중복 방문 방지

        visited[idx] = true; // 방문 처리

        for (let i = 1; i <= nums[idx]; i++) { // 현재 위치에서 가능한 모든 점프 탐색
            if (dfs(idx + i)) return true;
        }

        return false;
    }

    return dfs(0); // 0번 인덱스에서 시작
}

