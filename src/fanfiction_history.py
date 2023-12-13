import csv
from fanfic import *
from col_nums import *

def order_dict(list):
    new_dict = {}

    while len(list) > 1:
        greatest = ""
        greatest_count = 0
        for item in list:
            if list[item] >= greatest_count:
                greatest = item
                greatest_count = list[item]

        new_dict[greatest] = greatest_count
        list.pop(greatest)

    return new_dict



class FicHistoryNumFic:
    def __init__(self, csv_location):
        # creates the list of fics
        with open(csv_location, 'r') as fics_read:
            csv_reader = csv.reader(fics_read, delimiter=',')
            self.fic_list = []

            current_title = ""
            current_author = ""
            current_rating = ""
            current_word_count = 0
            current_tags = []
            current_fandoms = []
            current_ships = []

            line_count = 0

            for row in csv_reader:
                if line_count == 0:
                    line_count = line_count
                elif line_count == 1:
                    current_title = row[TITLE]
                    current_author = row[AUTHOR]
                    current_rating = row[RATING]
                    current_word_count = int((row[WORD_COUNT]).replace(",", ""))
                    current_fandoms = row[FANDOM].split('$') if len(row[FANDOM]) > 0 else []
                    current_ships = row[SHIPS].split('$') if len(row[SHIPS]) > 0 else []
                    current_tags = [row[TAGS]] if len(row[TAGS]) > 0 else []
                else:
                    # change these once I have a better web scraping csv method
                    if row[TITLE] == current_title:
                        if len(row[TAGS]) > 0:
                            current_tags.append(row[TAGS])
                        if len(row[FANDOM]) > 0:
                            for fandom in row[FANDOM].split('$'):
                                current_fandoms.append(fandom)
                        if len(row[SHIPS]) > 0:
                            for ship in row[SHIPS].split('$'):
                                current_ships.append(ship)
                    else:
                        self.fic_list.append(
                            Fanfiction(current_title, current_author, current_rating, current_word_count,
                                       current_fandoms, current_ships, current_tags))
                        current_title = row[TITLE]
                        current_author = row[AUTHOR]
                        current_rating = row[RATING]
                        current_word_count = int(row[WORD_COUNT].replace(',', ''))
                        current_fandoms = row[FANDOM].split('$') if len(row[FANDOM]) > 0 else []
                        current_ships = row[SHIPS].split('$') if len(row[SHIPS]) > 0 else []
                        current_tags = [row[TAGS]] if len(row[TAGS]) > 0 else []
                line_count += 1

            self.fic_list.append(Fanfiction(current_title, current_author, current_rating, current_word_count,
                                            current_fandoms, current_ships, current_tags))



        # ratings
        self.ratings = {"General Audiences": 0, "Teen And Up Audiences": 0, "Mature": 0, "Explicit": 0, "Not Rated": 0}
        for fic in self.fic_list:
            self.ratings[fic.rating] += 1

        # fandoms
        self.fandom_list = {}
        for fic in self.fic_list:
            for fandom in fic.fandoms:
                if fandom in self.fandom_list:
                    self.fandom_list[fandom] += 1
                else:
                    self.fandom_list[fandom] = 1
        self.fandom_list = order_dict(self.fandom_list)

        # ships
        self.ship_list = {}
        for fic in self.fic_list:
            for ship in fic.ships:
                if ship in self.ship_list:
                    self.ship_list[ship] += 1
                else:
                    self.ship_list[ship] = 1
        self.ship_list = order_dict(self.ship_list)

        # tags
        self.tag_list = {}

        # puts all tags in a list
        for fic in self.fic_list:
            for tag in fic.tags:
                if tag in self.tag_list:
                    self.tag_list[tag] += 1
                else:
                    self.tag_list[tag] = 1
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
        return len(self.fic_list)

    def top_rating(self):
        top_rating = ""
        top_rating_count = 0
        for rating in self.ratings:
            if self.ratings[rating] > top_rating_count:
                top_rating = rating
                top_rating_count = self.ratings[rating]

        return top_rating, top_rating_count

    def total_words_read(self):
        words_read = 0
        for fic in self.fic_list:
            words_read += fic.word_count

        return words_read

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
