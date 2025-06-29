def frequency(alphabet, text):
    repetitions = []
    for i in range(len(alphabet)):
        count = text.count(alphabet[i])
        repetitions.append([alphabet[i], count])
    return repetitions

def order_frequency(repetitions):
    frequencies = sorted(repetitions, key=lambda x: x[1], reverse=True)
    return frequencies

def replace_frequency(history_frequencies, text, frequencies):
    for i in range(5):
        letter_replace = frequencies[i][0]
        letter = history_frequencies[i]
        text = text.replace(letter_replace, letter.lower())
    return text

def replace_user(text, frequencies):
    remaining = "N S H R D L C U M W F G Y P B V K J X Q Z"
    for m in range(5, len(frequencies)):
        print("The letter", frequencies[m][0], "do you want to replace it with:")
        print(remaining)
        letter_replace_public = input("Type one of the above options:")
        letter_replace_public = letter_replace_public.lower()
        text = text.replace(frequencies[m][0], letter_replace_public)
        remaining = remaining.replace(letter_replace_public.upper(), '')
        print(text)
    return text

def replace_error(text):
    print("Desa modificar alguna letra")
    print("A. Yes        B.No")
    replace = input("Elije una opción: ")
    while replace.upper() == "A":
        letter_replace = input("Ingresa letra a modificar: ")
        letter_replace_new = input("Por cual desea cambiarla: ")
        text = text.replace(letter_replace.lower(),letter_replace_new.upper())
        print(text, flush=True)
        print("Desa modificar alguna letra")
        print("A. Yes        B.No")
        replace = input("Elije una opción: ")
    return text

text = "C LAIM HZVG CMA, ZI C MCLCKY OCS, OCS CWCY... ZH ZR C TCSD HZVG OAS HJG SGNGLLZAI. CLHJAUMJ HJG TGCHJ RHCS JCR NGGI TGRHSAYGT, ZVBGSZCL HSAABR JCPG TSZPGI HJG SGNGL OASFGR OSAV HJGZS JZTTGI NCRG CIT BUSRUGT HJGV CFSARR HJG MCLCKY. GPCTZIM HJG TSGCTGT ZVBGSZCL RHCSOLGGH, C MSAUB AO OSGGTAV OZMJHGSR LGT NY LUDG RDYWCLDGS JCR GRHCNLZRJGT C IGW RGFSGH NCRG AI HJG SGVAHG ZFG WASLT AO JAHJ. HJG GPZL LAST TCSHJ PCTGS, ANRGRRGT WZHJ OZITZIM YAUIM RDYWCLDGS, JCR TZRBCHFJGT HJAURCITR AO SGVAHG BSANGR ZIHA HJG OCS SGCFJGR AO RBCFG…"
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
history = "ETAOINSHRDLCUMWFGYPBVKJXQZ"
repetitions = frequency(alphabet, text)
frequencies = sorted(repetitions, key=lambda x: x[1], reverse=True)
print(frequencies)
first_replace = replace_frequency(history, text, frequencies)
print("The resulting text after replacing the most repeated letters with E, T, A, O, and I respectively is:", flush=True)
print(first_replace, flush=True)
final_text = replace_user(first_replace, frequencies)
print(final_text, flush=True)
print(replace_error(final_text))
