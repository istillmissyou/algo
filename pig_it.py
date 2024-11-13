def pig_it(text: str):
    words = text.split(' ')
    result = []
    for word in words:
        if word.isalpha():
            result.append(f'{word[1:]}{word[0]}ay')
        else:
            result.append(word)
    return ' '.join(result)

def pig_it(text: str) -> str:
    return ' '.join(f'{word[1:]}{word[0]}ay' if word.isalpha() else word for word in text.split())

pig_it('Pig latin is cool')
pig_it('Hello world !')