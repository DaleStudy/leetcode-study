// 시간복잡도 : O(n^2) - 정렬 O(n log n), 숫자 하나를 고정하고 나머지 두 숫자를 투 포인터로 순회
// 공간복잡도 : O(n) - 정렬할 배열을 복사, 결과 배열의 공간은 제외

function threeSum(nums: number[]): number[][] {
  const result: number[][] = [];
  // 합이 크고 작은것에 따라 포인터를 움직이기위해 오름차순 정렬, 원본 배열은 유지
  const sortedNums = [...nums].sort((a,b)=>a-b);

  for(let i = 0; i<sortedNums.length-2; i++){
    // 고정한 숫자가 양수면 뒤의 숫자들도 양수라 합이 0이 될수없음
    if(sortedNums[i]>0){
      break;
    }
    // 같은 숫자를 다시 고정하면 똑같은 조합이 나오므로 건너뜀
    if(i>0 && sortedNums[i]===sortedNums[i-1]){
      continue;
    }

    let left = i+1, right = sortedNums.length-1;

    while(left<right){
      const sum = sortedNums[i]+sortedNums[left]+sortedNums[right];

      if(sum===0){
        result.push([sortedNums[i],sortedNums[left],sortedNums[right]]);
        left+=1;
        right-=1;

        // 방금 넣은 조합과 중복되지않게 양쪽에서 같은 숫자들을 건너뜀
        while(left<right && sortedNums[left]===sortedNums[left-1]){
          left+=1;
        }
        while(left<right && sortedNums[right]===sortedNums[right+1]){
          right-=1;
        }
      }
      else if(sum<0){
        // 합이 작으면 왼쪽 포인터를 옮겨 더 큰 숫자를 선택
        left+=1;
      }
      else{
        // 합이 크면 오른쪽 포인터를 옮겨 더 작은 숫자를 선택
        right-=1;
      }
    }
  }

  return result;
};
