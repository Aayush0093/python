isOldEnough = False
isLicense = False
age = int(input("How old are you? "))
license = input("Do you have a driver's license? (yes/no) ")

license1 = license.lower()
if(license1 == "yes"):
    isLicense = True
else:
    isLicense = False

if(age>=18):
    isOldEnough = True
else:
    isOldEnough = False

if(isOldEnough and isLicense):
    print("You can drive.")
elif(isOldEnough and not isLicense):
    print("You don't have a license.")
elif(not isOldEnough and isLicense):
    print("You are not old enough.")
else:
    print("You can't drive as both conditions are not met.")