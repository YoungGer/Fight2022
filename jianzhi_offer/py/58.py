class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        """按空格分割成单词列表，1.末位单词+空格 2.最后一个单词末位不加空格"""
        if s == [] : return ""
        ls = s.split()  # ['the', 'sky', 'is', 'blue']
        if ls == []: return ""
        res = ""
        for i in range(len(ls)-1): # 少一个，处理末位不加空格
            res += ls[len(ls) - 1 - i] + " "  # 最后一个单词 + 空格  
        res += ls[0] # 末位不加空格
        return res