from os import system
from time import sleep
import calculator_script_1_stat as stat_calculator
import calculator_script_2_EV as EV_calculator

def main():
    system('cls')
    print("Press 1 to calculate stats press 2 to calculate EV")
    mainctr = int(input("Option: "))
    if mainctr == 1:
        stat_input()
    elif mainctr == 2:
        EV_input()
    else:
        system('cls')
        print("Invalid input! /n Restarting in 5 seconds.")
        sleep(5)
        main()
    

def stat_input():
    try:
        system('cls')
        print("Enter the required stats")
        HP = int(input("Enter HP: "))
        Attack = int(input("Enter attack: "))
        Defense = int(input("Enter Defense: "))
        Special_Attack = int(input("Enter special attack: "))
        Special_Defense = int(input("Enter special defense: "))
        Speed = int(input("Enter speed: "))
        IV = int(input("Enter IV(0-31 only): "))
        if IV > 31 or IV < 0:
            print("Please enter between 0 and 31 only! /n Restarting in 3 seconds.")
            sleep(2)
            stat_input()
        EV = int(input("Enter EV(0-255 only): "))
        if EV > 255 or EV < 0:
            print("Please enter between 0 and 255 only! /n Restarting in 3 seconds.")
            sleep(2)
            stat_input()
        Level = int(input("Enter level: "))
        Nature = natur()
    except ValueError:
        print("Invalid Input!\n Restarting in 5 seconds.")
        sleep(5)
        stat_input()

    Total_HP = stat_calculator.stat_calc.hp_calculator(HP, IV, EV, Level)
    Total_Attack = stat_calculator.stat_calc.attack_calculator(Attack, IV, EV, Level, Nature)
    Total_Defense = stat_calculator.stat_calc.defense_calculator(Defense, IV, EV, Level, Nature)
    Total_SpAttack = stat_calculator.stat_calc.SpAttack_calculator(Special_Attack, IV, EV, Level, Nature)
    Total_SpDefense = stat_calculator.stat_calc.SpDefense_calculator(Special_Defense, IV, EV, Level, Nature)
    Total_Speed = stat_calculator.stat_calc.Speed_calculator(Speed, IV, EV, Level, Nature)

    system('cls')
    print("Your HP is:", Total_HP)
    print("Your Attack is:", Total_Attack)
    print("Your Defense is:", Total_Defense)
    print("Your SP Attack is:", Total_SpAttack)
    print("Your SP Defense is:", Total_SpDefense)
    print("Your Speed is:", Total_Speed)
    sleep(10)

    check()

def natur():
    print("""Enter the number of your pokemon's nature: 
    0. Hardy    5. Bold     10. Timid   15. Modest  20. Calm
    1. Lonely   6. Docile   11. Hasty   16. Mild    21. Gentle
    2. Brave    7. Relaxed  12. Serious 17. Quiet   22. Sassy
    3. Adamant  8. Impish   13. Jolly   18. Bashful 23. Careful
    4. Naughty  9. Lax     14. Naive   19. Rash    24. Quirky""")
    nature_input = int(input("Nature: "))
    return nature_input

def EV_input():
    system('cls')
    Stat = int(input("Enter desired increase in stat: "))
    Nature = natur()
    Level = int(input("Enter base level: "))
    IV = int(input("Enter IV(0 - 31 only!): "))
    if IV > 31 or IV < 0:
        print("Please enter between 0 and 31 only! /n Restarting in 3 seconds.")
        sleep(2)
        EV_input()
    EV = int(input("Enter ev(Please enter 0 - 255 only!): "))
    if EV > 255 or EV < 0:
        print("Please enter between 0 and 255 only! /n Restarting in 3 seconds.")
        sleep(2)
        EV_input()

    print("Press 1 to calculate all stat. \n Press 2 to calculate a single stat.")
    option = int(input("Option: "))
    if option == 1: #every stat is equal to the base_formula in next file
       HP = int(input("Enter HP: "))
       total_hp = EV_calculator.EV_calc.HP_formula(Stat, Nature, Level, HP, IV, EV)
       Attack = int(input("Enter Attack: "))
       total_Attack = EV_calculator.EV_calc.Attack_formula(Stat, Nature, Level, Attack, IV, EV)
       Defense = int(input("Enter Defense: "))
       total_Defense = EV_calculator.EV_calc.Defense_formula(Stat, Nature, Level, Defense, IV, EV)
       SP_Attack = int(input("Enter SP Attack: "))
       total_SpAttack = EV_calculator.EV_calc.SpAttack_formula(Stat, Nature, Level, SP_Attack, IV, EV)
       SP_Defense = int(input("Enter SP Defense: "))
       total_SpDefense = EV_calculator.EV_calc.SpDefense_formula(Stat, Nature, Level, SP_Defense, IV, EV)
       Speed = int(input("Enter Speed: "))
       total_Speed = EV_calculator.EV_calc.Speed_formula(Stat, Nature, Level, Speed, IV, EV)

       system('cls')
       print("EVs needed to get desired HP: ", total_hp)
       print("EVs needed to get desired Attack: ", total_Attack)
       print("EVs needed to get desired Defense: ", total_Defense)
       print("EVs needed to get desired SP Attack: ", total_SpAttack)
       print("EVs needed to get desired SP Defense: ", total_SpDefense)
       print("EVs needed to get desired Speed: ", total_Speed)
       sleep(5)
       check()

    elif option == 2:
            system('cls')
            print("""Enter desired stat to be calculated: 
            1. HP
            2. Attack
            3. Defense
            4. SP Attack
            5. SP Defense 
            6. Speed""")
            stat_option = int(input("Option: "))
            if stat_option == 1:
                system('cls')
                HP = int(input("Enter HP: "))
                total_hp = EV_calculator.EV_calc.HP_formula(Stat, Nature, Level, HP, IV, EV)
                print("EVs needed to get desired HP: ", total_hp)
                sleep(5)
                check()
            elif stat_option == 2:
                system('cls')
                Attack = int(input("Enter Attack: "))
                total_Attack = EV_calculator.EV_calc.Attack_formula(Stat, Nature, Level, Attack, IV, EV)
                print("EVs needed to get desired Attack: ", total_Attack)
                sleep(5)
                check()
            elif stat_option == 3:
                system('cls')
                Defense = int(input("Enter Defense: "))
                total_Defense = EV_calculator.EV_calc.Defense_formula(Stat, Nature, Level, Defense, IV, EV)
                print("EVs needed to get desired Defense: ", total_Defense)
                sleep(5)
                check()
            elif stat_option  == 4:
                system('cls')
                SP_Attack = int(input("Enter SP Attack: "))
                total_SpAttack = EV_calculator.EV_calc.SpAttack_formula(Stat, Nature, Level, SP_Attack, IV, EV)
                print("EVs needed to get desired SP Attack: ", total_SpAttack)
                sleep(5)
                check()
            elif stat_option == 5:
                system('cls')
                SP_Defense = int(input("Enter SP Defense: "))
                total_SpDefense = EV_calculator.EV_calc.SpDefense_formula(Stat, Nature, Level, SP_Defense, IV, EV)
                print("EVs needed to get desired SP Defense: ", total_SpDefense)
                sleep(5)
                check()
            elif stat_option == 6:
                system('cls')
                Speed = int(input("Enter Speed: "))
                total_Speed = EV_calculator.EV_calc.Speed_formula(Stat, Nature, Level, Speed, IV, EV)
                print("EVs needed to get desired Speed: ", total_Speed)
                sleep(5)
                check()

def check():
    system('cls')
    print("Press 1 to perform another computation /n Press 2 to exit")
    check_ctr = int(input("Opton: "))
    if check_ctr == 1:
        main()
    elif check_ctr == 2:
        exit()
    else:
        system('cls')
        print("Invalid input! /n Restarting in 5 seconds.")
        sleep(5)
        check()

main()