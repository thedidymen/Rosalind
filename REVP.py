__author__ = 'Reijer'

DNA =  {"A": "T", "T": "A", "C": "G", "G": "C"}

def load_file():
    """
    Takes DNA strings in FASTA format in txt file
    Returns a strings.
    """
    print "Loading IDs and DNA strings from file..."
    # inFile: file
    inFile = open("rosalind_revp.txt", 'r')
    file = {}
    key = ""
    for line in inFile:
        if line[0] == ">":
            if key != "":
                file[key[1:]] = item
            key = line.strip()
            item = ""
        else:
            item += line.strip()
    file[key[1:]] = item
    print "  ", len(file), "DNA strings loaded."
    return file.get(key[1:])

def reversecomplement(s):
    if s[0] == DNA.get(s[-1]):
        return True
    else:
        return False

def main():
    counter = 0
    string = load_file()
    print string
    for i in range(len(string)-3):                                  # index of every possible starting position
        if len(string[i:])+1 < 13:                                  # checks that the maximum length of search string
            max = len(string[i:])+1                                 # does not exceeds length of string
        else:
            max = 13                                                # max 13 so it includes 12
        for j in range(4, max, 2):                                  # by default palindrome needs to be even
            rc = True
            for k in range(j/2):                                    # walks by half of ever letter of search string
                if not reversecomplement(string[i+k:i+j-k]):        # check if elements of search string matches its reverse complement
                    rc = False
            if rc == True:
                counter += 1
                print i+1, j#, string[i:j+i]
    print counter

if __name__ == '__main__':
    main()