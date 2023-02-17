import random

MAX_LINES=3
MAX_BET=100
MIN_BET=1

ROWS=3
COLS=3

symbol_count={
    "A":2,
    "B":4,
    "C":6,
    "D":8
}

symbol_value={
    "A":8,
    "B":6,
    "C":4,
    "D":2
}

def check_winnings(columns,lines,bet,values):
    winnings=0
    winning_lines=[]
    for line in range(lines):
        symbol=columns[0][line]
        for column in columns:
            symbol_to_check=column[line]
            if symbol!=symbol_to_check:
                break
        else:
            winnings+=values[symbol]*bet
            winning_lines.append(line+1)

    return winnings,winning_lines


def get_slot_machine_spin(rows,cols,symbols):
    all_symbols=[]
    for symbol,symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    
    #row is col
    columns=[]
    for _ in range(cols):
        column=[]
        #copying to current symbols
        current_symbols=all_symbols[:]
        for _ in range(rows):
            value=random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)
    return columns


def print_slot_machine(columns):
    #transpose i,e row to col, col to row
    for row in range(len(columns[0])):
        for i,col in enumerate(columns):
            if i !=len(columns)-1:
                print(col[row], end=" | ")
            else:
                print(col[row], end=" ")
        print()


#collect user depoist amount inserted
def deposit():
    while True:
        amount=input("ENTER DEPOIST AMOUNT : ")
        if amount.isdigit():
            amount=int(amount)
            if amount>0:
                break
            else:
                print("AMOUNT MUST BE GREATER THAN 0,",end=" ")
        else:
            print("PLEASE ENTER VALID DEPOIST AMOUNT,",end=" ")
    return amount

#no of lines u want to bet on 
def get_number_of_lines():
    while True:
        no_of_lines=input("ENTER NUMBER OF LINES (1-"+str(MAX_LINES)+") : ")
        if no_of_lines.isdigit():
            no_of_lines=int(no_of_lines)
            if no_of_lines>=1 and no_of_lines<=MAX_LINES:
                break
            else:
                print("NUMBER OF LINES WHOULD BE WITH IN RANGE ,",end=" ")
        else:
            print("NUMBER OF LINES SHOULD BE INTEGER ,", end=" ")
    return no_of_lines

#AMOUNT U WANT TO BET
def get_bet():
    while True:
        amount=input("ENTER AMOUNT U LIKE TO BET ON EACH LINE:")
        if amount.isdigit():
            amount=int(amount)
            if MIN_BET<=amount<=MAX_BET:
                break
            else:
                print("BET AMOUNT MUST BE WITH IN ("+str(MIN_BET)+" "+str(MAX_BET)+")",end=" ")
        else:
            print("BET AMOUNT MUST BE INTEGER ,", end=" ")
    return amount



def game(balance):
    lines=get_number_of_lines()
    while True:
        bet=get_bet()
        total_bet=lines*bet
        if total_bet>balance:
            print("ENTERED BET IS EXCEEEDING DEPOIST BALANCE. CURRENT DEPOIST BALANCE = ",balance)
        else:
            break
    print(f"You are betting {bet} amount on {lines} lines. Total bet = {lines*bet}")
    slot_machine=get_slot_machine_spin(ROWS,COLS,symbol_count)
    print_slot_machine(slot_machine)
    winnings,winning_lines=check_winnings(slot_machine,lines,bet,symbol_value)
    print(f"YOU WON {winnings} :)")
    print(f"YOU WON ON ",*winning_lines) #print like u won on 1, u won on 2 * used as iter on list
    return winnings-total_bet

#amount u want to bet on each line 
def main():
    balance=deposit()
    while True:
        print(f"Current balance is ${balance}")
        spin=input("Press ENTER to Play (q to QUIT)")
        if spin=='q' or spin=="Q":
            break
        balance+=game(balance)
    print(f"you left with {balance}")


main()
