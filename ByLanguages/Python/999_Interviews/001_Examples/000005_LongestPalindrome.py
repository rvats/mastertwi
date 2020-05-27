class Solution:
    def longestPalindrome(self, s: str) -> str:
        palindromeDictionary = {}
        slen = len(s)
        p1 = 0
        p2 = slen-1
        while p2 >= p1:
            if s[p1]!=s[p2]:
                p2-=1
            else:
                if p1!=p2:
                    if self.isPalindrome(s[p1:p2+1]) and s[p1:p2+1] not in palindromeDictionary:
                        palindromeDictionary[s[p1:p2+1]] = len(s[p1:p2+1])
                        p1+=1
                        p2=slen-1
                    else:
                        p2-=1
                else:
                    if s[p1] not in palindromeDictionary:
                        palindromeDictionary[s[p1]] = len(s[p1])
                    p1+=1
                    p2=slen-1
        if len(palindromeDictionary)>0:
            return max(palindromeDictionary,key=palindromeDictionary.get)
        else:
            return ""
    
    def isPalindrome(self, string: str) -> bool:
        return string==string[::-1]
	###############################################
		
	def longestPalindrome(self, s: str) -> str:
        def check(l, r):
            while 0 <= l <= r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l + 1:r]
        pals = [check(i, i) for i in range(len(s))] + [check(i, i + 1) for i in range(len(s) - 1) if s[i] == s[i + 1]]
        return sorted(pals, key = len)[-1] if pals else ''
	###############################################