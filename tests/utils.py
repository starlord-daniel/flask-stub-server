import random
import string


def get_random_string(num_letters: int) -> str:
    '''Return a random string of ascii letters with length "num_letters" '''
    random_string = ''.join(random.choice(string.ascii_letters) for _ in range(num_letters))
    return random_string
