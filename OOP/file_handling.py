#### file handling

import os
from pathlib import Path

try:

  with open('my_first_file.txt', 'x') as file:
    file.write("Brand new file!\n")
    file.write("Learning Python file handling.\n")
  print("File 'my_first_file.txt' has been created!")
except FileExistsError:
  print("File already exist! Won't overwrite.")


#checking if file exist
second_file = 'my_safe_file.txt'

if not os.path.exists(second_file):
  with open(second_file, 'w') as file:
    file.write("Safe new file creation!\n")
  print(f"New File [{second_file}] Created!")
else:
  print("File already exists, not creating.")

print("\n...............................\n")
file_path = Path('my_modern_file.txt')

if not file_path.exists():
    file_path.write_text("Created with pathlib!\n")
    print(f"New file [{file_path}] created!")
else:
    print("File already exist, not creating. ")