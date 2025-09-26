class Card:
  # インスタンス生成のためのコンストラクタ
  def __init__(self, value, suit, intValue):
    self.value = value
    self.suit = suit
    self.intValue = intValue

  # オブジェクトの状態を表示する関数
  def getCardString(self):
    return self.suit + self.value + "(" + str(self.intValue) + ")"

# 新しくカードを作成し、カード情報を返す関数を使用します
# card1はヒープを指しています。したがってcard1にはヒープアドレスが保存されています。
card1 = Card("A","♦︎",1)

# 出力
print(card1.getCardString())