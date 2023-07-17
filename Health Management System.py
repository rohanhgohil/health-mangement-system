# Health Management System

# To get the date and time
def getdate():
    import datetime
    return datetime.datetime.now()

# Dictionary for the people
dic = {
    1:"rahul",
    2:"raj",
    3:"rohan"
}

# Title
print("-----Health Management System-----")
user = int(input("Press 1 to Add data\nPress 2 for Retrieve data\n"))
user1 = int(input("Press 1 for Exercise\nPress 2 for Diet\n"))
user2 = int(input("Press 1 for Rahul\nPress 2 for Raj\nPress 3 for Rohan\n"))

# Main function
def system(a,b,c):
    if a==1:
        return add_data(a,b,c)

    elif a==2:
        return retrieve_data(a,b,c)
    else:
        print("Invalid Input")

# To add Data
def add_data(a,b,c):
    if b==1:
        return exercise(a,b,c)
    elif b==2:
        return diet(a,b,c)
    else:
        print("Invlaid Input")

# To retrieve Data
def retrieve_data(a,b,c):
    if b==1:
        return exercise(a,b,c)
    elif b==2:
        return diet(a,b,c)
    else:
        print("Invalid Input")

# For exercise
def exercise(a,b,c):
    if a==1:     # Add Data
        with open(f"{dic[c]} exercise.txt", "a") as f:
            f.write(f"[{getdate()}] : {input('Enter your exercise: ')}\n")
        print("Added Successfully")

    elif a==2:   # Retrieve Data
        with open(f"{dic[c]} exercise.txt") as f:
            print(f.read())

# For diet
def diet(a,b,c):
    if a==1:     # Add Data
        with open(f"{dic[c]} diet.txt", "a") as f:
            f.write(f"\n[{getdate()}] : {input('Enter your food: ')}\n")
        print("Added Successfully")

    elif a==2:   # Retrieve Data
        with open(f"{dic[c]} diet.txt") as f:
            print(f.read())


# Running the function
system(user,user1,user2)
