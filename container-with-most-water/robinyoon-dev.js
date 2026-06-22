/**
 * @param {number[]} height
 * @return {number}
 */
var maxArea = function (height) {

    // 투 포인터
    // 왼쪽 포인터, 오른쪽 포인터. lower 라인의 포인터를 움직여야함.

    let leftPointer = 0;
    let rightPointer = height.length - 1;
    let tempMax = 0;

    while (leftPointer !== rightPointer) {
        let areaHeight = Math.min(height[leftPointer], height[rightPointer]);

        let areaWidth = rightPointer - leftPointer;

        let waterArea = areaHeight * areaWidth;

        tempMax = Math.max(tempMax, waterArea);

        if (height[leftPointer] < height[rightPointer]) {
            leftPointer++;
        } else {
            rightPointer--;
        }
    }

    return tempMax;

};
