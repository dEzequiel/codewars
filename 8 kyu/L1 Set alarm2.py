def set_alarm(employed, vacation):
    # Your code here
    if employed == True and not vacation:
        return True;
    else:
        return False;