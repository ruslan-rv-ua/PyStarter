from typing import Union

# type number = int | float

def double_number(x:int|float) -> int | float:
# def double_number(x:Union[int, float]) -> Union[int, float]:
# def double_number(x:number) -> number:
    return x * 2
    
i = double_number(2)
f = double_number(2.0)
s = double_number("2")

n = input('Введіть ціле число: ')
print(1 + double_number(n))