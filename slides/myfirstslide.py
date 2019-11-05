#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pi3d
import sys,os

sys.path.insert(1, os.path.join(sys.path[0], '..'))

import config
import core.graphics as graphics
import core.peripherals as peripherals

try:
   import mqttclient
except:
   import core.mqttclient as mqttclient



text2 = pi3d.PointText(graphics.pointFontbig, graphics.CAMERA, max_chars=35, point_size=256) #slider2 Time & shutter


if config.shutterup or config.shutterdown:
  uhrzeit_block = pi3d.TextBlock(-280, 100, 0.1, 0.0, 15, data_obj=peripherals.eg_object,attr="uhrzeit", text_format= "{:s}", size=0.99, spacing="F", space=0.05, colour=(1.0, 1.0, 1.0, 1.0))
  text2.add_text_block(uhrzeit_block)
  kugelswitch = pi3d.TextBlock(-100, -100, 0.1, 0.0, 15, text_format= chr(0xE001),size=0.99, spacing="F", space=0.05, colour=(1.0, 1.0, 1.0, 1.0))
  text2.add_text_block(kugelswitch)
  shutterDown = pi3d.TextBlock(300, -100, 0.1, 0.0, 1, text_format= chr(0xE021),size=0.69, spacing="C", space=0.6, colour=(1, 1, 1, 0.8))
  text2.add_text_block(shutterDown)
  shutterUp = pi3d.TextBlock(-300, -100, 0.1, 180.0, 1, text_format= chr(0xE001),size=0.69, spacing="C", space=0.6, colour=(1, 1, 1, 0.8))
  text2.add_text_block(shutterUp)
else:
  uhrzeit_block = pi3d.TextBlock(-280, 0, 0.1, 0.0, 15, data_obj=peripherals.eg_object,attr="uhrzeit", text_format= "{:s}", size=0.99, spacing="F", space=0.05, colour=(1.0, 1.0, 1.0, 1.0))
  text2.add_text_block(uhrzeit_block)      
        
        
def inloop(textchange = False,activity = False, offset = 0):
      
     if textchange:
       text2.regen()
     if shutterUp.y != -100 and shutterUp.colouring.colour[2] == 1:
        shutterUp.set_position(y=-100)
     if (shutterUp.colouring.colour[2] == 0):
        if shutterUp.y > 0:
          shutterUp.set_position(y=-100)
        shutterUp.set_position(y=(shutterUp.y+2))
        activity = True



     if shutterDown.y != -100 and shutterDown.colouring.colour[2] == 1:
        shutterDown.set_position(y=-100)
     if (shutterDown.colouring.colour[2] == 0):
        if shutterDown.y < -99:
          shutterDown.set_position(y=0)
        shutterDown.set_position(y=(shutterDown.y-2))
        activity = True
       
 

     if peripherals.touch_pressed:
      peripherals.touch_pressed = False     
      if peripherals.clicked(shutterUp.x,shutterUp.y):
        peripherals.controlrelays(config.shutterdown, 0)
        mqttclient.publish("scheinwerfer", '0')
        peripherals.controlrelays(config.shutterup, 1)
        shutterUp.colouring.set_colour([0,1,0])
        shutterDown.colouring.set_colour([1,1,1])


      elif peripherals.clicked(shutterDown.x,shutterDown.y):
        peripherals.controlrelays(config.shutterup, 0)
        peripherals.controlrelays(config.shutterdown, 1)
        mqttclient.publish("scheinwerfer", '1')
        shutterUp.colouring.set_colour([1,1,1])
        shutterDown.colouring.set_colour([0,1,0])


      else:
        peripherals.controlrelays(config.shutterdown, 0)
        peripherals.controlrelays(config.shutterup, 0)
        shutterUp.colouring.set_colour([1,1,1])
        shutterDown.colouring.set_colour([1,1,1])
        
        
     if offset != 0:
         offset = graphics.slider_change(text2.text, offset)
         if offset == 0:
             text2.regen()
     text2.draw()   
         
     return activity,offset



