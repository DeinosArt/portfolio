import serveur.serverflask as serveurflask

import serveur.pythonanywhere_launch
application = serveur.pythonanywhere_launch.app

def main():
    print(f"starting!")
    serveurflask.start_serveur()

if __name__ == "__main__":
    main()

