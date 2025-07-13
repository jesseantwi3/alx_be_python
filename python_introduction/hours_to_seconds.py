hours = 2

seconds = hours * 60 * 60

# Handle plural or singular unit
unit = "hour" if hours == 1 else "hours"

print(f"{hours} {unit} is {seconds} seconds.")

