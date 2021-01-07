list_unit = ['U2', 'U3', 'U5', 'U6', 'U7']


def get_qeusetion():
    with open("TrueOrFalse.txt", 'r', encoding='utf-8') as p:
        text = p.readlines()
        datas = {'中英文化': {}, '综合教材': {}}
        for data in text:
            data = data.strip()
            if data in datas.keys():
                name = data
                continue
            if data in list_unit:
                unit = data
                datas[name][data] = []
            else:
                datas[name][unit].append(data)
    return datas


def bigin(questions):
    while True:
        for name in questions.keys():
            for unit in questions[name].keys():
                print(unit)
                for ques in questions[name][unit]:
                    print(ques[:-1])
                    A = ques[-1]
                    while True:
                        key = input("请输入你的答案(输入Q退出):").upper()
                        if key == 'Q' or key == 'q':
                            exit(0)
                        elif key == A:
                            print("回答正确！")
                            break
                        else:
                            print("回答错误！")
                            continue


if __name__ == '__main__':
    questions = get_qeusetion()
    bigin(questions)