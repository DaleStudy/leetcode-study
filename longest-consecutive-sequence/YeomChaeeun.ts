/**
 * 가장 긴 연속의 시퀀스 구하기
 * @param nums
 */
function longestConsecutive(nums: number[]): number {

    // length 가 0, 1 인 경우
    if(nums.length < 2)
        return nums.length; // 0, 1

    // 정렬
    nums = nums.sort((a, b) => a - b)

    // 접근 (1) 처음 연속된 count만 리턴함 =============
    // let count = 1
    // for(let i = 0; i < nums.length-1; i++) {
    //     if(nums[i] === nums[i+1]) {
    //         continue;
    //     } else if(nums[i] - nums[i+1] === 1) {
    //         count++;
    //     } else {
    //         break;
    //     }
    // };
    // console.log(count);
    // return count;

    // =========

    let longest = 0;
    let current = 1;
    for(let i = 0; i < nums.length-1; i++) {
        if(nums[i] === nums[i - 1]) {
            continue;
        } else if(nums[i] + 1 === nums[i + 1] ) {
            current += 1;
        } else {
            longest = Math.max(current, longest);
            current = 1;
        }
    }

    return longest;
};
