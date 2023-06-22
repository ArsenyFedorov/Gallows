from text import Text


class PrintInput:
    def __init__(self):
        self.txt = Text()

    def print_status(self, user_list: list):
        """Эта функция выводит сообщение о состояние слова"""
        print(self.txt.progress, *user_list)

    def print_message(self, message):
        print("=" * len(message))
        print(message)
        print("=" * len(message))

    def input_char(self) -> str:
        print("=" * len(self.txt.char))
        char = input(self.txt.char).upper().strip()
        print("=" * len(self.txt.char))
        return char

    def user_option(self):
        print("=" * len(self.txt.menu))
        print(self.txt.menu)
        option = input(self.txt.option).strip()
        print("=" * len(self.txt.menu))
        if option.isdigit() and 0 < int(option) < 3:
            return int(option)
        else:
            print("=" * len(self.txt.error))
            print(self.txt.error)
            print("=" * len(self.txt.error))
