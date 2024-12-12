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
    let temp = 1;

    for(let i = 0; i < nums.length-1; i++) {
        if(nums[i] === nums[i + 1]) {
            // console.log(nums[i], '===', nums[i+1])
            continue;
        } else if(nums[i] + 1 === nums[i + 1] ) {
            // console.log(nums[i], '+ 1 =', nums[i+1])
            temp += 1;
        } else {
            // console.log(longest, ' - ', temp)
            longest = Math.max(temp, longest);
            temp = 1;
        }
    }

    // i가 마지막인 경우 for문의 else문을 타지 않으므로 다시 한번 체크함
    longest = Math.max(temp, longest);
    return longest;
};
