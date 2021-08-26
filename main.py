import datetime as dt
import json
import random
import smtplib
from quote import Quote
from keys import PASSWORD, MAIN_EMAIL

now = dt.datetime.now()
print(f'Starting time: {now.hour}:{now.minute}:{now.second}')

# TODO: Add a proper Try Catch, checking if list isn't empty
with open('dnf_quotes.json', 'r', encoding="utf8") as file:
    data_from_json = json.load(file)
    quotes = []
    for json_object in data_from_json:
        quote = Quote(json_object['quote'],
                      json_object['title'],
                      json_object['author'],
                      json_object['link'],
                      json_object['words'],
                      json_object['chapter'])
        quotes.append(quote)

emails = open('emails.txt').read().splitlines()

chosen_quote = random.choice(quotes)

# TODO: Make a formatting system for all weird characters instead of doing it manually

# TODO: Make a feature which will check for a ratings
# TODO: Different ratings will get quotes from different lists
for mail in emails:
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=MAIN_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MAIN_EMAIL,
            to_addrs=mail,
            msg=f'SUBJECT:Daily DNF Quotes\n\n'
                f'{chosen_quote.quote}\n\n\n'
                f'Title: "{chosen_quote.title}"\n'
                f'Author: {chosen_quote.author}\n'
                f'Words: {chosen_quote.words}\n'
                f'Chapters: {chosen_quote.chapter}\n'
                f'Link: {chosen_quote.link}'
        )
    print(f'Send email to {mail} - {now.hour}:{now.minute}:{now.second}')

# TODO: DB
quotes.remove(chosen_quote)

with open('dnf_quotes.json', 'w', encoding='utf8') as file:
    json.dump(quotes, file, indent=4)

if len(quotes) > 0:
    print(f'Successfully deleted one record! Quotes left: {len(quotes)}')
else:
    print(f'Quotes list: {len(quotes)}\n'
          'NONE QUOTES LEFT!')
