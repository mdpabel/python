# https://codingbat.com/prob/p129981

def make_out_word(out, word):
    n = len(out)
    return out[:n/2] + word + out[n/2:]
