import string
import random


class Utils:

    def generate_random_string(N):
        return ''.join(random.choices(string.ascii_uppercase +
                                      string.digits, k=N))
