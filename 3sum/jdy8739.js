/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var threeSum = function(nums) {
    const answer = [];

    const sorted = nums.sort((a, b) => a - b);

    for (let i=0; i<sorted.length; i++) {
        if (i > 0 && sorted[i] === sorted[i - 1]) {
            // 위 조건으로 중복 숫자 필터
            continue;
        }

        let l = i + 1;
        let h = sorted.length - 1;

        while (l < h) {
            const sum = sorted[i] + sorted[l] + sorted[h];

            if (sum === 0) {
                const arr = [sorted[i], sorted[l], sorted[h]];
                answer.push(arr);

                // 아래 반복문으로 중복 숫자 필터
                while (l < h && sorted[l] === sorted[l + 1]) l++;
                while (l < h && sorted[h] === sorted[h - 1]) h--;

                h--;
                l++;
            }

            if (sum > 0) h--;
            if (sum < 0) l++;
        }
    }

    return answer;
};

// TC: O(n2)
// SC: O(1)


