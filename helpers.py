def start_task():
    print(f"\ntask---> start\n")


def end_task():
    print(f"\n\tend <---task\n")


def run(func):
    start_task()
    func()
    end_task()
    print("\n")
