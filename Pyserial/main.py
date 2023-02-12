# -*- coding: utf-8 -*-
from AutoOpenWeb import website
from BrailleDecode import braille_process
import time


COM_PORT = "None"
BAUD_RATE = 115200
URL = "https://www.facebook.com/"
flag = 1
flag2 = 1
pre_text = "None"
dem = 0
def openwb():
    global flag
    port = website().com_port_check()
    if port != "None":
        if flag == 1:
            print("Open", URL)
            time.sleep(1)
            #website().open()
            time.sleep(1)
            flag = 0
        else:
            pass
    else:
        flag = 1

    #print("Port: {}, Web status: {}".format(port, flag))
    time.sleep(1)
    return port

while True: 
    COM_PORT = website().com_port_check()
    if COM_PORT != "None":
        braille = braille_process(COM_PORT, BAUD_RATE)
        braille_alphabet = braille.alphabet()
        count_text = braille.count_Encode()
        vietnamese_decode = braille.vietnamese_Encode()
        break

while True:
    openwb()
    if COM_PORT != "None":
        key_website = braille.keypad()
        key = key_website
        if (key):
            print(key)

    text_website = input("Nhap tu: ")
    text = text_website
    if text != "None":
        text = text.lower().strip()
        if text != pre_text:
            flag2 = 1

        if COM_PORT != "None" and flag2 == 1: # Servo control function: Finished
            pre_text = text
            vietnamese_decoded_text = []
            vietnamese_accent = ""
            text_without_accent = ""
            demkhongdau = 0
            demcodau = 0
            for i in text:
                
                try:
                    vietnamese_decoded_text.append(vietnamese_decode[i]) 
                    demcodau += 1
                except:
                    vietnamese_decoded_text.append(i)
                    if demcodau < 1:
                        demkhongdau += 1
                    else:
                        continue
                
                """  if vietnamese_decode[i] == "None":
                    vietnamese_decoded_text = braille_alphabet[i]
                else:
                    vietnamese_decoded_text = vietnamese_decode[i] """
                #bán = bsaan
            
            print(vietnamese_decoded_text)
            print("Chữ có dấu nằm ở vị trí thứ: ", demkhongdau)
            print("dấu là: ", vietnamese_decoded_text[demkhongdau][:2])
            print("Chữ chứa dấu là: ", vietnamese_decoded_text[demkhongdau][2:])
            
            chuchuadau = vietnamese_decoded_text[demkhongdau][2:]
            vietnamese_decoded_text[demkhongdau] = vietnamese_decoded_text[demkhongdau][:2]
            
            print(vietnamese_decoded_text[demkhongdau][2:])
            vietnamese_decoded_text.insert(demkhongdau + 1, chuchuadau )
            print(vietnamese_decoded_text)
            
    #ắ   saă
            for j in vietnamese_decoded_text:
                dem += 1
                decoded_count = count_text[str(dem)]
                decoded_text = decoded_count + braille_alphabet[j] 
                print(decoded_text) 
                braille.on(decoded_text,2)
            if dem >= len(vietnamese_decoded_text):
                dem = 0 
                
            """ decoded_count = count_text[str(dem)]
            decoded_text =decoded_count + braille_alphabet[i] 
            print(decoded_text)
            braille.on(decoded_text,2) """
                
            
            """ if (i == text[len(text)-1]):
                braille.off(1) """
            
            flag2 = 0



