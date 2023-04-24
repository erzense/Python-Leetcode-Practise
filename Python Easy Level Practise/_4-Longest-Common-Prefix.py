"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

"""

def longestCommonPrefix(strs = ["flower","flow","flight"]):
    strs_prefixes = []
    strs_prefixes_db = []
    isCommonPrefix = False
    for i in strs:
        for x in range(1,len(i)+1):
            strs_prefixes.append(i[0:x])
    
    for p in strs_prefixes:
        if strs_prefixes.count(p) == 3:

            isCommonPrefix = True
            strs_prefixes_db.append(p)          
        else:
            pass
            
   
    if (isCommonPrefix):
        print(f"Longest Common Prefix in {strs} : ",max(strs_prefixes_db, key=len))
    else:
        print("There is no common prefix among the input strings.")

    

longestCommonPrefix()