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

def mark_completed(index):
    item = "X " + checklist[index]
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

    else:
        print("Wrong Option")


def test():
    # create("navy")
    # create('blue')
    # create('cyan')
    # create('green')
    # create('yellow')
    # create('red')
    # create('orange')
    # create('white')
    # print(checklist)
    # read(9)
    # print(checklist)
    # destroy(9)
    # print(checklist)
    # update(8, 'red')
    # update(7, 'orange')
    # print(checklist)
    # print('-------testing list items-----------')
    # create("purple sox")
    # create("red cloak")
    # create("green sox")
    # create("yellow sox")
    # print(read(0))
    # print(read(1))
    # update(0, "purple socks")
    # destroy(1)
    # print(read(0))
    # list_all_items()
    # mark_completed(1)
    # list_all_items()
    print('-------testing user items-----------')
    # Call your new function with the appropriate value
    select("C")
    # View the results
    list_all_items()
    # Call function with new value
    select("R")
    # View results
    list_all_items()
    # Continue until all code is run

test()