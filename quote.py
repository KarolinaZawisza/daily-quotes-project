class Quote(dict):

    def __init__(self, quote, title, author, link, words, chapter, nsfw):
        self.quote = quote
        self.title = title
        self.author = author
        self.link = link
        self.words = words
        self.chapter = chapter
        self.nsfw = nsfw
        dict.__init__(self,
                      quote=quote,
                      title=title,
                      author=author,
                      link=link,
                      words=words,
                      chapter=chapter,
                      nsfw=nsfw)
