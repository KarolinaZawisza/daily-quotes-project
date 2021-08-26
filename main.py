import datetime as dt
import json
import random
import smtplib

# TODO: Find a way to store these safely
MY_EMAIL = 'dailydnfquotes@gmail.com'
PASSWORD = 'Dmaj7D6x2Aadd9Ax2'

now = dt.datetime.now()
print(f'Starting time: {now.hour}:{now.minute}:{now.second}')

# TODO: Add a proper Try Catch, checking if list isn't empty
with open('dnf_quotes.json', 'r', encoding="utf8") as file:
    data = json.load(file)
    quote_list = [x['quote'] for x in data]
    title_list = [x['title'] for x in data]
    author_list = [x['author'] for x in data]
    words_list = [x['words'] for x in data]
    chapter_list = [x['chapter'] for x in data]
    link_list = [x['link'] for x in data]

emails = open('emails.txt').read().splitlines()

dnf_quotes = random.choice(quote_list)
index = quote_list.index(dnf_quotes)
print(f'Index: {index}')

# Removing \u2019 and \u2018 character and replacing it with a '
# TODO: Make a formatting system for all weird characters instead of doing it manually
dnf_quotes_formatted = dnf_quotes.replace("\u2019", "'").replace("\u2018", "'")
title_formatted = title_list[index].replace("\u2019", "'").replace("\u2018", "'")
author_formatted = author_list[index].replace("\u2019", "'").replace("\u2018", "'")

# TODO: Make a feature which will check for a ratings
# TODO: Different ratings will get quotes from different lists
for mail in emails:
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=mail,
            msg=f'SUBJECT:Daily DNF Quotes\n\n'
                f'{dnf_quotes_formatted}\n\n\n'
                f'Title: "{title_formatted}"\n'
                f'Author: {author_formatted}\n'
                f'Words: {words_list[index]}\n'
                f'Chapters: {chapter_list[index]}\n'
                f'Link: {link_list[index]}'
        )
    print(f'Send email to {mail} - {now.hour}:{now.minute}:{now.second}')

# Removing used quote from file
quote_list.remove(dnf_quotes)
title_list.pop(index)
author_list.pop(index)
words_list.pop(index)
chapter_list.pop(index)
link_list.pop(index)

with open('dnf_quotes.json', 'r', encoding='utf8') as file:
    data_test = json.load(file)
    print(f'First: {len(data_test)}')

for element in data_test:
    if element == data_test[index]:
        data_test.pop(data_test.index(element))

print(f'Second: {len(data_test)}')

with open('dnf_quotes.json', 'w', encoding='utf8') as file:
    json.dump(data_test, file, indent=4)

if len(quote_list) > 0:
    print(f'Successfully deleted one record! Quotes left: {len(quote_list)}')
else:
    print(f'Quotes list: {len(quote_list)}\n'
          'NONE QUOTES LEFT!')
