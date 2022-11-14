import string
from random import sample
def get_random_password(n: int) -> str:
    alphabet = string.ascii_uppercase + string.ascii_lowercase + string.digits
    if n > len(alphabet):
        raise ValueError ("Требуемый пароль больше базы символов")
    return "" "".join(sample(alphabet, n))

      # TODO написать функцию генерации случайных паролей



print(get_random_password(8))

