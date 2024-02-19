class Solution:
    def balancedString(self, s: str) -> int:
        n = len(s) // 4
        target_counter = Counter(s)
        extras = {char: max(0, count - n) for char, count in target_counter.items()}
        
        if not any(extras.values()):
            return 0
        
        i = 0
        res = len(s)
        
        for j, char in enumerate(s):
            if char in extras:
                extras[char] -= 1
            
            while all(val <= 0 for val in extras.values()):
                res = min(res, j - i + 1)
                if s[i] in extras:
                    extras[s[i]] += 1
                i += 1
                
        return res
