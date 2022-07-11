def cashier(func):
    old_data_dict = {}

    def _wrapper(*args):
        if args in old_data_dict:
            result = old_data_dict[args]
        else:
            result = func(*args)
            old_data_dict[args] = result
        return result
    return _wrapper


@cashier
def multiplier(number: int):
    return number * 2
