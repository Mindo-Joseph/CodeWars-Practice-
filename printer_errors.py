def printer_error(s):
    total_length_string= len(s)
    total_missed = 0
    for char in s :
        if char > "m":
            total_missed+=1
    return str(total_missed)+"/"+str(total_length_string)


print(printer_error("aaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyz"))