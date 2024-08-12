#
# Code to calculate BMI and give user a rating
#
print("BMI Calculator")

def get_info(info):
    #******************************************
    # GetInfo from user
    # Function will loop till user correctly gives input.
    #******************************************
    while True:
        try:
            if info == "age":
                age = int(input("Enter age: "))
                if 0 <= age <= 99:
                    return age
                else:
                    raise Exception()
            elif info == "gender":
                gender = input("Enter gender(1:Male, 2:Female): ")
                if gender in ["1", "2"]:
                    return gender
                else:
                    raise Exception()
            elif info == "weight":
                weight = round(float(input("Enter weight in kgs: ")))
                if 0 <= weight <= 250:
                    return weight
                else:
                    raise Exception()
            elif info == "height":
                height = round(float(input("Enter height in cms: ")))
                if 0 <= height <= 244:
                    return height
                else:
                    raise Exception()
            else:
                return int(input(f"Enter {info}: "))
        except:
            print("\nError! Please enter a correct number\n")
    
# Get age, gender, weight & height
age = get_info("age")
gender = get_info("gender")
weight = get_info("weight")
height = get_info("height")

if height == 0:
    print("\nYour rating is -3\n")
else:
    # Calculate BMI and rating
    bmi = (weight / (height * height)) * 10000
    print("Weight: ",weight, " Height: ",height)
    if bmi <= 42:
        if bmi <= 21:
            scaled_bmi = ((6 * bmi) / 21) - 3
        else:
            scaled_bmi = ((6 * bmi) / 21) - 9
        print("\n\nYour rating is: ", round(scaled_bmi),"  Scaled BMI: ",scaled_bmi,"\n\n")
    else:
        print("\nError! BMI out of range\n")
