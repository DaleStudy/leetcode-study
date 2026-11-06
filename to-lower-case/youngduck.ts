// 시간복잡도 : O(n) - toLoserCase 메서드는 문자열의 모든문자를 한번씩 순회
// 공간복잡도 : O(n) - JavaScript의 문자열은 불변이므로 들어온값 그대로의 길이인 n의 문자열 생성
function toLowerCase(s: string): string {

    return s.toLowerCase();
    
};