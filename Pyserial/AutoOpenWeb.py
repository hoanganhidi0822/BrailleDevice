import time
import serial.tools.list_ports
import winsound
import webbrowser

class website():
    def __init__(self):
        self.url = "https://www.facebook.com/"
        self.arduino_port = "None"
        self.flag = 1
    
    def open(self):
        winsound.Beep(1000, 200)
        time.sleep(0.1)
        winsound.Beep(1000, 200)
        webbrowser.open(self.url)

    def open_once_time(self):
        ports = list(serial.tools.list_ports.comports())
        if ports == []:
            self.arduino_port = "None"

        else:
            for port in ports:
                self.arduino_port = port.device
        
        if self.arduino_port != "None":
            if self.flag == 1:
                time.sleep(1)
                self.open()
                time.sleep(1)
                self.flag = 0
                print("Open ", self.url)
            else:
                pass
        else:
            self.flag = 1

        print("Port: {}, Web status: {}".format(self.arduino_port, self.flag))
        time.sleep(1)
    
    def com_port_check(self):
        ports = list(serial.tools.list_ports.comports())
        if ports == []:
            self.arduino_port = "None"

        else:
            for port in ports:
                self.arduino_port = port.device
        
        return self.arduino_port