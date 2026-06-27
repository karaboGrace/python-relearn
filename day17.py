def encode(strs):
        """Encodes a list of strings to a single string.
        """
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res
#def decode(s):
# res = []
  # i = 0
    #while i < len(s):
        # Step 1: find where the '#' is, starting from position i
        # Step 2: extract the length-prefix (characters from i up to the '#'), convert to int
        # Step 3: figure out where the actual string content starts (just after '#')
        # Step 4: slice out exactly `length` characters from there
        # Step 5: append that string to res 
        # Step 6: move i forward, past the string you just extracted
        j = i
# return res


def decode(s):
    res = []
    i = 0
    while i < len(s):
        j = i
        while s[j] != "#":
            j += 1
        length = int(s[i:j])
        start = j + 1
        end = start + length
        res.append(s[start:end])
        i = end
    return res
