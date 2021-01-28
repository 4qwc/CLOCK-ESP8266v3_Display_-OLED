from machine import Pin, I2C
import ssd1306
from time import sleep

# ESP8266 Pin assignment
i2c = I2C(-1, scl=Pin(5), sda=Pin(4))

oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)


H = 0
M = 0
S = 0
while (True):
     
    S <= 0
    S +=1
    sleep(1)
    oled.fill(0)# clear oled
    
    if S == 59:  
        S=0
        M+=1
        
        if M==59:
            M=0
            H+=1
            if H==23:
                H=0
            
    print('Time: ',H,M,S)
    
    ss = S
    SEC = str(ss)
    
    mm = M
    MIN = str(mm)
    
    hh = H
    HOR = str(hh)
    
    oled.text('TIME: '+ HOR +':'+ MIN +':'+ SEC, 0, 45)
    
    oled.text('PROJECT HS4QWC', 0, 0)
    oled.text('DATE TIME', 10, 25)
    oled.show()
#oled.fill(0)# clear oled
#oled.fill(1)# 1 = เติมสีหน้าจอทั้งหมด
