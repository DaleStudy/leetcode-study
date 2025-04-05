/**
 *
 * 연속된 숫자의 최대 길이를 구하는 문제
 * @param {number[]} nums
 * @return {number}
 *
 * 풀이
 *
 * nums 배열을 중복을 제거하고 오름차순으로 정렬한다.
 * 중복을 제거하고 정렬한 배열을 순회하면서 연속된 숫자의 길이를 구한다.
 */

function longestConsecutive(nums: number[]): number {
    if (nums.length === 0) return 0;
    const sortNum = Array.from(new Set(nums)).sort((a, b) => a - b);

    if (sortNum.length === 1) return 1;

    const resultArray : number[] = []
    let count = 1;

    for(let i=0; i<sortNum.length-1; i++){
        const prevNum = sortNum[i];
        const nextNum = sortNum[i+1];

        if(prevNum +1 === nextNum){
            count ++;
        }else{
            resultArray.push(count)
            count =1;
        }
    }
    resultArray.push(count);

    return resultArray.length > 0 ? Math.max(...resultArray) : 1;
};
