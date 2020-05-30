# Complete the howManyGames function below.
def howManyGames(price, difference, minimum_price, total_sum_available):
    """
    :rtype: int
    """
    game_purchased = 0
    current_price = price

    while total_sum_available > current_price:
        game_purchased += 1
        total_sum_available -= current_price
        if current_price - difference >= minimum_price:
            current_price -= difference
        else:
            current_price = minimum_price

    return game_purchased


print(howManyGames(10, 10, 0, 20))
