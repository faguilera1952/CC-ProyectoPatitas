class user:
    def __init__(self):
        self.profile = None

def main():
    admin = user()
    noAdmin = user()

    print(f'el usuario es{noAdmin.profile} profile.')
if __name__ == '_main_':
    main()