import string

def alphabet_position(text):
    alphabet = {
        ch: i + 1
        for i, ch in enumerate(string.ascii_lowercase)
    }
    out_string = ""
    
    for ch in text.lower():
        if ch in alphabet:
            out_string += str(alphabet[ch])
            out_string += " "
    
    return out_string[:len(out_string) - 1]
            
print(alphabet_position("The sunset sets at twelve o' clock."))