import random 
def get_numbers_ticket(n):
    min = 1
    max = 1000 
    lottery_numbers_list = [] #робе список
    for i in range(n): 
        lottery_numbers = random.randrange(min, max)
        print("Ваші лотерейні числа:", lottery_numbers)
 
if __name__ == '__main__':
    get_numbers_ticket(11) #колв квитків
