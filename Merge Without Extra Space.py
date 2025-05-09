class Solution:
    def mergeArrays(self, a, b):
        # Dono arrays ke last elements se start karenge
        n = len(a)
        m = len(b)
        i = n - 1
        j = 0
        
        # Jab tak a ka last aur b ka first compare kar sakte hain
        while i >= 0 and j < m and a[i] > b[j]:
            # Swap karenge agar a[i] b[j] se bada ho
            a[i], b[j] = b[j], a[i]
            i -= 1
            j += 1
        
        # Ab dono arrays ko sort karenge taaki final merged sorted ho
        a.sort()
        b.sort()
