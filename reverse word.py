class Solution:
    def reverseWords(self, s):
        # code here
        striped = s.strip(".")
        splited = striped.split(".")
        temp = -1
        reverse = []
        for i in range(len(splited)):
            if len(splited[temp]) is not 0:
                reverse.append(splited[temp])
            temp -= 1
            
        return ".".join(reverse)
