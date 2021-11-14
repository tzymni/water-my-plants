#!/usr/bin/env python

import RPi.GPIO as GPIO
import time
import argparse

# relay channel
CHANNEL = 21

# time to wait after open relay
DELAY_TIME = 5

# GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(CHANNEL, GPIO.OUT)

def close_relay(pin):
    print("Relay closed")    
    GPIO.output(pin, GPIO.HIGH)  

def open_relay(pin):
    print("Relay open")
    GPIO.output(pin, GPIO.LOW)  

def parser():
    parser = argparse.ArgumentParser(description='Open relay for defined time in open_time argument.')
    parser.add_argument('--open_time', type=int,
                    help='Time of open relay in seconds.')
    parser.set_defaults(open_time=DELAY_TIME)
    args = parser.parse_args()
    return args

if __name__ == '__main__':
    try:    
        args = parser()
        print('Relay will be open for ' + str(args.open_time) + ' seconds')
        print('Relay will be open after ' + str(DELAY_TIME) +' seconds')
        time.sleep(DELAY_TIME)
        open_relay(CHANNEL)
        time.sleep(args.open_time)
        close_relay(CHANNEL)
        GPIO.cleanup()
    except KeyboardInterrupt:
        GPIO.cleanup()
