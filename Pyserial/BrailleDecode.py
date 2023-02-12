import serial.tools.list_ports
import serial
import time

class braille_process():
    def __init__(self, COM_PORT, BAUD_RATE):
        self.serialCom = COM_PORT
        self.braille_decode = { 'a':'1','ă':'345','â':'16', 'b':'12', 'c':'14', 'd':'145','đ':'2346', 'e':'15','ê':'126',
                                'g':'1245', 'h':'125', 'i':'24', 'j':'245', 'k':'13', 'l':'123', 'm':'134',
                                'n':'1345', 'o':'135','ô':'1456', 'ơ':'236', 'p':'1234', 'q':'12345', 'r':'1235', 's':'234', 't':'2345',
                                'u':'136','ư':'1256', 'v':'1236', 'w':'2456', 'x':'1346', 'y':'13456', ' ': '0',
                                'sa':'35','hu':'56','ho':'26','ng':'36','na':'6'
                                }
        self.count_encode = {'1':'k','2':'l','3':'m','4':'n','5':'o','6':'p','7':'q','8':'r'}
        
        self.vietnamese_encoding = {
                                    'à': 'hua', 'á': 'saa', 'ả': 'hoa', 'ã': 'nga', 'ạ': 'naa',
                                    'ă': 'ă', 'ằ': 'huă', 'ắ': 'saă', 'ẳ': 'hoă', 'ẵ': 'ngă', 'ặ': 'naă',
                                    'â': 'a', 'ầ': 'huâ', 'ấ': 'sâ', 'ẩ': 'hoâ', 'ẫ': 'ngâ', 'ậ': 'naâ',
                                    'đ': 'đ',
                                    'è': 'hue', 'é': 'sae', 'ẻ': 'hoe', 'ẽ': 'nge', 'ẹ': 'nae',
                                    'ê': 'ê', 'ề': 'ê', 'ế': 'ê', 'ể': 'ê', 'ễ': 'ê', 'ệ': 'ê',
                                    'ì': 'i', 'í': 'i', 'ỉ': 'i', 'ĩ': 'i', 'ị': 'i',
                                    'ò': 'o', 'ó': 'o', 'ỏ': 'o', 'õ': 'o', 'ọ': 'o',
                                    'ô': 'ô', 'ồ': 'ô', 'ố': 'ô', 'ổ': 'ô', 'ỗ': 'ô', 'ộ': 'ô',
                                    'ơ': 'ơ', 'ờ': 'ơ', 'ớ': 'ơ', 'ở': 'ơ', 'ỡ': 'ơ', 'ợ': 'ơ',
                                    'ù': 'u', 'ú': 'u', 'ủ': 'u', 'ũ': 'u', 'ụ': 'u',
                                    'ư': 'ư', 'ừ': 'ư', 'ứ': 'ư', 'ử': 'ư', 'ữ': 'ư', 'ự': 'ư',
                                    'ỳ': 'y', 'ý': 'y', 'ỷ': 'y', 'ỹ': 'y', 'ỵ': 'y'
}
        if self.serialCom != "None":
            self.serialCom = serial.Serial(COM_PORT, BAUD_RATE)
            self.serialCom.timeout = 1

    def alphabet(self):
        return self.braille_decode
    def count_Encode(self):
        return self.count_encode
    def vietnamese_Encode(self):
        return self.vietnamese_encoding

    def on(self, decoded_text, timeOn):
        if self.serialCom != "None":
            self.serialCom.write(decoded_text.encode())
            
            time.sleep(timeOn)
            #print("Read data for on()")
            print(self.serialCom.readline().decode())
            time.sleep(int(timeOn))
    
    def off(self, timeOff):
        if self.serialCom != "None":
            self.serialCom.write(' '.encode())
            time.sleep(1)
            #print("Read data for off()")
            print(self.serialCom.readline().decode())
            time.sleep(int(timeOff))
        
    def keypad(self): 
        if self.serialCom != "None":
            self.key = self.serialCom.readline().decode()
            return self.key