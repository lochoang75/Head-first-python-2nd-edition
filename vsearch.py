def search4vowels(phrase: str) ->set:
    """Display any vowels found in an asked-for word."""
    vowels = set('aeiou')
    return vowels.intersection(set(phrase))


def search4vowels(phrase: str, letter: str='aeiou') -> set:
    """Return a set of the 'letter' found in phrase"""
    return set(letter).intersection(set(phrase))
