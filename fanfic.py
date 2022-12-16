class Fanfiction:

    # TO DO: add in fandom
    def __init__(self, title, author, rating, word_count, fandoms, ships, tags):
        self.title = title
        self.author = author
        self.rating = rating
        self.word_count = word_count
        self.fandoms = fandoms
        self.ships = ships
        self.tags = tags

    def stringify(self):
        return f"{self.title} : {self.fandoms} : {self.tags}"
    def get_tags_string(self):
        tags = ""
        for tag in self.tags[:-1]:
            tags += f"{tag}, "
        tags += f"{self.tags[-1]}"
        return tags
    def __str__(self):
        return f"{self.title} by {self.author}"

    def __lt__(self, other):
        return self.title < other.title