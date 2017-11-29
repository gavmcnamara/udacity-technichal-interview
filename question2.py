# Given a string a, find the longest palindromic
# substring contained in a. Your function definition
# should look like question2(a), and return a string.

def question2(a):
    # if a has no value there is no runtime errors
    if a <= "":
        return a
    # Create an empty string to store pargest palendrome
    lng_palendrome = ""
    for i in range(len(a)):
        for x in range(i):
            substring = a[x: i+1]
            if substring == substring[::-1]:
                if len(substring) > len(lng_palendrome):
                    lng_palendrome = substring

    # if the number of palendromes is zero this will run
    if len(lng_palendrome) == 0:
        print a, "is not a palendrome"
    return lng_palendrome

print question2("abcracecarfef")
print question2("aba")
print question2("abbaaba")
print question2("")
print question2("sadasljdlka1234554321sjksdjljf")
print question2("ab")

# Efficiency: O(n^2), this is because of the two for loops
# the first for loop is equal to O(n) and the second is
# equal to O(n). So combined it is O(n^2)

# Code Design: this function will detect a palendrome in
# string a and find the longest outcome. This will also
# see if there is no palendromes and print out the input
# with a statement declaring this is not a palendrome