from json import JSONEncoder

def replace(field):
    return field.replace("\u2019", "'").replace("\u2018", "'")


class Quote(dict):

    def __init__(self, quote, title, author, link, words, chapter):
        self.quote = quote
        self.title = title
        self.author = author
        self.link = link
        self.words = words
        self.chapter = chapter
        self.replace_all()
        dict.__init__(self,
                      quote=quote,
                      title=title,
                      author=author,
                      link=link,
                      words=words,
                      chapter=chapter)

    def replace_all(self):
        self.quote = replace(self.quote)
        self.title = replace(self.title)
        self.author = replace(self.author)
