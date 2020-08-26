# Objective

# Extract the following from the resume:
# Job ID   -> #667885
# Name
# Email
# Phone
# LinkedIn link

# -------------------------------------------------------------

import re
EOF = ''
# Read the file as a text

f = open(r"C:\Users\Purushotham\Desktop\oracle_aug\day_03\regex_ex\resume.txt", "r")

# Patterns

jobid = r'#\d{6}'
email = r"(\w+\.)?(\w+)@\w+\.(com|org|in)"
phone = r"(\d{3}-){2}\d{4}"
linkedin = r"(linkedin.com)/\w+/(\w+[-])*(\w+)"
name = r"(Sincerely|Thankfully)[,]?[\n]*(?P<name>(\w+\s?)*)"


# Apply the patterns and store what ever is extracted
line = f.read()

if __name__ == "__main__":
    

    m = re.search(jobid, line)
    if m:
        print('JOBID     : ', m.group())

    m = re.search(email, line)
    if m:
        print('EMAIL     : ', m.group())

    m = re.search(phone, line)
    if m:
        print('PHONE     : ', m.group())

    m = re.search(linkedin, line)
    if m:
        print('LINKEDIN  : ', m.group())

    m = re.search(name, line)
    if m:
        print('NAME  : ', m.groupdict()['name'])
# Print the results



f.close()
