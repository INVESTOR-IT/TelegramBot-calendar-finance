from re import search


async def check_login(login: str) -> bool:
    try:
        login.split('@')[1].index('.')
    except:
        return False
    return True


async def check_password(password: str) -> bool | str:
    if len(password) < 8:
        return 'Пароль состоит меньше 8 символов'
    if not search(r'[A-Z]', password):
        return 'Отсуствует заглавной буквы'
    if not search(r'[a-z]', password):
        return 'Отсуствует строчной буквы'
    if not search(r'[0-9]', password):
        return 'Отсуствуеют цифры'
    return True
