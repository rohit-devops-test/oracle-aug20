import re
EOF = ''
# Read the file as a text

f = open(r"C:\Users\Purushotham\Desktop\oracle_july\day_03\regex_ex\resume.txt", "r")
content = f.read()
f.close()
# Patterns

jobid = '#(\d){6}'
email = "\w+\.\w+@\w+\.(com|org|in)"
phone = "(\d{3}-){2}(\d{4})"
linkedin = "(linkedin.com)/\w+/((\w+-){2}(\w+)|(\w+))"
name = "Sincerely,\n+(?P<Name>\w+\s\w+)"

# Apply the patterns and store what ever is extracted



m = re.search(jobid, content)
if m:
    print('JOBID     : ', m.group())

m = re.search(email, content)
if m:
    print('EMAIL     : ', m.group())

m = re.search(phone, content)
if m:
    print('PHONE     : ', m.group())

m = re.search(linkedin, content)
if m:
    print('LINKEDIN  : ', m.group())

m = re.search(name, content)
if m:
    print('NAME      : ', m.groupdict()['Name'])
