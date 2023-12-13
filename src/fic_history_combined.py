from fanfiction_history import *
from fic_history_wc_base import *

def wcOp(num):
    return num/1000
def nfOp(num):
    return num * num

class FicHistoryCombo:
    def __init__(self, csv_location):
        WordCount = FicHistoryWC(csv_location)
        NumFics = FicHistoryNumFic(csv_location)

        self.total_fics_read = WordCount.total_fics()
        self.words_read = WordCount.total_words_read()

        fic_list = []

        # ratings
        self.ratings = {"General Audiences": 0, "Teen And Up Audiences": 0, "Mature": 0, "Explicit": 0, "Not Rated": 0}

        for rating in WordCount.ratings:
            self.ratings[rating] += wcOp(WordCount.ratings[rating])
        for rating in NumFics.ratings:
            self.ratings[rating] += nfOp(NumFics.ratings[rating])

        # fandoms
        self.fandom_list = {}
        for fandom in WordCount.fandom_list:
            self.fandom_list[fandom] = wcOp(WordCount.fandom_list[fandom])
        for fandom in NumFics.fandom_list:
            if fandom in self.fandom_list:
                self.fandom_list[fandom] += nfOp(NumFics.fandom_list[fandom])
            else:
                self.fandom_list[fandom] = nfOp(NumFics.fandom_list[fandom])
        self.fandom_list = order_dict(self.fandom_list)

        # ships
        self.ship_list = {}
        for ship in WordCount.ship_list:
            self.ship_list[ship] = wcOp(WordCount.ship_list[ship])
        for ship in NumFics.ship_list:
            if ship in self.ship_list:
                self.ship_list[ship] += nfOp(NumFics.ship_list[ship])
            else:
                self.ship_list[ship] = nfOp(NumFics.ship_list[ship])
        self.ship_list = order_dict(self.ship_list)

        # tags
        self.tag_list = {}

        # puts all tags in a list
        for tag in WordCount.tag_list:
            self.tag_list[tag] = wcOp(WordCount.tag_list[tag])
        for tag in NumFics.tag_list:
            if tag in self.tag_list:
                self.tag_list[tag] += nfOp(NumFics.tag_list[tag])
            else:
                self.tag_list[tag] = nfOp(NumFics.tag_list[tag])
        self.tag_list = order_dict(self.tag_list)



    # HELPFUL METHODS
    def __len__(self):
        return len(self.fic_list)

    def __str__(self):
        return f"Contains {len(self.fic_list)} fics"

    # RETRIEVAL METHODS
    def get_ratings(self):
        return self.ratings


    # PRINTING METHODS
    def print_fics(self):
        count = 1
        for fic in self.fic_list:
            print(f"{count}: {fic.stringify()}:     {fic.get_tags_string()}")
            count += 1

    def print_top_tags(self, i=3):
        for index, (tag, tag_count) in enumerate(self.tag_list.items()):
            if i <= index:
                break
            print(f"{index+1}. {tag} ({tag_count})")

    def print_top_fandoms(self, i=3):
        j  = 1
        for index, (fandom, fandom_count) in enumerate(self.fandom_list.items()):
            if i <= index:
                break

            print(f"{index+1}. {fandom} ({fandom_count})")


    def print_top_ships(self, i=3):
        for index, (ship, ship_count) in enumerate(self.ship_list.items()):
            if i <= index:
                break
            print(f"{index+1}. {ship} ({ship_count})")


    # STATISTICAL METHODS
    def total_fics(self):
        return self.total_fics_read

    def top_rating(self):
        top_rating = ""
        top_rating_count = 0
        for rating in self.ratings:
            if self.ratings[rating] > top_rating_count:
                top_rating = rating
                top_rating_count = self.ratings[rating]

        return top_rating, top_rating_count

    def total_words_read(self):
        return self.words_read

    def top_tags(self, i=5):
        top_tags = {}

        for index, (tag, tag_count) in enumerate(self.tag_list.items()):
            if i <= index:
                return top_tags
            top_tags[tag] = tag_count

        return top_tags

    def total_fandoms(self):
        return len(self.fandom_list)

    def total_ships(self):
        return len(self.ship_list)

    def top_fandoms(self, i=5):
        top_fandoms = {}

        for index, (fandom, fandom_count) in enumerate(self.fandom_list.items()):
            if i <= index:
                return top_fandoms
            top_fandoms[fandom] = fandom_count

        return top_fandoms

    def top_ships(self, i=5):
        top_ships = {}

        for index, (ship, ship_count) in enumerate(self.ship_list.items()):
            if i <= index:
                return top_ships
            top_ships[ship] = ship_count

        return top_ships


