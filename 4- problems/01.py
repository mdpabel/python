def sleep_in(weekday, vacation):
    if vacation == True:
        return True
    elif weekday == False:
        return True
    return False


print(sleep_in(False, False))
print(sleep_in(True, False))
print(sleep_in(False, True))
