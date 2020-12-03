from bayesian.bbn import build_bbn

def f_prize_door(prize_door):
    return 0.33333333
def f_guest_door(guest_door):
    return 0.33333333
def f_monty_door(prize_door, guest_door, monty_door):
    if prize_door == guest_door:  # 参赛者猜对了
        if prize_door == monty_door:
            return 0     # Monty不会打开有车的那扇门，不可能发生
        else:
            return 0.5   # Monty会打开其它两扇门，二选一
    elif prize_door == monty_door:
        return 0         #  Monty不会打开有车的那扇门，不可能发生
    elif guest_door == monty_door:
        return 0         # 门已经由参赛者选定，不可能发生
    else:
        return 1    # Monty打开另一扇有羊的门

if __name__ == '__main__':
    g = build_bbn(
        f_prize_door,
        f_guest_door,
        f_monty_door,
        domains=dict(
            prize_door=['A', 'B', 'C'],
            guest_door=['A', 'B', 'C'],
            monty_door=['A', 'B', 'C']))

    g.q()
    g.q(guest_door='A')
g.q(guest_door='A', monty_door='B')

