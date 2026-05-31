/**
	Stack을 활용한 방식
	문자열 s의 길이 -> N
	시간 복잡도 : O(N)
	공간 복잡도 : O(N)
*/
class Solution {
    public boolean isValid(String s) {
        boolean result= true;
        Stack<Character> sta=new Stack<>();
        Map<Character,Character> map=new HashMap<>();
        map.put('}','{');
        map.put(']','[');
        map.put(')','(');
        for(int i=0; i<s.length();i++){
            char ch=s.charAt(i);
            if(ch == '(' || ch == '[' || ch == '{'){
                sta.push(ch);
                continue;
            }
            char target=map.get(ch);
            if(sta.isEmpty()){
                result=false;
                break;
            }
            if(!(sta.peek() == target)){
                result=false;
                break;
            }
            sta.pop();
        }
        if(!sta.isEmpty()){
            result=false;
        }
        return result;    
    }
}
