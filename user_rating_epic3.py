import random

print("\n******************************************************")
print("\t\tUser Rating Calculator")
print("******************************************************\n")

def get_info(info):
    while True:
        try:
            if info == "age":
                age_input = input("Enter age: ")
                if not age_input.isdigit():
                    raise ValueError("Invalid input. Age must be a positive integer.")
                age = int(age_input)
                if 0 <= age <= 99:
                    return age
                else:
                    raise ValueError("Invalid age range. Please enter a valid age between 0 and 99.")
            elif info == "gender":
                gender = input("Enter gender (1: Male, 2: Female): ")
                if gender in ["1", "2"]:
                    return gender
                else:
                    raise ValueError("Invalid gender selection. Please enter 1 for Male or 2 for Female.")
            elif info == "weight":
                weight_input = input("Enter weight in kgs: ")
                if not weight_input.replace('.', '', 1).isdigit():
                    raise ValueError("Invalid input. Weight must be a numeric value.")
                weight = round(float(weight_input), 2)
                if 0 <= weight <= 250:
                    return weight
                else:
                    raise ValueError("Invalid weight range. Please enter a valid weight between 0 and 250 kgs.")
            elif info == "height":
                height_input = input("Enter height in cms: ")
                if not height_input.replace('.', '', 1).isdigit():
                    raise ValueError("Invalid input. Height must be a numeric value.")
                height = round(float(height_input))
                if 0 <= height <= 244:
                    return height
                else:
                    raise ValueError("Invalid height range. Please enter a valid height between 0 and 244 cms.")
            elif info == "alcohol":
                alcohol = input("Do you consume alcohol? (Y/N): ").upper()
                if alcohol == "Y":
                    while True:
                        drinks_input = input("How many drinks do you consume? ")
                        if not drinks_input.isdigit() or int(drinks_input) <= 0:
                            print("Invalid input. Number of drinks must be a positive integer.")
                        else:
                            return int(drinks_input)
                elif alcohol == "N":
                    return 0
                else:
                    raise ValueError("Invalid selection. Please enter 'Y' or 'N'.")
            elif info == "tobacco":
                tobacco = input("Do you consume tobacco? (Y/N): ").upper()
                if tobacco == "Y":
                    while True:
                        packs_input = input("How many packs do you consume? ")
                        if not packs_input.isdigit() or int(packs_input) <= 0:
                            print("Invalid input. Number of packs must be a positive integer.")
                        else:
                            return int(packs_input)
                elif tobacco == "N":
                    return 0
                else:
                    raise ValueError("Invalid selection. Please enter 'Y' or 'N'.")
            elif info == "users":
                users = input("Enter how many users do you want to add? (Limit: 9): ")
                if not users.isdigit():
                    raise ValueError("Invalid input. Please enter an integer between 0 and 9")
                users = int(users)
                if 0 <= users <= 9:
                    return users
                else:
                    raise ValueError("Invalid range. Please enter a valid number between 0 and 9.")
            else:
                return int(input(f"Enter {info}: "))
        except ValueError as e:
            print(f"\nError! {e}\n")
        except Exception as e:
            print(f"\nUnexpected error: {e}\n")

def calc_bmi_rating(height, weight):
    if height == 0:
        return -3
    else:
        bmi = round((weight / (height * height)) * 10000, 2)  ## BMI Formula in kgs and cm
        if bmi <= 42:
            return round(3 - (6 / 21) * abs(bmi - 21))  ## Scale to [-3,-2, -1,0 1, 2, 3]
        else:
            return -3


def calculate_rating(value):
    if value == 0:
        return 3
    elif value in [1, 2]:
        return 2
    elif value in [3, 4]:
        return 1
    elif value in [5, 6]:
        return 0
    elif value in [7, 8]:
        return -1
    elif value in [9, 10]:
        return -2
    else:
        return -3


def get_user_rating():
    ## Get user age, gender, weight, height, alcohol and tobacco consumption details
    age = get_info("age")
    gender = get_info("gender")
    weight = get_info("weight")
    print("User weight is ", weight)
    height = get_info("height")
    print("User height is ", height)
    alcohol = get_info("alcohol")
    tobacco = get_info("tobacco")

    # Calculate individual ratings
    bmi_rating = calc_bmi_rating(height, weight)
    alcohol_rating = calculate_rating(alcohol)
    tobacco_rating = calculate_rating(tobacco)

    # Integrate ratings into a final user rating
    user_rating = round((bmi_rating + alcohol_rating + tobacco_rating) / 3)

    # Ensure the final rating is within the expected range
    if user_rating < -3:
        user_rating = -3
    elif user_rating > 3:
        user_rating = 3
    
    return user_rating

# Get details for 1 user, then get details for more
user_list = [get_user_rating()]
additional_users = get_info("users")
for i in range(additional_users):
    print(f"\n Enter details for User {i + 1}")
    user_list.append(get_user_rating())

# Print all user ratings
for i in range(len(user_list)):
    print(f"\n User{i+1} rating is {user_list[i]}")
