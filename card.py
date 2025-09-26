import random

# カード
class Card:
  # インスタンス生成のためのコンストラクタ
  def __init__(self, value, suit, intValue):
    self.value = value
    self.suit = suit
    self.intValue = intValue

  # オブジェクトの状態を表示する関数
  def getCardString(self):
    return self.suit + self.value + "(" + str(self.intValue) + ")"

# デッキ
class Deck:
  # コンストラクタ
  def __init__(self):
    self.deck = self.generateDeck()

  # デッキを生み出す関数
  @staticmethod
  def generateDeck():
    newDeck = []
    values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    suits = ["♣", "♦", "♥", "♠"]

    for suit in suits:
      for i, value in enumerate(values):
        newDeck.append(Card(value, suit, i + 1))

    return newDeck

  # カードをドロー
  def draw(self):
    return self.deck.pop()

  # デッキにあるカードを全て表示
  def printDeck(self):
      print("Displaying cards...")
      for card in self.deck:
        print(card.getCardString())

  # カードをランダムに入れ替える関数
  def shuffleDeck(self):
    deckSize = len(self.deck)
    for i in range(deckSize -1, 0, -1):
      j = random.randint(i, deckSize-1)
      temp = self.deck[i]
      self.deck[i] = self.deck[j]
      self.deck[j] = temp

# ディーラー
class Dealer:

    @staticmethod
    def startGame(amountOfPlayers, gameMode):
      table = {
        "players": [],
        "gameMode": gameMode,
        "deck": Deck()
      }

      table["deck"].shuffleDeck()

      for person in range(0, amountOfPlayers):
        playerCard = []
        # ブラックジャックの時から書き換え
        for i in range(0, Dealer.initialCards(gameMode)):
            playerCard.append(table["deck"].draw())
        table["players"].append(playerCard)

      return table["players"]

    # ゲームの内容によって手札を変更
    @staticmethod
    def initialCards(gameMode):
        if gameMode == "21":
            return 2
        if gameMode == "poker":
            return 5

# 卓の設定2 players、ポーカー
table1 = Dealer.startGame(2, "poker")

# 1人目のplayerの手札をfor文で出力
for i in range (0,Dealer.initialCards("poker")):
  print(table1[0][i].getCardString())