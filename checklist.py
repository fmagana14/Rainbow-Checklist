checklist = list()

def list_all_items():
    index = 0
    for list_item in checklist:
        print(list_item)
        index += 1

def create(item):
    checklist.append(item)

def read(index):
    return checklist[index]

def update(index, item):
    checklist[index] = item

def destroy(index):
    checklist.pop(index)

def marked_complete(index):
    checklist[index] += " √"

def select(function_code):
    if function_code.upper() == "C":
        item = input("Enter item to add: ")
        create(item)

    elif function_code.upper() == "R":
        index = int(input("Enter index to read: "))
        if 0 <= index < len(checklist):
            print(read(index))
        else:
            print("Invalid index")

    elif function_code.upper() == "U":
        index = int(input("Enter index to update: "))
        item = input("Enter updated item: ")
        update(index, item)
         
    elif function_code.upper() == "D":
        index = int(input("Enter index to destroy: "))
        destroy(index)

    elif function_code.upper() == "L":
        list_all_items()

    elif function_code.upper() == "M":
        index = int(input("Enter index to mark completed: "))
        marked_complete(index)

    elif function_code.upper() == "Q":
        return False

    else:
        print("Unknown Option")
    
    return True

def user_input(prompt):
    user_input = input(prompt)
    return user_input

def test():
    create("Purple Sox")
    create("Red cloak")
    create("Purple Soxs")

    print(read(0))
    print(read(1))

    update(0, "Purple Soxs")

    destroy(1)

    print(read(0))

# Run Tests
test()

running = True
while running:
    selection = input("Press C to add to list, R to Read from list, U to Update, D to Destroy, L to List, M to Mark Completed, and Q to quit: ")
    running = select(selection)
