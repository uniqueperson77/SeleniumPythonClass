#paper,tape,stickers,ribbons
#process finsihed


def my_decorator(func_name):
    def f1():
        print("Ready with paper,tape,stickers,ribbons.")
        func_name()
        print("Packing process.")
    return f1


@my_decorator
def gift():
    print("This is gift")

gift()