import serial
import time

serialcomm = serial.Serial('COM4', 115200)
serialcomm.timeout = 1

text=input("Nhập chữ cái bất kì: ").lower().strip()

braille_decode={
'a':'1','b':'12','c':'14','d':'145','e':'15','f':'124',
'g':'1245','h':'125','i':'24','j':'245','k':'13','l':'123','m':'134',
'n':'1345','o':'135','p':'1234','q':'12345','r':'1235','s':'234','t':'2345',
'u':'136','v':'1236','w':'2456','x':'1346','y':'13456','z':'1356'
}
#decoded_text = braille_decode[text]
#print("Chữ sau giải mã là: ",decoded_text)

def textOn(decoded_text,timeOn):
    serialcomm.write(decoded_text.encode())
    print(serialcomm.readline().decode())
    time.sleep(int(timeOn))

def textOff(timeOff):
    serialcomm.write(' '.encode())
    print(serialcomm.readline().decode())
    time.sleep(int(timeOff))   
    
while True:
    for i in text:
        print(i)
        decoded_text = braille_decode[i] 
        textOn(decoded_text,1)
        textOff(1)
        
    break