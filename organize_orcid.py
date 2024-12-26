import re

checks = ["Hayrapetyan2024","Hayrapetyan2023","Tumasyan2024","Tumasyan2023","Tumasyan2022", "Sirunyan2022", "Tumasyan2021", "Sirunyan2021",
          "Abbas2020","Abbas2024", "Abbas2021", "Sirunyan2020", "Sirunyan2019",
          "Fiorina2020", "Fiorina2019", "Tumasyan2023","Abbas2023","Hayrapetyan2023"]
print("words to check:", len(checks))

# Combine the checks into a single regular expression
regex_pattern = '|'.join(checks)

# Function to replace matched strings with a unique number appended
def replace_with_unique_number(match):
    replace_with_unique_number.counter += 1
    return f"{match.group()}{replace_with_unique_number.counter}"

replace_with_unique_number.counter = 0

# Read, process, and write to the same file using context managers
with open("bib_test.bib", "r") as file:
    file_string = file.read()
    processed_string = re.sub(regex_pattern, replace_with_unique_number, file_string)

with open("bib_test.bib", "w") as file:
    file.write(processed_string)

# Process for long author names replacement
to_write = []
with open('bib_test.bib', 'r') as file:
    for line in file:
        if len(line) > 10000:
            to_write.append("author={The CMS Collaboration},\n")
        elif 1000 < len(line) < 10000 and ("Accettura, Carlotta" not in line and "Black, K.M. and Jindariani, S." not in line):
            to_write.append("author={The CMS GEM Group},\n")
        elif 1000 < len(line):
            to_write.append("author={The Muon Collider Collaboration},\n")
        else:
            to_write.append(line)

with open("bib.bib", "w") as file:
    file.writelines(to_write)
