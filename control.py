from console import PrintInput
from modul import Word


class Star:
    def __init__(self):
        self.console = PrintInput()
        self.word = Word("КОТ")

    def start_game(self):
        while True:
            option = self.console.user_option()
            self.word.empty_word = [" -- " for i in range(len(self.word.word))]
            match option:
                case 1:
                    while True:
                        if self.word.user_hp == 0:
                            self.console.print_message(self.console.txt.death)
                            break
                        elif " -- " not in self.word.empty_word:
                            self.console.print_message(self.console.txt.win)
                            break
                        else:
                            self.console.print_status(self.word.empty_word)
                            char = self.console.input_char()
                            if char in self.word.empty_word:
                                self.console.print_message(self.console.txt.repeat)
                                continue
                            self.word.check(char)
                            if char not in self.word.word:
                                self.console.print_message(self.console.txt.miss)
                            else:
                                self.console.print_message(self.console.txt.shot)
                case 2:
                    self.console.print_message(self.console.txt.game_over)
                    break
