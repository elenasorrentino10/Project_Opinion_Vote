from libraries.redis_connection import redis_connection
from libraries.display_menu import display_menu
from libraries.identify_user import identify_user
from libraries.insert_proposal import insert_proposal
from libraries.display_proposals import display_proposals
from libraries.vote_proposal import vote_proposal
from libraries.delete_user import delete_user
from libraries.flush_database import flush_database


def main():
    user = None
    r = redis_connection()

    while True:
        print('\n=== Vote my choice! ===')
        display_menu()
        choice = input('Enter your action (1-6): ')
        print()

        match choice:
            case '1':  # Identify user
                user = identify_user(r)

            case '2':  # Insert proposal
                if not user:
                    print('You need to identify yourself before submitting a proposal!')
                else:
                    insert_proposal(r, user)

            case '3':  # View proposals
                display_proposals(r)

            case '4':  # Vote a proposal
                if not user:
                    print('You need to identify yourself before voting a proposal!')
                else:
                    vote_proposal(r, user)

            case '5':  # Delete account
                if not user:
                    print("You need to identify yourself before deleting your account.")
                else:
                    delete_user(user, r)
                    user = None

            case '6':  # Flush/Clear Redis database
                flush_database(r)
                user = None

            case '0':  # Exit/Quit
                print("Exiting the program...")
                break

            case _:  # Invalid input handling
                print("Invalid choice. Please try again.")


if __name__ == '__main__':
    main()
