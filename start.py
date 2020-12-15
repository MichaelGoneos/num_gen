import os

from colorama import Fore

dir_path = "None"


def start():
    print(Fore.MAGENTA + """
███╗   ██╗██╗   ██╗███╗   ███╗     ██████╗ ███████╗███╗   ██╗
████╗  ██║██║   ██║████╗ ████║    ██╔════╝ ██╔════╝████╗  ██║
██╔██╗ ██║██║   ██║██╔████╔██║    ██║  ███╗█████╗  ██╔██╗ ██║
██║╚██╗██║██║   ██║██║╚██╔╝██║    ██║   ██║██╔══╝  ██║╚██╗██║
██║ ╚████║╚██████╔╝██║ ╚═╝ ██║    ╚██████╔╝███████╗██║ ╚████║
╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝     ╚═════╝ ╚══════╝╚═╝  ╚═══╝
                                                               """ + Fore.RESET)

    def ask_save():
        save_to_file = input("Save to file? Y/N\n> ")
        if save_to_file.lower() == "y":
            def ask_file_name():
                file_name = input("What would you like the file to be called?\n> ") + ".txt"
                os.path.exists(os.path.dirname(os.path.realpath(__file__)) + "/generated")
                global dir_path
                try:
                    os.mkdir(os.path.join(os.path.dirname(os.path.realpath(__file__)) + "/generated"))
                except FileExistsError:
                    pass
                if not os.path.exists(os.path.dirname(os.path.realpath(__file__)) + "/generated/" + file_name):
                    dir_path = os.path.join(os.path.dirname(os.path.realpath(__file__)) + "/generated/", file_name)
                else:
                    override = input("File already exists... override? Y/N\n> ")
                    if override.lower() == "y":
                        dir_path = os.path.join(os.path.dirname(os.path.realpath(__file__)) + "/generated/", file_name)
                    elif override.lower() == "n":
                        print("\n\n")
                        ask_file_name()

            ask_file_name()
        elif save_to_file.lower() == "n":
            print(Fore.YELLOW + "WARNING: " + Fore.RESET + "Only use with small amounts of numbers!")
        else:
            print("Invalid response... try again\n")
            ask_save()

    ask_save()
