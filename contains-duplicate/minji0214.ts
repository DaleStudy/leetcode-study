function containsDuplicate(nums: number[]): boolean {
    let answer = false
  for(let i = 0; i< nums.length; i ++ ){
    if(nums.findIndex((value)=> value === nums[i]) !== i){
        answer = true
        break;
     }
    }  
    return answer
};
//-> time limit 초과 오류 발생
//시간복잡도
// for + findIndex	O(n²) ❌
// for + Set or Map	O(n) ✅
//중복 여부만 체크할 때는 무조건 Set을 쓰는 게 효율적
// includes, findIndex, indexOf는 절대 루프 안에서 쓰지 말것 — O(n²) 
function containsDuplicate(nums: number[]): boolean {
	const seen = new Set(); //지금까지 본 숫자들을 저장 
	for (const num of nums) {
		if (seen.has(num)) return true; // 중복 발견 
		seen.add(num); // 중복이 아닐 경우 추가 
	}
	return false; // 중복 없음
}
//Set : 중복 없는 값을의 모음. 배열처럼 생겼지만, 중복을 허용하지 않음 (중복제거)
//Map : key → value 형태로 저장하는 객체 (검색 수정)

