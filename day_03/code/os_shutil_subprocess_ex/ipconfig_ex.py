import subprocess
import re

content = subprocess.check_output("ipconfig -all", shell=True)

content = content.decode()

pattern = r"(\w{2}-){5}\w{2}"

for m in re.finditer(pattern, content):
    if(m):
        print(m.span(), ' ----> ', m.group())


print('--------------------- Another Method')

content2 = content.split('\r\n')
for line in content2:
    if("Physical" in line):
        m = re.search(pattern, line)
        print(m.group())
