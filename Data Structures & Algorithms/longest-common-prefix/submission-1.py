class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort(key=len)
        output = []
        for i in range(len(strs[0])):
            for j in strs[1:]:
                if strs[0][i] != j[i]:
                    return "".join(output)
            output.append(strs[0][i])    
        return "".join(output)