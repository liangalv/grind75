class Solution:
    def isPalindrome(self, s: str) -> bool:
        start, end = 0, len(s)-1
        while start != end:
            head = s[start].lower()
            tail = s[end].lower()
            if head.isalnum() and tail.isalnum():
                if head != tail:
                    return False
                #increment both by one as they are the same 
                start += 1
                end += 1
            if not head.isalnum():
                start += 1
            if not tail.isalnum():
                end += 1
        return True
            
            