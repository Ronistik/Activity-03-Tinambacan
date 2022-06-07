class EV_calc():

    def HP_formula(stat_formula, nature_formula, level_formula, base_formula, IV_formula, EV_formula):
        D_total = ((2 * base_formula + IV_formula + (EV_formula / 4)) * (level_formula/100))
        nature_formula = 1
        total = ((((stat_formula / nature_formula) - D_total) * 400 / level_formula) / 4) * 4
        return total
        
    def Attack_formula(stat_formula, nature_formula, level_formula, base_formula, IV_formula, EV_formula):
        D_total = ((2 * base_formula + IV_formula + (EV_formula / 4)) * (level_formula/100))
        if nature_formula > 0 and nature_formula < 5:
            nature_formula = 1.1
        elif nature_formula == 5 or nature_formula == 10 or nature_formula == 15 or nature_formula == 20:
            nature_formula = 0.9 
        else:
            nature_formula = 1
        total = ((((stat_formula / nature_formula) - D_total) * 400 / level_formula) / 4) * 4
        return total

    def Defense_formula(stat_formula, nature_formula, level_formula, base_formula, IV_formula, EV_formula):
        D_total = ((2 * base_formula + IV_formula + (EV_formula / 4)) * (level_formula/100))
        if nature_formula == 5 or nature_formula == 7 or nature_formula == 8 or nature_formula == 9:
            nature_formula = 1.1
        elif nature_formula == 1 or nature_formula == 11 or nature_formula == 16 or nature_formula == 21:
            nature_formula = 0.9 
        else:
            nature_formula = 1
        total = ((((stat_formula / nature_formula) - D_total) * 400 / level_formula) / 4) * 4
        return total

    def SpAttack_formula(stat_formula, nature_formula, level_formula, base_formula, IV_formula, EV_formula):
        D_total = ((2 * base_formula + IV_formula + (EV_formula / 4)) * (level_formula/100))
        if nature_formula == 15 or nature_formula == 16 or nature_formula == 17 or nature_formula == 19:
            nature_formula = 1.1
        elif nature_formula == 3 or nature_formula == 8 or nature_formula == 13 or nature_formula == 23:
            nature_formula = 0.9 
        else:
            nature_formula = 1
        total = ((((stat_formula / nature_formula) - D_total) * 400 / level_formula) / 4) * 4
        return total

    def SpDefense_formula(stat_formula, nature_formula, level_formula, base_formula, IV_formula, EV_formula):
        D_total = ((2 * base_formula + IV_formula + (EV_formula / 4)) * (level_formula/100))
        if nature_formula > 19 and nature_formula < 24:
            nature_formula = 1.1
        elif nature_formula == 4 or nature_formula == 9 or nature_formula == 14 or nature_formula == 19:
            nature_formula = 0.9 
        else:
            nature_formula = 1
        total = ((((stat_formula / nature_formula) - D_total) * 400 / level_formula) / 4) * 4
        return total

    def Speed_formula(stat_formula, nature_formula, level_formula, base_formula, IV_formula, EV_formula):
        D_total = ((2 * base_formula + IV_formula + (EV_formula / 4)) * (level_formula/100))
        if nature_formula == 10 or nature_formula == 11 or nature_formula == 13 or nature_formula == 14:
            nature_formula = 1.1
        elif nature_formula == 2 or nature_formula == 7 or nature_formula == 17 or nature_formula == 22:
            nature_formula = 0.9 
        else:
            nature_formula = 1
        total = ((((stat_formula / nature_formula) - D_total) * 400 / level_formula) / 4) * 4
        return total