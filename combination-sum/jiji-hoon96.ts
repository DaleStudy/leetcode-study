/**
 * 
 * @param candidates 
 * @param target 
 * 
 * backtracking 알고리즘으로 문제 해결 
 * 
 */

function combinationSum(candidates: number[], target: number): number[][] {
    const result : number[][] = [];
    if(candidates.length === 0){
        return result ;    
    }

    candidates.sort((a,b)=> a-b);

    const validCandidates : number[] = candidates.filter(num => num <= target);

    if(validCandidates.length ===0) {
        return result;
    }

    const currentCombination : number[] = [];

    function backtrack (startIndex : number, remainingTarget : number) :void {
        if(remainingTarget === 0){
            result.push([...currentCombination]);
            return;
        }

        for(let i=startIndex; i<validCandidates.length; i++){
            const currentNum = validCandidates[i];

            if(currentNum > remainingTarget) {
                break;
            }
            currentCombination.push(currentNum);

            backtrack(i,remainingTarget - currentNum)

            currentCombination.pop()            

        }
    }

    backtrack(0, target);
    return result;
  };
