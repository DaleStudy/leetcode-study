/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */

 /**
  * map을 통해 문자의 개수를 저장하고, 두 문자열의 문자 개수를 비교해서 다른 값이 있다면 false를 반환하도록 풀이를작성했습니다
  *
  */
var isAnagram = function(s, t) {
    if(s.length !== t.length) return false;

    const length = s.length;

    const stringMap = new Map();
    const targetMap = new Map();

    for(let i = 0; i < length; i ++){

        const stringChar = s[i];
        const currentStringMap = stringMap.get(stringChar);
        
        if(currentStringMap){
            stringMap.set(stringChar, currentStringMap + 1)
        }else{
            stringMap.set(stringChar, 1)
        }

        const targetChar = t[i];
        const currentTargetMap = targetMap.get(targetChar);

        if(currentTargetMap){
            targetMap.set(targetChar, currentTargetMap + 1)
        }else{
            targetMap.set(targetChar, 1)
        }
    }

    for(const [char, count] of [...stringMap]){
        const targetCount = targetMap.get(char);

        if(!targetCount) return false;
        if(targetCount !== count) return false;
    }
    
    return true
};
