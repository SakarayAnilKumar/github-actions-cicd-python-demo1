from datetime import datetime

print("Python artifact demo")

with open("results.txt","W") as file:
  file.write("Hello from github\n")
  file.write("This file is created in git\n")
  file.write(f"Generated time is {datetime.now()}\n")
  
print("results.txt file is created successfully")
