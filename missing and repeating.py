class Solution:
    def findTwoElement(self, arr):
        dic = {}
        li = []
        for num in arr:
            if num in dic:
                dic[num] += 1
            else:
                dic[num] = 1
        # print(dic)
        d = max(dic.items(), key = lambda x : x[1])
        li.append(d[0])
        # print(li)
        for num in range(1,len(arr)+1):
            # print(num)
            if num not in arr:
                # print(num)
                li.append(num)
        return li
