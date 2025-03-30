/**
 * 처음 집과 끝 집은 연결되어 있음.
 * 주어진 배열에서 인접한 집을 털지 않고 훔칠 수 있는 최대 금액을 계산하는 함수
 * 
 * @param {number[]} nums - 각 집에 있는 돈의 양을 나타내는 배열
 * @returns {number} - 경보를 울리지 않고 훔칠 수 있는 최대 금액
 * 
 * 시간 복잡도: O(n)
 *   - 모든 집을 한 번씩 방문
 * 
 * 공간 복잡도: O(1)
 *  - 상수 개의 변수만 사용
 */
function rob(nums: number[]): number {
    const houses = nums.length;

    if (houses === 1) return nums[0];

    const robber = (nums: number[], start: number, end: number) => {
        let prevMax = 0; // 바로 이전 집까지 털어서 얻은 최대 금액
        let currMax = 0; // 현재 집까지 털어서 얻은 최대 금액

        // start부터 end까지 반복하며 DP 진행
        for (let i = start; i <= end; i++) {
            // 현재 집(i)을 털 경우와 털지 않을 경우의 최대 금액 계산
            const temp = currMax;
            currMax = Math.max(currMax, prevMax + nums[i]);
            prevMax = temp;
        }

        return currMax;
    }


    // 원형 구조이므로, 첫 번째 집을 털 경우와 마지막 집을 털 경우는 동시에 불가능
    // 두 구간을 따로 계산하고 최대값을 반환
    const max1 = robber(nums, 0, houses - 2); // 첫 번째 집부터 마지막에서 두 번째 집까지 고려
    const max2 = robber(nums, 1, houses - 1); // 두 번째 집부터 마지막 집까지 고려

    return Math.max(max1, max2);

};

