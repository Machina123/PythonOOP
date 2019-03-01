import coinclass

if __name__ == '__main__':
    coin = coinclass.Coin()
    print("Simulating 15 throws...")
    for i in range(15):
        coin.throw()
        print(f"Throw #{i + 1}: {coin.show_side()}")
    print("Finished")
