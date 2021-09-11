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

    @staticmethod
    def create_object_from_raw_data(json_object):
        return Quote(json_object['quote'],
                  json_object['title'],
                  json_object['author'],
                  json_object['link'],
                  json_object['words'],
                  json_object['chapter'],
                  json_object['nsfw'])
