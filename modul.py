class Word:
    """Этот класс создаёт слово которое нужно угадать """
    def __init__(self, word: str):
        self.word = list(word)
        self.empty_word = [" -- " for i in range(len(self.word))]
        self.user_hp = 8

    def check(self, char: str):
        """Эта функция проверяет на то есть ли буква пользователя в загадоном слове"""
        for i in range(len(self.word)):
            if self.word[i] == char:
                self.empty_word[i] = char
        if char not in self.word:
            self.user_hp -= 1
