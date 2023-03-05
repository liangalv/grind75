class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #the naive implementaiton would be to generate two histograms that count up each letter and return if they are the same 
        #we can do some quick tests such as comparing the length to determine it's possible for them to be the same length 
        if len(s) != len(t):
            return False
        #generate histogram 1
        s_histogram = dict()
        t_histogram = dict() 
        print(type(s_histogram))
        for char in s: 
            s_histogram[char] = s_histogram.get(char,0) + 1
        for char in t:
            t_histogram[char] = t_histogram.get(char,0) + 1
        
        return s_histogram == t_histogram
            