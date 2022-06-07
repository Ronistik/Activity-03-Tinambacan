from sympy import Ordinal


class stat_calc():
    def hp_calculator(calc_HP, calc_IV, calc_EV, calc_Level):
        calc_total = ((2 * calc_HP + calc_IV + (calc_EV / 4)) * calc_Level/100) + calc_Level + 10
        return calc_total
    
    def attack_calculator(calc_Attack, calc_IV, calc_EV, calc_Level, calc_nature):
        if calc_nature > 0 or calc_nature < 5:
            nature_stat = 1.1
        elif calc_nature == 5 or calc_nature == 10 or calc_nature == 15 or calc_nature == 20:
            nature_stat = 0.9
        else :
            nature_stat = 1
        calc_total = (((2 * calc_Attack + calc_IV + (calc_EV / 4)) * calc_Level / 100) + 5) * nature_stat
        return calc_total

    def defense_calculator(calc_defense, calc_IV, calc_EV, calc_Level, calc_nature):
        if calc_nature == 5 or calc_nature == 7 or calc_nature == 8 or calc_nature == 9:
            nature_stat = 1.1
        elif calc_nature == 1 or calc_nature == 11 or calc_nature == 16 or calc_nature == 21:
            nature_stat = 0.9
        else :
            nature_stat = 1
        calc_total = (((2 * calc_defense + calc_IV + (calc_EV / 4)) * calc_Level / 100) + 5) * nature_stat
        return calc_total

    def SpAttack_calculator(calc_SpAttack, calc_IV, calc_EV, calc_Level, calc_nature):
        if calc_nature == 15 or calc_nature == 16 or calc_nature == 17 or calc_nature == 19:
            nature_stat = 1.1
        elif calc_nature == 3 or calc_nature == 8 or calc_nature == 13 or calc_nature == 23:
            nature_stat = 0.9
        else :
            nature_stat = 1
        calc_total = (((2 * calc_SpAttack + calc_IV + (calc_EV / 4)) * calc_Level / 100) + 5) * nature_stat
        return calc_total
    
    def SpDefense_calculator(calc_SpDefense, calc_IV, calc_EV, calc_Level, calc_nature):
        if calc_nature == 20 or calc_nature == 21 or calc_nature == 22 or calc_nature == 23:
            nature_stat = 1.1
        elif calc_nature == 4 or calc_nature == 9 or calc_nature == 14 or calc_nature == 19:
            nature_stat = 0.9
        else :
            nature_stat = 1
        calc_total = (((2 * calc_SpDefense + calc_IV + (calc_EV / 4)) * calc_Level / 100) + 5) * nature_stat
        return calc_total

    def Speed_calculator(calc_Speed, calc_IV, calc_EV, calc_Level, calc_nature):
        if calc_nature == 10 or calc_nature == 11 or calc_nature == 13 or calc_nature == 14:
            nature_stat = 1.1
        elif calc_nature == 2 or calc_nature == 7 or calc_nature == 17 or calc_nature == 22:
            nature_stat = 0.9
        else :
            nature_stat = 1
        calc_total = (((2 * calc_Speed + calc_IV + (calc_EV / 4)) * calc_Level / 100) + 5) * nature_stat
        return calc_total