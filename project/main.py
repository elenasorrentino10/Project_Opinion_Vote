from libraries.redis_connection import redis_connection
from libraries.identify_user import identify_user
from libraries.delete_user import delete_user
from libraries.flush_database import flush_database
from libraries.display_menu import display_menu
from libraries.insert_proposal import insert_proposal
from libraries.vote_proposal import vote_proposal



def display_proposals():
    ...


def main():
    user_id = None
    r = redis_connection()

    while True:
        print('\n=== Vote my choice! ===')
        display_menu()
        choice = input('Enter your action (1-7): ')
        print()

        match choice:
            case '1':  # Identifica l'utente della applicazione
                user_id = identify_user(r)

            case '2':  # Inserisci una proposta da votare
                if not user_id:
                    print('You need to identify yourself before writing a message!')
                else:
                    insert_proposal(r, user_id)

            case '3':  # Visualizza le proposte da votare
                ...

            case '4':  # Dai il tuo voto a una proposta
                if not user_id:
                    print('You need to identify yourself before writing a message!')
                else:
                    vote_proposal(r, user_id)                

            case '5':  # Esci dal programma
                print("Exiting the program...")
                break

            case '6':  # Elimina l'utente
                if not user_id:
                    print("You need to identify yourself before deleting your user.")
                else:
                    delete_user(user_id, r)
                    user_id = None

            case '7':  # Svuota il database redis
                flush_database(r)
                user_id = None

            case _:
                print("Invalid choice. Please try again.")


if __name__ == '__main__':
    main()
