import json

x = {
  "name": "Ashura Sheikh",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Loyalty","Pride"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}



y = {
  "name": "Ashura Sahil",
  "age": 25,
  "married": False,
  "divorced": False,
  "children": None,
  "pets": None,
  "cars": [
    {"model": "Lexus 230", "mpg": 27.5},
    {"model": "Lancer Edge", "mpg": 24.1}
  ]
}

z = {
  "name": "Ashura Mustafa",
  "age": 35,
  "married": True,
  "divorced": False,
  "children": None,
  "pets": None,
  "cars": [
    {"model": "Ferrari 230", "mpg": 27.5},
    {"model": "Porche Edge", "mpg": 24.1}
  ]
}

print(json.dumps(x, indent=2))
print(json.dumps(y, indent=2))
print(json.dumps(z, indent=2))
