import datetime as dt
import json
import random
import smtplib
from quote import Quote
from emails import Email, get_rating
from keys import PASSWORD, MAIN_EMAIL

rating = 'SFW'

now = dt.datetime.now()
print(f'Starting time: {now.hour}:{now.minute}:{now.second}')

# TODO: Move it all to the DB
# TODO: Add a proper Try Catch, checking if list isn't empty
with open('dnf_quotes.json', 'r', encoding="utf8") as file:
    data_from_json = json.load(file)
    quotes_list = []
    for json_object in data_from_json:
        quote = Quote(json_object['quote'],
                      json_object['title'],
                      json_object['author'],
                      json_object['link'],
                      json_object['words'],
                      json_object['chapter'],
                      json_object['nsfw'])
        quotes_list.append(quote)

with open('emails.json', 'r') as file:
    emails_from_json = json.load(file)
    emails_list = []
    for json_object in emails_from_json:
        json_email = Email(json_object['email'],
                           json_object['name'],
                           json_object['nsfw'])
        emails_list.append(json_email)

chosen_quote = random.choice(quotes_list)

# TODO: Add checking for quote rating and default
for mail in range(0, len(emails_list)):
    receiver = emails_list[mail]
    # if receiver.nsfw == chosen_quote.nsfw:
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=MAIN_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MAIN_EMAIL,
            to_addrs=receiver.email,
            msg=f'SUBJECT:Daily {get_rating(receiver.nsfw)} DNF Quotes\n\n'
                f'{chosen_quote.quote}\n\n\n'
                f'Title: "{chosen_quote.title}"\n'
                f'Author: {chosen_quote.author}\n'
                f'Words: {chosen_quote.words}\n'
                f'Chapters: {chosen_quote.chapter}\n'
                f'Link: {chosen_quote.link}\n\n\n'
                f'Hello {receiver.name}!\n'
                f'Thank you for subscribing to Daily DNF Quotes with rating {get_rating(receiver.nsfw)}.\n'
                f'If you would like to manage your subscription or rating settings,'
                f' you can always contact us on Twitter!\n\n'
                f'We hope that you liked your today quote and see you tomorrow! :)'.encode('UTF-8')
        )
    print(f'Send email to {receiver.name} ({receiver.email}) - {now.hour}:{now.minute}:{now.second}')

quotes_list.remove(chosen_quote)

with open('dnf_quotes.json', 'w', encoding='utf8') as file:
    json.dump(quotes_list, file, indent=4)

if len(quotes_list) > 0:
    print(f'Successfully deleted one record! Quotes left: {len(quotes_list)}')
else:
    print(f'Quotes list: {len(quotes_list)}\n'
          'NONE QUOTES LEFT!')
