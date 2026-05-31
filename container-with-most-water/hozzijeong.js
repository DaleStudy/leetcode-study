/**
 * @param {number[]} height
 * @return {number}
 */
var maxArea = function(height) {
    // x축이 가장 길면서 y축 역시 가장 높은 즉 높이가 가장 높은 값을 찾으라는 의미.
    // startIndex값과 그 값에 해당하는 height를 받고
    // endIndex의 값과 그 값에 해당하는 height를 받는다.
    // 여기서 가장 큰 점은 startIndex와 endIndex가 멀면 멀수록 좋다
    // 그리고 그 값을 하나씩 줄여가면서 더 큰 값을 찾아 적용한다
  
    let max = 0;

    let startIndex = 0;
    let endIndex = height.length -1;

    while(startIndex < endIndex){
        const startHeight = height[startIndex];
        const endHeight = height[endIndex];

        const xLength = endIndex - startIndex;
        const minHeight = Math.min(startHeight, endHeight);

        const size = xLength * minHeight;

        max = Math.max(size,max);

        if(startHeight >= endHeight){
            endIndex -=1;
        }else{
            startIndex +=1;
        }
    };

    return max
};
