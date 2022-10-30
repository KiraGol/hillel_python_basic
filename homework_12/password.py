import re


def check_password(data: str) -> str:
    """
    checks password with requirements
    """
    result = (len(data) > 8,
              re.search(r'[a-z]', data),
              re.search(r'[A-Z]', data),
              re.search(r'[0-9]', data),
              re.search(r'[d_$#@+=-]', data))
    if len(data) < 8:
        raise ValueError("Not correct length of password")
    if re.search(r'[a-z]', data) is None:
        raise ValueError("Do not have a-z symbols")
    if re.search(r'[A-Z]', data) is None:
        raise ValueError("Do not have A-Z symbols")
    if re.search(r'[0-9]', data) is None:
        raise ValueError("Do not have 0-9 numbers")
    if re.search(r'[d_$#@+=-]', data) is None:
        raise ValueError("Do not have characters in password $#-@+=")
    if all(result) is True:
        return "Password is correct"


print(check_password("JHfffHJJU000677)600U"))
