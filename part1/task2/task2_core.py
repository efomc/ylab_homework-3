from time import sleep


def exponent_sleep(call_count, start_sleep_time, factor, border_sleep_time):
    def exponent_sleep_decorator(func):
        def _wrapper(*args, **kwargs):
            print("Начало работы")
            t = start_sleep_time
            for index in range(1, call_count + 1):
                sleep(t)
                result = func(*args, **kwargs)
                print(
                    f"Запуск номер {index}. Ожидание {t} секунд. "
                    f"Результат декорируемой функции = {result}."
                )
                t *= 2 ** factor
                if t >= border_sleep_time:
                    t = border_sleep_time
            print("Конец работы")

        return _wrapper

    return exponent_sleep_decorator
