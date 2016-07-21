HANDS = ('グー','チョキ','パー')


def select_hand():
    """
    コンピューターの手をランダムに決める
    :return:HAND'の中のいずれか。
    """
    import random

    random.choice(HANDS)

    return


def judgement(player , computer):
    """
    じゃんけんの勝敗を判定する。
    :param player:HANDSの中のどれか
    :param computer:HANDSの中のどれか
    :return:プレイヤーが勝ちの場合は１、あいこは０、負けは−１を返す
    """
    if player == computer:
        if player == 1 or player == 2 or player == 3:

            return 0

    else:
        if player == 1:
            if computer == 2:
                return 1
            if computer == 3:
                return -1
        if player == 2:
            if computer == 1:
                return -1
            if computer == 3:
                return 1
        if player == 3:
            if computer == 1:
                return 1
            if computer == 2:
                return -1


def save_score(result):
    """
    'score.txt'に戦績を保存。
    win:x lose:y draw:zのディクショナリデータを保存する。
    :param result:
    :return: None
    """
    f = open ("score.txt","w")

    pass

    res = {'win' : x , 'lose' : y, 'draw' : z}

    f.write(res)

    f.close()

    print >> f , "score.py"

    return

if __name__=='__main__':
    player = int (input('グー(1)/チョキ(2)/パー(3)を選んでください(数字):'))
    computer = select_hand()
    result =judgement(player , computer)
    #コンピューターの手と勝敗の結果を表示

    print(computer)

    print(result)

    save_score(result)