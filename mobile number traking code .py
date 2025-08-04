import phonenumbers
from phonenumbers import geocoder

number = phonenumbers.parse("+497204197822")
location = geocoder.description_for_number(number, "en")
print(location)  # Output: "California"

number = phonenumbers.parse("+869876543210", None)
location = geocoder.description_for_number(number, "en")
print("Location:", location)

phonenumber1= phonenumbers.parse("+9172294536272")
phonenumber2= phonenumbers.parse("+9172394536272")


print("\nphone numbers location\n")

print(geocoder.description_for_number(phonenumber1,"en"));
print(geocoder.description_for_number(phonenumber2,"en"));