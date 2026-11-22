// 시간복잡도 : O(1) - n과 상관없이 문제의 최대 계단수인 45까지 고정된 횟수만 계산
// 공간복잡도 : O(1) - 길이가 46인 고정된 배열 사용
// 최대 계단수 대신 n까지 계산하고 n+1 크기의 배열을 만들면 시간, 공간복잡도 모두 O(n)

function climbStairs(n: number): number {
    // 누적 합이라 해야하나 결국 N STEP까지 구하는거는 N-1, N-2스텝의 경우의 수를 합해주면됨
    const arr = [...new Array(46)].map((iitem)=>0);

    // 0칸은 아무것도 하지않는 경우 1개, 1~3칸은 직접 구한 경우의 수로 초기화
    arr[0]=1;
    arr[1]=1;
    arr[2]=2;
    arr[3]=3;
   
   for(let i =4; i<=45; i++){
    arr[i]=arr[i-2]+arr[i-1];
   }

    
    return arr[n];
};
