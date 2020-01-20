#!/usr/bin/env python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(3,GPIO.OUT)
time.sleep(1)

GPIO.output(3,True)
time.sleep(0.5)

GPIO.output(3,False)
time.sleep(0.5)


GPIO.cleanup()