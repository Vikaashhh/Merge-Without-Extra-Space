# 🚀 Day 27 - Merge Without Extra Space

## Challenge:
You're given two sorted arrays a[] and b[] of sizes n and m respectively. Your task is to merge both arrays in a sorted manner without using any extra space.

Update array a[] to contain the first n sorted elements, and array b[] to contain the last m sorted elements.

---

## 🧠 Approach
- Swap & Sort:

- Compare the largest element in a[] with the smallest in b[].

- If a[i] > b[j], swap them.

- After processing, sort both arrays individually.

---

## Why it works:

- Swapping ensures the bigger elements move to b[], and smaller to a[].

- Final sort ensures both arrays are independently sorted and together form a merged sorted array.

---

## 💡 Key Concepts
- In-place Merging

- Two-pointer Technique

- Sorting without Extra Space

---

## 📊 Time & Space Complexity
Time: O((n + m) log(n + m)) → due to sorting

Space: O(1) → no extra space used

---

## 🏁 Conclusion
This is a classic interview problem testing your ability to manipulate arrays efficiently and minimize space usage. Mastering in-place operations is key for optimal coding performance.

