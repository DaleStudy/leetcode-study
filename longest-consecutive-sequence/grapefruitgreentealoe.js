
/**
 * 정수 배열 nums
 * 가장 많이 연속되는 요소의 길이 리턴.
 * O(n) 시간안에 돌아가는 알고리즘 사용할것.
 */
/*우선 처음 푼 방법은*/

var longestConsecutive = function(nums) {
    let maxCount = 0;
    nums = [...nums].sort((a,b)=>a-b);
    for(let i = 0;i < nums.length;i++){
        let current = nums[i];
        let count = 1;
        for(let j = i+1;j<nums.length;j++){
            if(current+1 == nums[j]){
                current = nums[j]
                count +=1;
            }else if(current == nums[j]){
                continue;
            }
        }
        maxCount = Math.max(maxCount,count)
        count = 1;
    }
    return maxCount
};


/*시간복잡도:
2중for문+sort
n^2 + nlogn => n^2.
공간복잡도:
nums는 초기화했고,
기타 변수들만 사용을 했다(maxCount,current,count)=> O(1)

하지만 이문제는 O(n)의 시간복잡도를 가져가야한다.
그러려면 sort도 하지말아야하고, 2중for문을 쓰지도 말아야한다.
(생각해보니 내가 사용한 방법을 인덱스+1해서 해결해도 되긴한다. 그래도 정렬때문에 nlogn이 된다.)

두번째 방법으로는,set을 사용해서 중복을 제거하는 방법이다.
*/

/**
 * @param {number[]} nums
 * @return {number}
 */
var longestConsecutive = function(nums) {
    if(nums.length == 0) return 0
    let maxCount = 1;
    nums.sort((a,b)=>a-b);
    nums = [...new Set(nums)];
    let count = 1;
    for (let i = 0; i < nums.length - 1; i++) {
        if (nums[i] + 1 === nums[i + 1]) {
            count += 1;
        } else if (nums[i] === nums[i + 1]) {
            // 중복일 경우 아무것도 안 하고 넘어감
            continue;
        } else {
            maxCount = Math.max(maxCount, count);
            count = 1;
        }
    }
    maxCount = Math.max(maxCount, count); // 마지막에도 비교 필요

    return maxCount
};
/*sort할때 시간복잡도가 nlog(n)인데 왜 통과했지.. 빅오 계산법이 최악의 경우를 계산한거라, 운좋게 통과한 것 같다.
좀 더 최적화 해보자
*/

/**
 * @param {number[]} nums
 * @return {number}
 */
var longestConsecutive = function(nums) {
    const numsSet = new Set(nums);
    let maxCount = 0;
    for(let num of numsSet){
        //중복된 계산 패스
        if(numsSet.has(num-1)) continue;
        let length = 1;
        while(numsSet.has(num+length)){
            length++
        }
        maxCount = Math.max(maxCount,length)
    }
    return maxCount
};

/*
set을 이용해서 중복을 제거
set의 has메소드를 활용하여 조회 최적화
while을 썼지만, for문의 첫번째 if문을 통해 실제 수행은 O(n)의 시간복잡도를 가짐.
이 외에도, set으로 만든 다음에 삭제해가면서(while) 순회가 아닌, 왼쪽 오른쪽값들을 연속적으로(while) 지우고, 연속이 끝나면 pop에서 나온 값의 left right를 조회해서 없으면 다시 최대값과 비교하는 방식이 있다.
근데 위의 코드에서 has로 조회하나, remove를 하려면 어차피 또 조회해야하니,
성능상의 차이는 크게 없는 것 같다.
*/