import time
import serial.tools.list_ports
import winsound
import webbrowser

class website():
    def __init__(self):
        self.url = "https://localhost:3000/Fontend_KHKT/"
        self.arduino_port = "None"
        self.flag = 1
        self.PORT_DRIVER = ["Arduino Uno", "USB-SERIAL CH340"]
    
    def open(self):
        time.sleep(1)
        winsound.Beep(1000, 200)
        time.sleep(0.1)
        winsound.Beep(1000, 200)
        webbrowser.open(self.url)
        time.sleep(1)

    def open_once_time(self):
        self.arduino_port = self.com_port_check()
        
        if self.arduino_port != "None":
            if self.flag == 1:                
                self.open()
                self.flag = 0
                print("Open:", self.url)
            else:
                pass
        else:
            self.flag = 1

        #print("Port: {}, Web status: {}".format(self.arduino_port, self.flag))
    
    def com_port_check(self):
        ports = list(serial.tools.list_ports.comports())
        
        if ports == []:
            self.arduino_port = "None"
        else:
            for port in ports:
                for driver in self.PORT_DRIVER:
                    if driver in port.description:
                        self.arduino_port = port.device
                    elif driver not in self.PORT_DRIVER:
                        print("Braille device not found")
        
        #print(self.arduino_port)
        return self.arduino_port

#print(website().com_port_check())
