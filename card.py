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
        # 入るカードが何か確認
        print(Card(value, suit, i + 1).getCardString())
        newDeck.append(Card(value, suit, i + 1))
    
    return newDeck

# デッキ生成
Deck()
