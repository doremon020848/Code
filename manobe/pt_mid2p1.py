#!/usr/bin/env python3
# ธฯธรณ์
# 670510755
# 229223 Sec 001

def main():
    
    daily_expenses = ['20240803', 'coffee-dinner-laz-temu', '45-50-200-150']
    print(my_accounts(daily_expenses))
   
def my_accounts(daily_expenses):

    food = ['breakfast', 'lunch', 'dinner']
    drink = ['coffee', 'starbuck', 'amazon']
    shopping = ['laz', 'shop', 'temu']
    
    f1 = del_(daily_expenses)[0]
    ff = del_(daily_expenses)[-1]
    f2 = list(map(lambda x: int(x),ff))
    num = list(range(0, len(f1)))

    food_ = list(map(lambda x: 1 if x in food else 0 ,f1))
    drink_ = list(map(lambda x: 1 if x in drink else 0 ,f1))
    shopping_ = list(map(lambda x: 1 if x in shopping else 0 ,f1))
    
    food_2 = food_.count(1)
    drink_2 = drink_.count(1)
    shopping_2 = shopping_.count(1)
    
    if food_2 > drink_2 and food_2 > shopping_2:
        g1 = list(map(lambda x,y: f2[y] if x == 1 else None, food_,num))
        g2 = sum(list(filter(lambda x: x != None,g1)))
        return ['food'] + [g2]
    
    elif drink_2 > food_2 and drink_2 > shopping_2:
        g1 = list(map(lambda x,y: f2[y] if x == 1 else None, drink_,num))
        g2 = sum(list(filter(lambda x: x != None,g1)))
        return ['drink'] + [g2]
    
    elif shopping_2 > food_2 and shopping_2 > drink_2:
        g1 = list(map(lambda x,y: f2[y] if x == 1 else None, shopping_,num))
        g2 = sum(list(filter(lambda x: x != None,g1)))
        return ['shopping']  + [g2]
    
def del_(daily_expenses):
    del daily_expenses[0]
    f1 = list(map(lambda x: x.split('-'),daily_expenses))
    return f1 

if __name__ == '__main__':
    main()