import re

file_name: str = str(input())


def is_valid_email(email_address: str) -> bool:
    regex: re.Pattern = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
    return bool(re.fullmatch(regex, email_address))


def get_domain(full_email_address: str) -> str:
    return full_email_address[full_email_address.find('@') + 1:]


existed_domains: dict[str, int] = dict()

with open(file_name, 'r') as file:
    for email in file.readlines():
        email = email.replace('\n', '')
        if is_valid_email(email):
            domain: str = get_domain(email)
            try:
                existed_domains.update({domain: existed_domains[domain] + 1})
            except KeyError:
                existed_domains.update({domain: 1})
        else:
            try:
                existed_domains.update({'INVALID': existed_domains['INVALID'] + 1})
            except KeyError:
                existed_domains.update({'INVALID': 1})

for domain in sorted([(key, value) for key, value in existed_domains.items()], key=lambda item: item[1], reverse=True):
    print(domain[0], domain[1])
