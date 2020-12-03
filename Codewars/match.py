import re

def domain_url(url):
    regex = re.compile("((?<=https://)|(?<=www\\.)|(?<=http://))\\w{0,}(?=\\.)")
    return regex.findall(url)

print(domain_url("https://youtube.com"))