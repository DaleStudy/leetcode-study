

/*
회전한 데이터에서 제일 작은 값을 찾는 문제라는 것을 기억해야한다.
그렇게 때문에, left, right를 각각 0, nums.length -1 로 두어서, left와 right가 같아질때 탈출하고, 그 같아진 index에 대한 nums[index]를 찾아내면 될 것 같다.
*/
/**
 * 
 * @param {*} nums 
 * @returns 
 */
function findMin(nums) {
    let left = 0;
    let right = nums.length - 1;

    while (left !== right) {
        let mid = Math.floor((left + right) / 2);

        if (nums[mid] > nums[right]) {
            // 최소값은 오른쪽에 있다
            left = mid + 1;
        } else {
            // 최소값은 왼쪽 구간에 있다 (mid도 포함 가능)
            right = mid;
        }
    }

    return nums[left]; // 또는 nums[right]도 같음
}
//시간복잡도 : 이진탐색을 썼으므로 O(logn)
//공간복잡도 : O(1)