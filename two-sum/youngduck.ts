// 시간복잡도 : 반복문한번에 완결된다 생각하여 O(N)인줄 알았는데 O(N^2)풀이라고 하네요, 해시맵으로 구현하는방법을 추가적으로 학습했습니다.
// 공간복잡도 : O(1) 입력값이 커져도 변수개수는 일정

function twoSum(nums: number[], target: number): number[] {
    // 이중반복문이아니라 투포인터를 둬서 해결
    let left = 0, right = 1;

    while(left<nums.length-1){
        const leftRightSum=nums[left]+nums[right];

        // 조건 만족 탈출
        if(leftRightSum===target){
            break;
        }
        // 조건불만족의 경우 left,right투포인터 어떻게 증가할것인지 처리
        // right가 우선끝으로가고 left를 증가해야할땐 right를 left값으로 이동시키면 O(n)으로 전수 순회가 가능
        else if(right<nums.length-1){ 
            right+=1;
        }
        else{
            left+=1;
            right = left+1;
        }
    }


    return [left,right];
};

