import random
lst_imen=list()
def imena():
    with open('in.txt', 'r') as file_in:
        for i in file_in:
            lst_imen.append(i.strip())
    return random.choice(lst_imen)

def generate_random_number(length):
    return ''.join([str(random.randint(0,10)) for _ in range(length-1)])
def multi_list():
    return f'http://learn.skillup.ua/room/intqa_wb1_1?username={imena()}&email={imena()}{generate_random_number(1)}%40email.ua&phone=%2B380{generate_random_number(9)}&autologin=0&lead=c{generate_random_number(2)}ed{generate_random_number(4)}aa-{generate_random_number(2)}x{generate_random_number(4)}-{generate_random_number(4)}cx{generate_random_number(4)}-bx{generate_random_number(4)}d-cb{generate_random_number(4)}d{generate_random_number(4)}{generate_random_number(4)}1{generate_random_number(4)}0'

