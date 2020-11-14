from random import randint

class System:
    def bot(self):
        x = ['r', 'p', 's']
        return x[randint(0,2)]

    def sys_gameOver(self, user, bot):
        if bot == user:
            return 0
        else:
            if bot == 'r':
                if user == 'p':
                    return 1
                elif user == 's':
                    return 2

            elif bot == 'p':
                if user == 'r':
                    return 2
                elif user == 's':
                    return 1

            else:
                if user == 'p':
                    return 2
                elif user == 'r':
                    return 1