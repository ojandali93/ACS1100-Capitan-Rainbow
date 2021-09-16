# print("Hello World")

# checklist = list()
# checklist 

# def my_fun_function(say_this):
#     print(say_this)

# my_fun_function('Hello World')

checklist = list()
checklist.append('Blue')
print(checklist)
checklist.append('Orange')
print(checklist)

def create(item):
    checklist.append(item)

def read(index):
    print(checklist[index])
    return checklist[index]

def update(index, item):
    checklist[index] = item

def destroy(index):
    checklist.pop(index)

def list_all_items():
    index = 0
    for item in checklist:
        print(str(index) + ' - ' + item)
        index += 1

def test():
    create("navy")
    create('blue')
    create('cyan')
    create('green')
    create('yellow')
    create('red')
    create('orange')
    create('white')
    print(checklist)
    read(9)
    print(checklist)
    destroy(9)
    print(checklist)
    update(8, 'red')
    update(7, 'orange')
    print(checklist)
    print('-------testing list items-----------')
    create("purple sox")
    create("red cloak")
    print(read(0))
    print(read(1))
    update(0, "purple socks")
    destroy(1)
    print(read(0))
    list_all_items()

test()