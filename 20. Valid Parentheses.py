'''20. Valid Parentheses
'""Example:
Input: s = "()"

Output: true'''
class Solution:
    def isValid(self, s: str) -> bool:
        s=list(s)
        l=[]
        for i in s:
            if i in "({[":
                l.append(i)
            else:
                if len(l)==0:
                    return False
                else:
                    top=l.pop()
                    if (i=="}"and top!="{") or (i==")" and top !="(")or(i=="]" and top!="["):
                        return False
        else:
            if len(l)==0:
                return True
            else:
                return False
