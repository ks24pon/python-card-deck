import random

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

# コンソールで確認
card1 = Deck()
card1.printDeck()

# コンソールでシャッフルされたデッキを確認
card1.shuffleDeck()
card1.printDeck()