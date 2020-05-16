# https://ftx.com/volume-monitor
from orders import Order, Ladder


if __name__ == "__main__":
    ladder = Ladder(fills=[Order("10700", "100"), Order("10800", "100")])
    stop = ladder.breakeven()
    pyramid_add = ladder.next_price_add(adjustment="50")
    profit_stop = ladder.next_price_add(adjustment="10")
    print((profit_stop, pyramid_add, stop))

    feeding = False
    while feeding == True:
        if current_bid > pyramid_add:
            # buy(pyramid_add)
            enable('buy', price=pyramid_add)
        if filled:
            pass
