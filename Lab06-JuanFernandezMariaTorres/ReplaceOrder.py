def enc(abc,key,str):
    for i in range (len(abc)):
        str = str.replace(abc[i],key[i].lower())    
    str = str.upper()
    return str
    
abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

#Excersice 1:
key = "BVZPMEXSRUAKYIWHOTCFDNJQLG"
str = "THERE IS NOTHING IMPOSSIBLE TO THEY WHO WILL TRY"
print("Excersice 1")
print(enc(abc,key,str))

#Excersice 2:
str = "SEFKWLREHKIF MC WIV KEHSWMSV HTZ CWDZF LY CVSDEV SLOODTMSHWMLT MT WIV KEVCVTSV LY HZQVECHEMVC. MW MTQLAQVC WIV DCV LY QHEMLDC HARLEMWIOC WL VTSLZV HTZ ZVSLZV MTYLEOHWMLT MT H NHF WIHW SHT LTAF JV DTZVECWLLZ JF HDWILEMPVZ KHEWMVC"
key = "HJSZVYRIMUBAOTLKXECWDQNGFP"
print("Excersice 2")
print(enc(key,abc,str))

