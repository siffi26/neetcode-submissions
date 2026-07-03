class Solution:

    def encode(self, strs: List[str]) -> str:
        # edge case: [""] expected [""] and input: [] expected []
        if not strs: # list empty []
            return ""
        elif len(strs) == 1 and strs[0] == "":
            return "_____"
        else:
            final_string = "||||".join(strs)
            print(final_string)
            return final_string

    def decode(self, s: str) -> List[str]:
        if s == "":
            return []
        if s == "_____":
            return [""]
        
        strs = s.split("||||")
        return strs
