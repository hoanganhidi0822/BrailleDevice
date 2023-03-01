#pyinstaller --onefile --icon=dist\product.ico main.py

from AutoOpenWeb import website
import time
import socketio

sio = socketio.Client()
wb = website()

COM_PORT = "COM4"
BAUD_RATE = 115200
URL = "https://www.facebook.com/"
flag = 1
flag2 = 1
pre_text = "None"
key_list = ["DETECT", "LESSONS", "BACK", "ENTER", "RIGHT", "LEFT", "AGAIN", "INPUT"]
text_input = "hi"
text_local = ""

dem = 0
dem1 = 0
tempcount = 0 
vietnamese_decoded_text = []
accent_text_position = []
demkhongdau = 0
demcodau = 0
count = 0
temp = 0


""" def emit_server(task, place, content):
    data = {
        "task": task,
        "place": place,
        "content": content
    }
    sio.emit("server_client_local", data)

@sio.event
def message_client_local(data):
    global text_local
    if (data["task"] == "TexttoController"):
        if (data["content"] != None):
            text_local = data["content"]
            print('message received with ', data, text_local)
            return text_local

@sio.event
def connect():
    print('connection')
    emit_server("Notification", "none", "connect to server")

@sio.event
def disconnect():
    print('disconnection')
    emit_server("Notification", "none", "disconnect to server")

 """

while True: 
    COM_PORT = website().com_port_check()
    if COM_PORT != "None":
        print("COM_PORT:", COM_PORT)
        from BrailleDecode import braille_process
        braille = braille_process(COM_PORT, BAUD_RATE)
        braille_alphabet = braille.alphabet()  
        count_text = braille.count_Encode()
        vietnamese_decode = braille.vietnamese_Encode()   
        #wb.open_once_time()
        
        while COM_PORT != "None":
            #sio.connect('http://192.168.0.107:6868', wait_timeout=10)
            if flag2 == 1:
                print("All brailles off")
                braille.off(1)
                flag2 = 0

            COM_PORT = wb.com_port_check()

            time.sleep(1)
            key_website = braille.keypad()
           # emit_server("TextoControllerWeb", "page_home", key_website)
            key = key_website
            if (key in key_list):
                print("key:", key)

            if key == "INPUT":
                vietnamese_decoded_text = []
                text_input = input("Nhap tu: ")
                text_website = text_input
            else:

                text_website = input("Nhập từ: ") #text_local
                
            text = text_website
            if text != "None":
                text = text.lower().strip() 
                if text != pre_text:
                    flag = 1
                else:
                    flag = 0

                if flag == 1: # Servo control function: Finished
                    pre_text = text
                    
                    for i in text:
                        
                        try:
                            vietnamese_decoded_text.append(vietnamese_decode[i])
                            temp = count 
                            accent_text_position.append(temp)
                            demcodau += 1      
                        except:
                            vietnamese_decoded_text.append(i)
                            demkhongdau += 1
                        count += 1
                        
                        print("vietnamese_decoded_text: ",vietnamese_decoded_text)
                        flag = 0
                        COM_PORT = wb.com_port_check()
                        text_website = "None"
                    
                    print("accent_pos: ", accent_text_position)
                    if demcodau == 0:
                        accent_text_position = None  
                             
                    """ if len(vietnamese_decoded_text) > 8:
                        del vietnamese_decoded_text[8:]  """     
                          
                    if accent_text_position != None:
                        
                        for accent_text_pos in accent_text_position:
                            vietnamese_accent = vietnamese_decoded_text[accent_text_pos + dem1][:2]
                            vietnamese_accent_text = vietnamese_decoded_text[accent_text_pos + dem1][2:]
                            vietnamese_accent_text_position = accent_text_pos + dem1
                            vietnamese_decoded_text[accent_text_pos + dem1] = vietnamese_accent
                            vietnamese_decoded_text.insert(accent_text_pos + dem1 + 1, vietnamese_accent_text)
                            dem1 += 1
                            #print("vietnamese_decoded_text: ",vietnamese_decoded_text)
                    else:
                        vietnamese_decoded_text = vietnamese_decoded_text
                    print("dem1: ", dem1)
                    print("count: ", count)
                    print("vietnamese_decoded_text: ",vietnamese_decoded_text)   
            
                    for j in vietnamese_decoded_text:
                        dem += 1
                        
                        decoded_count = count_text[str(dem)]
                        decoded_text = decoded_count + braille_alphabet[j] 
                        print(decoded_text) 
                        braille.on(decoded_text,1.5)
                        if j == " ":
                            tempcount = vietnamese_decoded_text.index(j)
                            #time.sleep(0.5)
                            dem = 0
                            time.sleep(0.2)
                            braille.off(1)
                    
                   #print("hi: ",len(vietnamese_decoded_text) - (tempcount + 1))       
                    if dem >= (len(vietnamese_decoded_text) - (tempcount + 1)):
                        dem =0
                        time.sleep(3)
                        braille.off(1)
                        vietnamese_decoded_text = []
                        accent_text_position = []
                        dem1 = 0
                        print("dem1..", dem1)
                        
                        
                elif flag == 0:                                                                  #AGAIN
                    if key == 'AGAIN':
                        pre_text = text
                        
                        for i in text:
                            try:
                                vietnamese_decoded_text.append(vietnamese_decode[i])
                                temp = count 
                                accent_text_position.append(temp)
                                demcodau += 1  
                                
                            except:
                                vietnamese_decoded_text.append(i)
                                demkhongdau += 1
                            count += 1
                            #print("vietnamese_decoded_text: ",vietnamese_decoded_text)
                            flag = 0
                            COM_PORT = wb.com_port_check()
                            text_website = "None"
                        
                        
                        if demcodau == 0:
                            accent_text_position = None  
                                
                        """ if len(vietnamese_decoded_text) > 8:
                            del vietnamese_decoded_text[8:]  """     
                                
                        if accent_text_position != None:
                            for accent_text_pos in accent_text_position:
                                
                                vietnamese_accent = vietnamese_decoded_text[accent_text_pos + dem1][:2]
                                vietnamese_accent_text = vietnamese_decoded_text[accent_text_pos + dem1][2:]
                                vietnamese_accent_text_position = accent_text_pos + dem1
                                vietnamese_decoded_text[accent_text_pos + dem1] = vietnamese_accent
                                vietnamese_decoded_text.insert(accent_text_pos + dem1 + 1, vietnamese_accent_text)
                                dem1 += 1
                        else:
                            vietnamese_decoded_text = vietnamese_decoded_text
                        print("vietnamese_decoded_text: ",vietnamese_decoded_text)   
                
                        for j in vietnamese_decoded_text:
                            
                            
                            decoded_count = count_text[str(dem)]
                            decoded_text = decoded_count + braille_alphabet[j] 
                            print(decoded_text) 
                            braille.on(decoded_text,1)
                            if j == " ":
                                tempcount = vietnamese_decoded_text.index(j)
                                #time.sleep(0.5)
                                dem = 0
                                time.sleep(0.2)
                                braille.off(1)
                                
                        
                    #print("hi: ",len(vietnamese_decoded_text) - (tempcount + 1))       
                        if dem >= (len(vietnamese_decoded_text) - (tempcount + 1)):
                            dem = 0 
                            time.sleep(1.3)
                            braille.off(1)
                            vietnamese_decoded_text = []
                            accent_text_position = []
                            dem1 = 0
                    else:
                        print("No event")
            
                        
    else:
        print("disconnect")
        time.sleep(0.5)
        flag2 = 1