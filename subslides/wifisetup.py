﻿#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os,sys

import pi3d

sys.path.insert(1, os.path.join(sys.path[0], '..'))

import config
import core.graphics as graphics
import core.peripherals as peripherals
import core.iwlist as iwlist

wifinetworkstext = pi3d.FixedString(config.installpath + 'fonts/opensans.ttf', 'Please choose your WIFI-network' , font_size=42, shadow_radius=4,justify='L', background_color=(0,0,0,30), color= (255,255,255,255),camera=graphics.CAMERA, shader=graphics.SHADER, f_type='SMOOTH')
wifinetworkstext.sprite.position(0, 200, 1)
wifinetworks = None
selectednetwork = None

def inloop(x = 0, y = 0, touch_pressed = False, textchange = False,activity = False):
       global wifinetworks,selectednetwork
       wifinetworkstext.draw()
       if wifinetworks == None:
        actnetwork = 0
        wifinetworks = iwlist.scan()
        
        
        for network in wifinetworks:
         if network['essid'] == '': network['essid'] = 'hidden'
         wifinetworks[actnetwork]['string'] = pi3d.FixedString(config.installpath + 'fonts/opensans.ttf','SSID: '+(str)(network['essid']) + ', Enc:' + (str)(network['enc']) + '  Ch:' + (str)(network['ch']) , font_size=32,shadow_radius=4,justify='L', background_color=(0,0,0,30), color= (255,255,255,255),camera=graphics.CAMERA, shader=graphics.SHADER, f_type='SMOOTH')
         wifinetworks[actnetwork]['string'].sprite.position(0, (100 - (actnetwork*80)), 1)
         actnetwork += 1
       else:
         for network in wifinetworks:
            network['string'].draw()
         if peripherals.touch_pressed:
           peripherals.touch_pressed = False
           activity = True
           selectednetwork = abs((int)((peripherals.lasty - 100)/80))
           if -1 <  selectednetwork  <  len(wifinetworks):
              peripherals.eg_object.usertextshow = 'Please enter WIFI password.'
              peripherals.eg_object.usertext = ''
              config.subslide = 'wifikeyboard'

 





         
       return activity



















