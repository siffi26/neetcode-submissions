class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        note = []
        for token in tokens:
            if token == "+":
                i = note.pop()
                j = note.pop()
                sum_ele = i+j
                note.append(sum_ele)
            elif token == "-":
                i = note.pop()
                j = note.pop()
                diff_ele = j-i
                note.append(diff_ele)
            elif token == "*":
                i = note.pop()
                j = note.pop()
                mul_ele = i*j
                note.append(mul_ele)
            elif token == "/":
                i = note.pop()
                j = note.pop()
                div_ele = int(j/i)
                note.append(div_ele)
            else:
                note.append(int(token))
        return note[0]
            
