class Game:
    # 历史最高分
    topScore = 0
    def __init__(self,playerName):
        self.playerName = playerName

    @staticmethod
    def showHelp():
        print("帮助信息，让僵尸吃掉脑子")

    @classmethod
    def showTopScore(cls):

        print("历史最高分:%d" % cls.topScore)
    def startGame(self):

        print("开始游戏！%s" % self.playerName)

Game.showHelp()
Game.showTopScore()
game=Game("hh")
game.startGame()