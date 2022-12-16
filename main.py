from fanfiction_history import *

if __name__ == "__main__":
    fic_list = FanfictionHistory("fanfic_extraction.csv")

    print("------ WELCOME TO YOUR AO3 WRAPPED ------")
    print()
    print(f"You read a total of {fic_list.total_fics()} fanfictions")
    print(f"You read {fic_list.total_words_read()} words")
    print()
    top_rating = fic_list.top_rating()
    print(f"Your top rating was {top_rating[0]}. You read {top_rating[1]} with that rating.")
    print()
    print(f"You read from {fic_list.total_fandoms()} fandoms. Here are your top 10:")
    fic_list.print_top_fandoms(10)
    print()
    print(f"You read from {fic_list.total_ships()} ships. Here are your top 20:")
    fic_list.print_top_ships(20)
    print()
    print("Here are your top 3 tags: ")
    fic_list.print_top_tags(20)









