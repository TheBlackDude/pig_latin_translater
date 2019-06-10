
def startwith_vowel(word: bool) -> bool:
    for l in 'aeiou':
        if word.startswith(l): return True
    return False

def translate_word(word: str) -> str:
    pyg = 'ay'

    if word and word.isalpha():
        title = word.istitle()
        word = word.lower()
        if startwith_vowel(word):
            if title: return word.title() + pyg
            return word + pyg
        if title: return word[1:].title() + word[0] + pyg
        return word[1:] + word[0] + pyg
    return word
