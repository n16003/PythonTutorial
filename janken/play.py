import json

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
    if player == 0 and computer ==1:
        return 1
    if player ==1 and computer  ==2:
        return 1
    if player ==2 and computer  ==0:
        return 1
    else:
        return -1



def save_score(result):
    res = {"win":0, "lose":0, "draw":0}
    with open ("score.txt" ,"r") as f:
        res =json.load(f)
    with open('score.txt', 'w') as f:
        if result == 1:
            res["win"]  +=1
        if result == -1:
            res["lose"] +=1
        if result == 0:
            res["draw"] +=1
        strlist = json .dumps(res)
        f.write(strlist)
    return None

if __name__ == '__main__':
    player = int(input('グー(1)/チョキ(2)/パー(3)を選んでください(数字):'))-1
    computer = select_hand()
    result = judgement(player, computer)
    # コンピューターの手と勝敗の結果を表示
    print("computer:", HANDS[computer])
    print(result)
    save_score(result)
