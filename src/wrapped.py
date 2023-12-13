# from fanfiction_history import *
from fic_history_combined import *

if __name__ == "__main__":
    fic_list = FicHistoryNumFic("./data/fic_scrape2023.csv")

    print("------ WELCOME TO YOUR AO3 WRAPPED ------")
    print()
    print(f"You read a total of {fic_list.total_fics()} fanfictions.")
    print(f"That's {fic_list.total_words_read()} words!")
    # print()
    top_rating = fic_list.top_rating()
    print(f"Your top rating was {top_rating[0]}.")
    print()
    print(f"You read from {fic_list.total_fandoms()} fandoms. Here are your top 5:")
    fic_list.print_top_fandoms(5)
    print()
    print(f"You read from {fic_list.total_ships()} ships. Here are your top 5:")
    fic_list.print_top_ships(5)
    print()
    print("Here are your top 10 tags: ")
    fic_list.print_top_tags(10)






