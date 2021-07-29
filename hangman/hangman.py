class Hangman:
    HANG_MAN = ["___", "\n |", "\n O", "\n/", "|", "\\", "\n/", " \\"]
    TOTAL_GUESS = len(HANG_MAN)

    def __init__(self, difficulty='easy'):
        self._guess_remain = Hangman.TOTAL_GUESS
        self._word = Hangman._set_word(difficulty)
        self.board = []
        self._win = False

    @classmethod
    def _set_word(cls, difficulty='easy'):
        word = "HANGMAN"
        return word
        # TODO
        # get a random word of desired length

    def set_board(self):
        for i in range(len(self._word)):
            self.board.append("_")

    def check_alphabet(self, a):
        i = 0
        exists_status = False
        while i < len(self._word):
            if self._word[i] == a:
                self.board[i] = a
                exists_status = True
            i += 1
        return exists_status

    def check_win(self):
        self._win = '_' not in self.board
        return self._win

    def show_progress(self):
        """
        shows the current board of words
        :return:
        """
        print("".join(self.board), "\n")

    def draw_hangman(self):
        i = 0
        while i < (self.TOTAL_GUESS - self._guess_remain):
            print(self.HANG_MAN[i], end="")
            i += 1
        print("\n")

    def guess_remains(self):
        return self._guess_remain > 0

    def update_guess_remains(self):
        self._guess_remain -= 1

    @classmethod
    def run(cls):
        while True:
            game = Hangman()
            game.set_board()
            while game.guess_remains() and not game.check_win():
                # ask user for an alphabet
                alpha = input("Please select an alphabet: ").upper()
                if not game.check_alphabet(alpha):
                    game.update_guess_remains()
                    print("Sorry alphabet doesn't exists!!")
                    print("Remaining guesses: {}".format(game._guess_remain))
                game.show_progress()
                game.draw_hangman()

            if game._win:
                print("Congratulations!! You won!")
            else:
                print("Sorry.. you lost :(")

            # ask to play again
            again = input("Play again (y/n)?")
            if again.lower() == "n":
                print("quitting game...")
                break


if __name__ == '__main__':
    Hangman.run()
