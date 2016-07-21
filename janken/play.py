HANDS = ('グー', 'チョキ', 'パー')


def select_hand():
    """
    コンピューターの手をランダムに決める
    :return:HAND'の中のいずれか。
    """
    import random

    a = random.randint(0, 2)

    return a


def judgement(player, computer):
    if player == computer:

        return 0

    else:
        if player == 1:
            if computer == 1:
                return 1
            if computer == 2:
                return -1
        if player == 2:
            if computer == 0:
                return -1
            if computer == 2:
                return 1
        if player == 3:
            if computer == 0:
                return 1
            if computer == 1:
                return -1


def save_score(result):
    f = open("score.txt", "w")
    x = y = z == 0
    res = {'win': x, 'lose': y, 'draw': z}

    if judgement() == 0:
        res['draw'] += 1

    if judgement() == 1:
        res['win'] += 1

    if judgement() == -1:
        res['lose'] += 1

    f.write(res)

    f.close()

    print>>f, "score.py"

    return

if __name__ == '__main__':
    player = int(input('グー(1)/チョキ(2)/パー(3)を選んでください(数字):'))
    computer = select_hand()
    result = judgement(player, computer)
    # コンピューターの手と勝敗の結果を表示

    print("computer:", HANDS[computer])

    print(result)

    save_score(result)
