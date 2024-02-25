player_size = 3
# по умолчанию 3
board = list(range(1, player_size**2+1))
w_cor = tuple

def get_boar_size():
    print("__________ПРЕДУПРЕЖДЕНИЕ!!!__________")
    print("__Можно выбрать разумный размер поля!_")
    print("___Но выиграет тот кто выставит ряд___")
    print("_________равный размеру поля!_________")
    player_size = input("Размер поля: ")
    try:
        player_size = int(player_size)
        if player_size < 3 or player_size > 9:
            print("Минимальный размер 3Х3, максимальный 9Х9, попробуйте еще раз!")
            get_boar_size()
        return player_size
    except ValueError:
        print("Некорректный ввод. Вы уверены, что ввели число?")
        get_boar_size()

def draw_board(board, player_size):
#    print(board)
    print("-" * player_size * 5)
    i1 = 0
    res = "| "
    for i in range(player_size):
#        print(i)
        for i1 in range(player_size):
            str_res = board[i1 + i * player_size]
#            print(type(str_res))
            try:
                if str_res < 10:
                    res = res + " "
            except:
                res = res + " "
            res = res +str(str_res)+" | "
        print(str(res))
        print("-" * player_size * 5)
        res = "| "


def take_input(player_token):
    valid = False
    while not valid:
        player_answer = input("Куда поставим " + player_token + "? ")
        try:
            player_answer = int(player_answer)
        except ValueError:
            print("Некорректный ввод. Вы уверены, что ввели число?")
            continue
        if 1 <= player_answer <= player_size**2:
            if str(board[player_answer - 1]) not in "XO":
                board[player_answer - 1] = player_token
                valid = True
            else:
                print("Эта клетка уже занята!")
        else:
            print("Некорректный ввод. Введите число от 1 до "+str(player_size**2)+".")

def w_comb(board, player_size):
# Переберем строки
# Создадим матрицу
    m_rez = []
    c_m_rez = []
    c_m_rez2 = []
    c_list = []
    t1 = 0
    t2 = 0
    test = ""
    c_r = ""
    wc = tuple
# Переберем строки
    for i in range(player_size):
        c_list.append(int(i))
        for i1 in range(player_size):
            c_r = int(i1 + i * player_size)
            c_m_rez.append(c_r)
            if i1 == player_size-1:
                m_rez.append(c_m_rez)
                c_m_rez = []
# Переберем столбцы
    c_m_rez = m_rez
    for i in range(len(c_m_rez)):
        for j in range(len(c_m_rez[i])):
            c_m_rez2.append(int(c_m_rez[j][i]))
        m_rez.append(c_m_rez2)
        c_m_rez2 = []
# Переберем диагонали
# Самая простая
    c_m_rez = m_rez
    for i in range(len(c_m_rez)):
       for j in range(len(c_m_rez[i])):
            if i == j:
                c_m_rez2.append(int(c_m_rez[i][j]))
    m_rez.append(c_m_rez2)
    c_m_rez2 = []
# Обратная диагональ
    t2 = len(c_list)-1
    for i in range(len(c_list)):
        for j in reversed(c_list):
            if t1 == i and t2 == j:
                c_m_rez2.append(int(c_m_rez[j][i]))
                t1 = t1 + 1
                t2 = t2 - 1
    m_rez.append(c_m_rez2)
    c_m_rez2 = []
    wc = m_rez
    return wc

def chek_res(board, each, player_size):
    r_m = []
    for i in range(player_size):
        r_m.append(board[each[i]])
    if len(set(r_m)) == 1:
        return True
    else:
        return False

def check_win(board, player_size):
#  Как перебрать все выигрышные комбинации?
    w_comb(board, player_size)
    win_coord = w_comb(board, player_size)
#    print(win_coord)
    for each in win_coord:
# Копать тут!!!
        if chek_res(board, each, player_size):
            return board[each[0]]

    return False


def main(board, player_size):
    counter = 0
    win = False
    while not win:
        draw_board(board, player_size)
        if counter % 2 == 0:
            take_input("X")
        else:
            take_input("O")
        counter += 1

        tmp = check_win(board, player_size)
        if tmp:
            print(tmp, "выиграл!")
            win = True
            break
        if counter == player_size**2:
            print("Ничья!")
            break
    draw_board(board, player_size)

player_size = get_boar_size()
board = list(range(1, player_size**2+1))
main(board, player_size)

input("Нажмите Enter для выхода!")