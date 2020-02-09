'''Apple クラス'''
class Apple:

    '''初期化メソッド(インスタンス変数の定義)'''
    def __init__(self, w, c):
        self.weight = w
        self.color = c

    '''インスタンスメソッドの定義'''
    def fresh(self, days, temp):
        self.freshness = days*temp
        print(f"入荷してから{days}日、平均{temp}度で保管されており新鮮度は{self.freshness}です。") 
