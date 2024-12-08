/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function(nums) {

    // 첫 번째 방법: filter + indexOf 사용 => indexOf(),filter() 각각 시간복잡도 O(n) 두 개가 중첩이므로 시간복잡도 O(n^2)
    // Runtime: Time Limit Exceeded 발생
    const method1 = function() {
            const filterNums = nums.filter((item,index) => nums.indexOf(item) !== index);
            return filterNums.length > 0;
    }

    // 두 번째 방법: Set 사용 => nums 배열을 set으로 변환할 때 한번씩 확인하면 되므로 시간복잡도 O(n)
    // Runtime: 14ms
    const method2 = function() {
        const setNums = new Set(nums);
        return setNums.size !== nums.length;
    }

    // 위 두 가지 방법 중 Set을 사용하는 것이 성능상 훨씬 나음
    return method2();
};
