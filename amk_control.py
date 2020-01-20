#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Date:2019.11.04
가습기 제어 (릴레이) 
"""

from __future__ import print_function 

import time
import ex1_kwstest as kws
import ex2_getVoice2Text as gv2t
import ex4_getText2VoiceStream as tts
import MicrophoneStream as MS
import RPi.GPIO as GPIO
import Adafruit_DHT as dht

GPIO.setmode(GPIO.BOARD)
GPIO.setup(5,GPIO.OUT)
humidity, temperature = dht.read_retry(11, 12)


def ledControl(result):
    text = result
    if text.find("가습기 켜") >= 0:
        
        print("가습기가 켜집니다. ")
        time.sleep(1)
        GPIO.output(5,True)
        time.sleep(0.5)
        GPIO.output(5,False)
        time.sleep(0.5)
        return("가습기를 킵니다.   ")

    elif text.find("가습기 꺼") >= 0:
        print("가습기가 꺼집니다.   ")
        time.sleep(1)
        GPIO.output(5,True)
        time.sleep(0.5)
        GPIO.output(5,False)
        time.sleep(0.5)
        GPIO.output(5,True)
        time.sleep(0.5)
        GPIO.output(5,False)
        time.sleep(0.5)
        return("가습기를 끕니다.       ")
    
    if text.find("온도 알려줘") >= 0:
        print("현재 온도는 {} 도 입니다 ".format(temperature))
        return("현재 온도는 {} 도 입니다 ".format(temperature))
    
    elif text.find("습도 알려줘") >= 0:
        print("현재 습도는 {} 퍼센트 입니다 ".format(humidity))
        return("현재 습도는 {} 퍼센트 입니다 ".format(humidity))
    if text.find("여친 알려줘") >= 0:
        print("아직 세상에 존재하지 않아요. 힘내세요 무준님 곧 태어날 예정이라고 생각하니까라고 생각하지마세요 평생 없어요.    ")
        return("아직 세상에 존재하지 않아요. 힘내세요 무준님 곧 태어날 예정이라고 생각하니까라고 생각하지마세요 평생 없어요.    ")
    
    if text.find("전생 알려줘") >= 0:
        print("이것도 없어요    무준님   ")
        return(" 이것도 없어요    무준님   ")
    
    if text.find("환생 알려줘") >= 0:
        print("다행이 자웅동체에요    무준님   ")
        return("다행이 자웅동체에요     무준님   ")
    
    else:
        return("정확한 명령을 말해주세요  ")

def main():
	#Example7 KWS+STT

    KWSID = ['기가지니', '지니야', '친구야', '자기야']
    while 1:
        recog=kws.test(KWSID[2])
        if recog == 200:
            print('KWS Dectected ...\n Start STT...')
            text = gv2t.getVoice2Text()
            print('Recognized Text: '+ text)
            tts.getText2VoiceStream(ledControl(text), "result_TTS.wav")
            MS.play_file("result_TTS.wav")
            time.sleep(2)

        else:
            print('KWS Not Dectected ...')

if __name__ == '__main__':
    try:
        main()

    finally:
        GPIO.cleanup()
