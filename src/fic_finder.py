from fanfiction_history import *

def print_menu():
    print("    Select an option")
    print("--------------------------")
    print("1. Deliver Wrapped")
    print("2. Print Available Fics")
    print("3. Filter Fics")
    print("4. Reset Filters")
    print("5. Print Current Filters")
    print("0. Exit")

def print_filters():
    print("Filters available:")
    print("1. Fandom")
    print("2. Rating")
    print("3. Word Count")
    print("4. Tags")


if __name__ == "__main__":
    fanfics = FanfictionHistory("fanfic_extraction.csv")


    screens = ["menu", "wrapped", "filter", "fandoms", "ratings", "word_count", "tags"]
    curr_screen = "menu"
    select = 'X'
    # [0: exclude, 1: include]
    filters = [
        {"fandoms": [], "ratings": [], "tags": []}, # exclude
        {"fandoms": [], "ratings": [], "tags": []}, # include
        [0, 100000000]
    ]

    print("WELCOME TO THE FANFIC FINDER")
    print()

    while True:
        if curr_screen == "menu":
            print_menu()
        elif curr_screen == "filters":
            print_filters()
        print()

        select = int(input("Selection: "))
        print()
        if select == 0:
            break
        if curr_screen == "menu":
            if select == 1:
                print("NO WRAPPED AVAILABLE AT THE MOMENT")
            elif select == 2:
                for fic in fanfics:
                    print(fic)
            elif select == 3:
                curr_screen = "filters"
            elif select == 4:
                filters = [
                    {"fandoms": [], "ratings": [], "tags": []},  # exclude
                    {"fandoms": [], "ratings": [], "tags": []},  # include
                    [0, 100000000]
                ]
                print("Filters reset")
                print()
            elif select == 5:
                print("Filters: ")
                print(filters)
        if curr_screen == "filters":
            if select == 1:
                print("Fandoms Available")
                fandoms = [0]
                count = 0
                for fandom in fanfics.top_fandoms(len(fanfics.fandom_list)):
                    fandoms.append(fandom)
                    count += 1
                    print(f"{count}. {fandom}")

                fandom = int(input("Number of fandom you would like to modify: "))
                in_ex = int(input("Include fandom (1) or Exclude fandom (0)?"))


                filters[in_ex]["fandoms"].append(fandoms[fandom])

                curr_screen = "menu"

