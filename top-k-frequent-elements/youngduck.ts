// N은 nums의 길이, M은 서로 다른 숫자의 개수
// 시간복잡도 : O(N + M log M) - N개 원소의 빈도를 세고, M개 항목을 빈도순으로 정렬
// 공간복잡도 : O(M) - 서로 다른 숫자의 빈도를 Map에 저장하고 M개 항목의 배열 생성

function topKFrequent(nums: number[], k: number): number[] {
    
    // 숫자를 key, 등장 횟수를 value로 저장
    const FrequentMap = new Map<number,number>();

    for(const i of nums){
        if(FrequentMap.has(i)){
            // 이미 등장한 숫자는 횟수 증가. has로 확인했으므로 get의 결과가 undefined가 아님
            FrequentMap.set(i,FrequentMap.get(i)!+1);
        }
        else{
            // 처음 등장한 숫자는 1로 초기화
            FrequentMap.set(i,1);
        }
    }


    return [...FrequentMap.entries()] // Map을 [숫자, 등장 횟수] 쌍의 배열로 변환
        .sort((a,b)=>b[1]-a[1]) // 등장 횟수를 기준으로 내림차순 정렬
        .slice(0,k) // 가장 많이 등장한 k개 항목 선택
        .map(([num])=>num); // 등장 횟수를 제외하고 숫자만 반환
};

