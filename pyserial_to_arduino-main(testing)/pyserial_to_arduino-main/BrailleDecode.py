from AutoOpenWeb import website
import serial.tools.list_ports
import serial
import time

wb = website()

class braille_process():
    def __init__(self, COM_PORT, BAUD_RATE):
        self.port = COM_PORT
        self.baud_rate = BAUD_RATE
        self.port = wb.com_port_check()

        if self.port != "None":
            try:
                self.serialCom = serial.Serial(self.port, self.baud_rate)
                self.serialCom.timeout = 1
                #print(self.serialCom.readline().decode())
            except:
                print("Init COM error")
                self.port = wb.com_port_check()

    def alphabet(self):
        self.braille_decode = { 'a' : '1',    'ă' : '345',  'â' : '16',  'b' : '12',  'c' : '14',   'd' : '145',  'đ' : '2346', 'e' : '15',  'ê' : '126',
                                'g' : '1245', 'h' : '125',  'i' : '24',  'j' : '245', 'k' : '13',   'l' : '123',  'm' : '134',
                                'n' : '1345', 'o' : '135',  'ô' : '1456','ơ' : '246', 'p' : '1234', 'q' : '12345','r' : '1235', 's' : '234', 't' : '2345',
                                'u' : '136',  'ư' : '1256', 'v' : '1236','x' : '1346', 'y' : '13456', ' ':'0','':'0',
                                'sa': '35',  'hu' : '56',  'ho' : '26', 'ng' : '36', 'na' : '6'
                                }
        return self.braille_decode
    
    def count_Encode(self):
        self.count_encode = {'1' : 'k', '2' : 'l', '3' : 'm', '4' : 'n', '5' : 'o', '6' : 'p', '7' : 'q', '8' : 'r'}
        return self.count_encode
    
    def vietnamese_Encode(self):
        self.vietnamese_encoding = {
                                    'à' : 'hua', 'á' : 'saa', 'ả' : 'hoa', 'ã' : 'nga', 'ạ' : 'naa',
                                    'ằ' : 'huă', 'ắ' : 'saă', 'ẳ' : 'hoă', 'ẵ' : 'ngă', 'ặ' : 'naă',
                                    'ầ' : 'huâ', 'ấ' : 'saâ', 'ẩ' : 'hoâ', 'ẫ' : 'ngâ', 'ậ' : 'naâ',
                                    'è' : 'hue', 'é' : 'sae', 'ẻ' : 'hoe', 'ẽ' : 'nge', 'ẹ' : 'nae',
                                    'ề' : 'huê', 'ế' : 'saê', 'ể' : 'hoê', 'ễ' : 'ngê', 'ệ' : 'naê',
                                    'ì' : 'hui', 'í' : 'sai', 'ỉ' : 'hoi', 'ĩ' : 'ngi', 'ị' : 'nai',
                                    'ò' : 'huo', 'ó' : 'sao', 'ỏ' : 'hoo', 'õ' : 'ngo', 'ọ' : 'nao',
                                    'ồ' : 'huô', 'ố' : 'saô', 'ổ' : 'hoô', 'ỗ' : 'ngô', 'ộ' : 'naô',
                                    'ờ' : 'huơ', 'ớ' : 'saơ', 'ở' : 'hoơ', 'ỡ' : 'ngơ', 'ợ' : 'naơ',
                                    'ù' : 'huu', 'ú' : 'sau', 'ủ' : 'hou', 'ũ' : 'ngu', 'ụ' : 'nau',
                                    'ừ' : 'huư', 'ứ' : 'saư', 'ử' : 'hoư', 'ữ' : 'ngư', 'ự' : 'naư',
                                    'ỳ' : 'huy', 'ý' : 'say', 'ỷ' : 'hoy', 'ỹ' : 'ngy', 'ỵ' : 'nay' }
        return self.vietnamese_encoding
    

    def on(self, decoded_text, timeOn):
        if self.serialCom != "None":
            try:
                self.serialCom.write(decoded_text.encode())
                time.sleep(timeOn)
                #print("Read data for on()")
                print(self.serialCom.readline().decode())
                time.sleep(int(timeOn))
            except:
                print("on func COM_PORT error")
                self.port = wb.com_port_check()
    
    def off(self, timeOff):
        self.status = "off"
        if self.serialCom != "None":
            try:
                self.serialCom.write(self.status.encode())
                time.sleep(int(timeOff))
                #print("Read data for off()")
                """ print(self.serialCom.readline().decode())
                time.sleep(int(timeOff)) """
            except:
                print("off func COM_PORT error")
                self.port = wb.com_port_check()
        
    def keypad(self): 
        if self.serialCom != "None":
            try:
                self.key = self.serialCom.readline().strip().decode("utf-8")
                return self.key
            except:
                print("keypad func COM_PORT error")
                self.port = wb.com_port_check()

"""
braille = braille_process("COM4", 115200)
COM_PORT = wb.com_port_check()
while COM_PORT != "None":
    key = braille.keypad()
    if key:
        print(key)"""