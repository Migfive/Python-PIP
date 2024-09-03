try:
    print(0 / 0)
    assert 1 != 1, 'One is Equal to one'

    age = 10
    if age < 18:
        raise Exception('You are too young')

except ZeroDivisionError as e:
    print(e)
except AssertionError as e:
    print(e)
except Exception as e:
    print(e)

print('Hola')