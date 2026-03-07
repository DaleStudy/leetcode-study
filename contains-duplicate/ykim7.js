// Input: number[]
// Output: boolean

// 배열은 sorting되어 있지 않음.
// Idea 1 : 이중 for loop으로 모든 값 비교 - O(n^2)
// Idea 2 : nums를 sort 한 후 앞에서부터 두개씩 비교. 정렬 - O(nlogn)
// Idea 3 : Hash table 로 추가하면서 저장. O(n) 검색 O(1) - O(n)

const found_num = new Set();

for (let i = 0; i < nums.length; i++) {
    if (found_num.has(nums[i])) {
        return true;
    } else {
        found_num.add(nums[i]);
    }
}
return false;
