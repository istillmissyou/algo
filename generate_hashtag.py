def generate_hashtag(s: str):
    result = '#' + ''.join(word.capitalize() for word in s.split())
    return result if 1 < len(result) <= 140 else False

    
generate_hashtag(" Hello there thanks for trying my Kata")
generate_hashtag("  ")