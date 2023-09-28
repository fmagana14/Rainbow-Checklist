checklist= list()

def list_all_items():
    index = 0 
    for list_item in checklist:
        print(list_item)
        index += 1 
   
    #create
def create(item):
    checklist.append(item)
    

    #read
def read (index) :
    return checklist[index]

    #update

def update (index, item):
    checklist [index] = item

    #distroy

def destroy(index):
    checklist.pop(index)

def list_all_items():
    index = 0
    for list_item in checklist:
        print(list_item)
        index += 1

def marked_complete(index):
    checklist[index] += "√"

def select(function_code):
    if function_code == "C":
        item_index = int(input("Index Number?"))
        create(input("Enter input to add:"))

    elif function_code ==  "R":
        item_index =  int(input("Index Number?"))
        if 0 <= item_index < len(checklist):
            print(read(item_index))
        else:
            print("Invalid index")
    
    elif function_code == "P":
        list_all_items()

    else:
        print("Unknown Option")

def user_input(prompt):
    user_input = input(prompt)
    return user_input

def test():
    
     create ("Purple Sox")
     create ("Red cloak")
     create ("Purple Soxs")

     print(read(0))
     print(read(1))

     update(0, "Purple Sox")

     destroy (1)

     print(read(0))

select ("C")

list_all_items()

select("R")

list_all_items()

user_value = user_input("0", "1" )
print(user_value)
test()
