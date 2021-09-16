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

test()