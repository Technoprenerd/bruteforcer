#all combinations of strings - project
#This will output all cominations/bruteforce the alfabet, to make a dictionary bruteforce.

string = ""
alfabet = "abcdefghijklmnopqrstuvwxyz"
que = []
stack = []

string += alfabet

def permute2(s):
    res = []
    if len(s) == 1:
        res = [s]
    else:
        for i, c in enumerate(s):
            for perm in permute2(s[:i] + s[i+1:]):
                res += [c + perm]

    return res

print permute2(string)
