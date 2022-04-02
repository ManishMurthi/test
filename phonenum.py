import phonenumbers
from phonenumbers import carrier,geocoder,timezone

number="+447459897989"
num=phonenumbers.parse(number)
tz=timezone.time_zones_for_number(num)
carr=carrier.name_for_number(num,"en")
geo=geocoder.description_for_number(num,"en")

print(num)
print(tz)
print(carr)
print(geo)
