import helpers


def first_task():
    data_list = [42, 'Hello', 3.14, True, None, [1, 2, 3], {'key': 'value'}, (5, 6)]
    print(data_list)


def second_task():
    original_list = [10, 20, 30, 40, 50]
    extracted_list = original_list[1:4]
    print(extracted_list)


for f in {first_task, second_task}:
    helpers.run(f)
