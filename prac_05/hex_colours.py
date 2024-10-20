COLOR_CODES = {"aliceblue": "#f0f8ff", "antiquewhite": "#faebd7", "aquamarine": "#7fffd4", "azure": "#f0ffff",
               "beige": "#f5f5dc", "bisque": "#ffe4c4", "black": "#000000", "blanchedalmond": "#ffebcd",
               "blueviolet": "#8a2be2", "brown": "#a52a2a"}

print("Color Names and Codes:")
for name, code in COLOR_CODES.items():
    print(f"{name} is {code}")

color_name = input("Enter a color name: ").strip().lower()

while color_name != "":
    try:
        print(f"The hexadecimal code for {color_name} is {COLOR_CODES[color_name]}")
    except KeyError:
        print("Invalid color name")

    color_name = input("Enter a color name: ").strip().lower()