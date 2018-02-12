# Given two strings s and t, determine whether some anagram
# of t is a substring of s. For example: if s = "udacity"
# and t = "ad", then the function returns True.
# Your function definition should look
# like: question1(s, t) and return a boolean True or False.

# Takes in 2 aruements and checks if they are anagrams

def isAnagram(str1, str2):
    str1_list = sorted(str1)
    str2_list = sorted(str2)
    return (str1_list==str2_list)

def question1(s, t):
    for i in range(len(s)-len(t)+1):
        if isAnagram(s[i: i+len(t)], t):
            return True
    return False

print question1("udacity", "ad")
print question1("udacity", "citys")
print question1("udacity", "ducaity")
print question1("udacity", "ciy")
print question1("udacity", " ")


# Efficiency: O(n)

# Code design:
# The isAnagram function creates two sorted lists and returns
# them equal to eachother

# The question1 function takes a for loop and iterates
# to see if t is a substring of s.
# There for the efficiency is O(n)

# Readability:
# The way I approached this problem was to use pythons sorted
# function to create two sorted lists. Then, create to arguments
# (s, t) to check if t is a substring of s. If this was true
# it would return boolean true and if not return false.