from utils import load_data

def show1():
    """
    возвращает список с данными всех кандидатов
    :return:
    """
    data = load_data()
    li = []
    for d in data:
        li.append(d['name'] + ' -')
        li.append(d['position'])
        li.append(d['skills'].capitalize())
        li.append(' ')
    return li


def show2(id):
    """
    возврат список с данными кандидатов
    :param id:
    :return:
    """
    data = load_data()
    info = data[id-1]
    li = []
    li.append(info['picture'])
    li.append(info['name'])
    li.append(info['position'])
    li.append(info['skills'])
    return li

def show_with_pre(li):

    """
    оформление для роута candidates/<x>
    :param li:
    :return:
    """
    res = '<pre>'

    res += f"""
        {li[1]}\n
        {li[2]}\n
        {li[3]}\n
        """
    res += '</pre>'
    return res


def get_u_by_skills(skill):
    """
    возврат кандидатов имеющих определенный скилл
    :param skill:
    :return:
    """
    data = load_data()
    li = []
    for i in range(len(data)):
        if skill in data[i]['skills'].lower():
            li.append(data[i]['name'] + ' -')
            li.append(data[i]['position'])
            li.append(data[i]['skills'].capitalize())
            li.append('')
    return li
