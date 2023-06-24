from libraries.redis_connection import redis_connection
from libraries.identify_user import identify_user
from libraries.delete_user import delete_user
from libraries.flush_database import flush_database
from libraries.display_menu import display_menu


def insert_proposal():
    ...


def display_proposals():
    ...


def vote_proposal():
    ...


def main():
    user_id = None
    r = redis_connection()

    while True:
        print('\n=== Vote my choice! ===')
        display_menu()
        choice = input('Enter your action (1-6): ')

        match choice:
            case '1':  # Identifica l'utente della applicazione
                user_id = identify_user(r)
            case '2':  # Inserisci una proposta da votare
                if not user_id:
                    print('You need to identify yourself before writing a message!')
                else:
                    ...
            case '3':  # Visualizza le proposte da votare
                ...
                # proposals = read_all_proposal() # leggi tutte le proposte
                # if not chat_messages:
                #    print("No chat messages available.")
                # else:
                #    print("Last 10 chat messages:")
                #    print_chat_messages(chat_messages)

            case '4':  # Dai il tuo voto a una proposta
                ...
            case 'q':  # Esci dal programma
                print("Exiting the program...")
                break
            case 'd':  # Elimina l'utente
                if not user_id:
                    print("You need to identify yourself before deleting your user.")
                else:
                    delete_user(user_id, r)
                    user_id = None
            case 'dd':  # Svuota il database redis
                flush_database(r)
                user_id = None
            case _:
                print("Invalid choice. Please try again.")


if __name__ == '__main__':
    main()
