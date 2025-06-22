

def square_result(func):
    def wrapper(a, b):
        result = func(a, b)
        return result * result
    return wrapper


@square_result
def add(a, b):
    return a + b

print(add(2, 3))


def check_user(user):
    def decorator(func):
        def wrapper():
            if user == "admin":
                func()
            else:
                print("Доступ запрещен, Только для admin")
        return wrapper
    return decorator

@check_user("admin")
def delete_database():
    print("База данных удалена")

@check_user("guest")
def delete_logs():
    print("Логи удалены")

delete_database()
delete_logs()