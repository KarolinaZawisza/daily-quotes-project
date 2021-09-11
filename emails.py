def get_rating(nsfw):
    if nsfw:
        return 'NSFW'
    else:
        return 'SFW'

class Email(dict):

    def __init__(self, email, name, nsfw):
        self.email = email
        self.name = name
        self.nsfw = nsfw
        dict.__init__(self,
                      email=email,
                      name=name,
                      nsfw=nsfw)

    @staticmethod
    def create_object_from_raw_data(json_object):
        return Email(
            json_object['email'],
            json_object['name'],
            json_object['nsfw'])
