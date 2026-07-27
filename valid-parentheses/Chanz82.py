class Solution:
    def isValid(self, s: str) -> bool:
        ch_stack = []
        ch_map = {}
        
        ch_map[")"] = "("
        ch_map["}"] = "{"
        ch_map["]"] = "["

        for ch in s:
            if ch == ")" or ch == "}" or ch == "]":
                if not ch_stack:
                    return False
                if ch_stack.pop() != ch_map[ch]:
                    return False
            else:
                ch_stack.append(ch)

        return not ch_stack
      
