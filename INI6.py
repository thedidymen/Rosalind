__author__ = 'Reijer'

def get_frequency_dict(sequence):
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq

def sentencetolist(s, n=0):
    return s.split(" ")
    # if s == "" or len(s)== n:
    #     return []
    # elif s[n] == " ":
    #     return [s[:n]] + sentencetolist(s[n+1:])
    # else:
    #     n += 1
    #     return sentencetolist(s, n)

def test():
    s = "When I find myself in times of trouble Mother Mary comes to me Speaking words of wisdom let it be And in my hour of darkness she is standing right in front of me Speaking words of wisdom let it be Let it be let it be let it be let it be Whisper words of wisdom let it be And when the broken hearted people living in the world agree There will be an answer let it be For though they may be parted there is still a chance that they will see There will be an answer let it be Let it be let it be let it be let it be There will be an answer let it be Let it be let it be let it be let it be Whisper words of wisdom let it be Let it be let it be let it be let it be Whisper words of wisdom let it be And when the night is cloudy there is still a light that shines on me Shine until tomorrow let it be I wake up to the sound of music Mother Mary comes to me Speaking words of wisdom let it be Let it be let it be let it be yeah let it be There will be an answer let it be Let it be let it be let it be yeah let it be Whisper words of wisdom let it be"
    freq = get_frequency_dict(sentencetolist(s))
    for key, value in freq.items():
        print key,
        print value

if __name__ == '__main__':
    test()