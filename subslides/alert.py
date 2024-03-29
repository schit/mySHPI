#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os,sys
import pi3d

sys.path.insert(1, os.path.join(sys.path[0], '..'))

import core.peripherals as peripherals
import config
import core.graphics as graphics



str1 = pi3d.FixedString(config.installpath + 'fonts/opensans.ttf', 'ALERT!', font_size=72, color = (255,0,0,255),background_color=(0,0,0,0),camera=graphics.CAMERA, shader=graphics.SHADER)
str1.sprite.position(0, 0, 0.1)



def inloop(textchange = False,activity = False):

    str1.draw()
    
    if  peripherals.touch_pressed:
      peripherals.touch_pressed = False
      config.subslide = None
      peripherals.eg_object.alert = 0
      peripherals.alert(0)
    return activity
