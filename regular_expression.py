import re

data = [
        'c15103','c15104','c15202',
        'n16001', 'n16002','n16003','n16004','n16005','n16006','n16007','n16008','n16009',
        's16001','s16002','s16003','s16004','s16005','s16006','s16007','s16008','s16009',
        's16101','s16102','s16103','s16104','s16105','s16106','s16107',
]

str_data = str(data)
print('c15***',re.findall(r'c15[12]0[342]',str_data))
print('c15***',re.findall(r'c15\d{3}',str_data))
print('n161**',re.findall(r's161\d{2}',str_data))
print('*****3',re.findall(r'[scn]\d{4}3',str_data))