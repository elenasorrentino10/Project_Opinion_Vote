from libraries.redis_connection import redis_connection
from libraries.identify_user import identify_user
from libraries.delete_user import delete_user
from libraries.flush_database import clear_database
import redis


def display_menu():
    ...
    # 1. Identifica utente
    # 2. Inserisci proposta
    # 3. Visualizza proposte
    # 4. Vota proposta
    # 5. Esci/chiudi programma
    # d. Cancella utente
    # dd. Pulisci database flushall


def get_choice():
    ...
    # 1, 2, 3, 4, 5


def identify():
    ...


def insert_proposal():
    ...


def display_proposals():
    ...


def vote_proposal():
    ...


def exit_program():
    ...


def flush_database():
    ...


def main():
    user_id = None
    r = redis_connection()

    while True:
        print('\n=== Chat Program ===')
        display_menu()
        choice = input('Enter your choice (1-6): ')

        match choice:
            case '1':
                user_id = identify_user(user_id, r)
            case '2':
                if not user_id:
                    print('You need to identify yourself before writing a message!')
                else:
                    ...
            case '3':
                ...
                # proposals = read_all_proposal() # leggi tutte le proposte
                # if not chat_messages:
                #    print("No chat messages available.")
                # else:
                #    print("Last 10 chat messages:")
                #    print_chat_messages(chat_messages)
            case 'd':
                if not user_id:
                    print("You need to identify yourself before deleting your user.")
                else:
                    delete_user(user_id, r)
                    print("User deleted successfully!")
                    user_id = None
            case 'dd':
                confirm = input("Are you sure you want to clear the database? This action cannot be undone. (y/n): ")
                if confirm.lower() == 'y':
                    clear_database(r)
                    print("Database cleared successfully!")
                    user_id = None
                else:
                    print("Clear database operation canceled.")

            case '6':
                print("Exiting the program...")
                break

            case default:
                print("Invalid choice. Please try again.")


if __name__ == '__main__':
    main()
