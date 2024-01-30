def div(numbers):
    try:
        result = numbers[0] / numbers[1]
    except IndexError:
        print('Треба мінімум два числа')
        return
    except ZeroDivisionError:
        print('Друге число не повинно бути 0')
        return
    except Exception as e:
        print('Піймали', e)
        return
    print(result)
# div([1,0])
# div([1])
# div(1)

def div(numbers):
    try:
        result = numbers[0] / numbers[1]
    except IndexError:
        print('Треба мінімум два числа')
        return
    except ZeroDivisionError:
        print('Друге число не повинно бути 0')
        return
    except Exception as e:
        print('Піймали', e)
        return
    finally:
        print('Функція відпрацювала')
    print(result)

# div([1,2])

def div(numbers):
    try:
        result = numbers[0] / numbers[1]
    except IndexError:
        print('Треба мінімум два числа')
        return
    except ZeroDivisionError:
        print('Друге число не повинно бути 0')
        return
    except Exception as e:
        print('Піймали', e)
        return
    else:
        print('Нічого не піймали')
    finally:
        print('Функція відпрацювала')
    print(result)

div([1,2])
