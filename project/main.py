from libraries.redis_connection import redis_connection
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


def insert_proposal():
    ...


def display_proposals():
    ...


def vote_proposal():
    ...


def exit_program():
    ...


def delete_user():
    ...


def flush_database():
    ...


def main():
    r = redis_connection()


if __name__ == '__main__':
    main()
