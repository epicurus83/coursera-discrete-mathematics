def change(amount):
    if amount is None or amount < 24 or amount > 1000:
        raise ValueError('"' + str(amount) + '" must be a integer between 24 and 1000')

    return _get_change(amount)


def _get_change(amount):
    if amount % 7 == 0:
        return [7] * int(amount/7)

    coins = _get_change(amount - 5)
    coins.append(5)
    return coins
