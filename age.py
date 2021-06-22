driving = input('請問你有沒有開過車？')
if driving != '有' and driving != '沒有':
    print('只能輸入有或沒有！')
    raise SystemExit
age = input('請問你的年齡？')
age = int(age)
if driving == '有':
    if age >= 18:
        print('你通過測驗了！')
    else:
        print('你無照駕駛！')
elif driving == '沒有':
    if age < 18:
        print('再', 18-age, '年,等你考到駕照就可以開車了！')
    else:
        print('怎麼還不去考駕照？')