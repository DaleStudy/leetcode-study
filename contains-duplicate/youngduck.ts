// 시간복잡도 : new Set은 n번 x add O(1) 인 함수, 즉 배열의 모든 원소를 한번씩 순회하므로 O(n)
// 공간복잡도 : n개의 원소를 Set에 저장하므로 O(n)

function containsDuplicate(nums: number[]): boolean {

    const uniqueNumsSet = new Set(nums);

    return uniqueNumsSet.size !== nums.length;
};

