def create_phone_number(n):
    #your code here

    #PREFIX
    list_prefix = []

    for prefix in n[:3]:
        list_prefix.append(str(prefix))

    styled_prefix = ''.join(list_prefix)
    final_prefix = "("+styled_prefix+")"+" "


    #MID NUMBERS
    list_midnum = []

    for num in n[3:6]:
        list_midnum.append(str(num))

    styled_mid  = ''.join(list_midnum)
    final_mid = styled_mid+"-"

    #FINAL NUMBERS
    list_finalnum = []
    for num in n [6:]:
        list_finalnum.append(str(num))

    styled_final = ''.join(list_finalnum)

    return final_prefix+final_mid+styled_final
