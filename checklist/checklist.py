# print("Hello World")

# checklist = list()
# checklist 

# def my_fun_function(say_this):
#     print(say_this)

# my_fun_function('Hello World')

checklist = list()
# checklist.append('Blue')
# print(checklist)
# checklist.append('Orange')
# print(checklist)

def create(item):
    checklist.append(item)

def read(index):
    return checklist[int(index)]

def update(index, item):
    checklist[index] = item

def destroy(index):
    checklist.pop(index)

def list_all_items():
    index = 0
    for item in checklist:
        print(str(index) + ' - ' + item)
        index += 1

def mark_complete(index):
    item = "√ " + checklist[index]
    update(index, item)

def mark_incomplete(index):
    item = checklist[index]
    print(item)
    item.replace("√","X")
    print(item)
    update(index, item)

def select(function_code):
    if function_code == "C":
        item_input = input("Input Item: ")
        create(item_input)
        print(checklist)

    elif function_code == "R":
        index_input = input("Item Index: ")
        read(index_input)
        print(checklist[int(index_input)])

    elif function_code == "P":
        print(list_all_items())

    elif function_code == "Q":
        return False

    elif function_code == "M":
        index = input("Index for complete item: ")
        mark_complete(int(index))

    elif function_code == "I":
        index = input("Index for incomplete item: ")
        mark_incomplete(int(index))

    else:
        print("Wrong Option")

def test():
    # insert testing below
    print('------ Testing Loop ------')

test()

running = True
while running:
    selection = input(
        "Press C to add to list, R to Read from list, P to display list, M to mark completed and I to mark incompleted: ")
    select(selection)