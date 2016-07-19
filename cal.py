def cal(year , month=1, day=1 ):
    """
    年月日から曜日を計算します
        曜日は０（日曜）から６（土曜）の数値で表現します

    :param year: 西暦４桁
    :param month: 月
    :param day: 日
    :return: ０−６（日曜ー土曜）
    """

    _year =year
    _month = month
    _day  = day

    if month == 1 or month == 2:
        _year = year -1
        _month = month +13
    else:
        _month = month +1

    aa =  int(_year * 365.25 )
    bb =  int( _month * 30.6)
    cc =  _year // 400
    dd =  _year // 100

    ee =  aa+bb+cc+_day - dd - 429
    ff =  ee // 7 * 7

    return (ee - ff + 1) % 7

#西暦を入力してもらい、その年のカレンダーを表示

#year = int(input('西暦を入力してください'))

