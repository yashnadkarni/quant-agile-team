#
#************************************************************************************
# Quant Systems Agile Group Project
# Team Tech Ninjas - BMI Calculator
#************************************************************************************
#
print("\nBMI Calculator\n")

def get_info(info):
    #******************************************
    # Function will loop till user correctly gives input
    # Returns age, gender, weight and height
    #******************************************
    while True:
        try:
            if info == "age":
                age = round(float(input("Enter age: ")))
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
            print("\nError! Please enter a correct value\n")
    
## Get user age, gender, weight & height
age = get_info("age")
gender = get_info("gender")
weight = get_info("weight")
height = get_info("height")

if height == 0:
    print("\nYour BMI rating is -3\n")
else:
    bmi = (weight / (height * height)) * 10000                  ## BMI Formula in kgs and cm
    if bmi <= 42:
        scaled_bmi = 3 - (6 / 21) * abs(bmi - 21)               ## Formula to scale and adjust according to -3 to 3 scale
        print("\nYour BMI rating is: ",round(scaled_bmi), "\n") ## Will only output [-3, -2, -1, 0, 1, 2, 3] rating
    else:
        print("\nYour BMI rating is -3\n")

#************************************************************************************
# END
#************************************************************************************
