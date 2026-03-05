/**
 * @param {number[]} nums
 * @return {number}
 */
var longestConsecutive = function (nums) {

    //엣지케이스: 빈배열인 경우
    if (nums.length === 0) {
        return 0;
    }

    //Set으로 중복값 제거하기
    const numsSet = new Set(nums);

    let tempMaxLength = 1;

    for (num of numsSet) {
        let startPoint = num - 1;
        let hasStart = numsSet.has(startPoint);

        //!hasStart인 num이 첫번째에 와야할 수니까!
        if (!hasStart) {

            let currentLength = 1;

            while (numsSet.has(num + currentLength)) {
                currentLength++;
            }
            // max 찾기
            tempMaxLength = Math.max(currentLength, tempMaxLength);
        } else {
            continue;
        }
    }

    return tempMaxLength;

};
