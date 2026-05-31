// input: array of integers [2,7,11,5], integer 9
// output: indices [0,1]

// 모든 배열의 쌍을 확인하면 시간복잡도가 O(n * n)이 됨.
// 배열의 요소와 인덱스를 함께 저장.

var twoSum = function (nums, target) {
    const indices = {};
    for (let i = 0; i < nums.length; i++) {
        indices[nums[i]] = i;
    }

    for (let i = 0; i < nums.length; i++) {
        let remainder = target - nums[i];
        if (indices[remainder] !== undefined && indices[remainder] !== i) {
            return [i, indices[remainder]];
        }
    }
};

// Time Complexity: O(n) + O(n) = O(n)
// Space Complexiy: O(n)
