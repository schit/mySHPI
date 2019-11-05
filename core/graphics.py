#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pi3d
import math
import os,sys

sys.path.insert(1, os.path.join(sys.path[0], '..'))
import config


#mytext = 'ß()1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZüöäÜÖÄ,.%:° -'
mytext = '°abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_+=~`[]{}|\:;"\'<>,.?/ üöäÜÖÄß'

additional = [chr(0xE000), #arrow
              chr(0xE001), #circle
              chr(0xE002), #cloud
              chr(0xE003), #raindrop
              chr(0xE004), #fire
              chr(0xE005), #house
              chr(0xE006), #filledcircle
              #chr(0xE007), #raining
              #chr(0xE008), #timer
              chr(0xE009), #clock
              #chr(0xE00A), #eye
              chr(0xE00B), #gauge
              chr(0xE00C), #sun
              #chr(0xE00D), #cloudsun
              chr(0xE00E), #lightoff
              chr(0xE00F), #lighton
              chr(0xE010), #settings
              #chr(0xE011), #heart
              chr(0xE012), #book
              #chr(0xE013), #child
              #chr(0xE014), #alarmclock
              #chr(0xE015), #presence
              chr(0xE016), #wifi
              #chr(0xE017), #mic
              #chr(0xE018), #bluetooth
              #chr(0xE019), #web
              #chr(0xE01A), #speechbubble
              #chr(0xE01B), #ampere
              chr(0xE01C), #motion
              #chr(0xE01D), #electric
              #chr(0xE01E), #close
              #chr(0xE01F), #leaf
              #chr(0xE020), #socket
              chr(0xE021), #temp
              #chr(0xE022), #tesla
              #chr(0xE023), #raspi
              #chr(0xE024), #privacy
              #chr(0xE025), #circle2
              #chr(0xE026), #bell
              #chr(0xE027), #nobell
              #chr(0xE028), #moon
              chr(0xE029), #freeze
              #chr(0xE02A), #whatsapp
              #chr(0xE02B), #touch
              #chr(0xE02C), #settings2
              #chr(0xE02D), #storm
              chr(0xE035), #shutter
              #chr(0xE034), #doublearrow
              #chr(0xE033), #usb
              #chr(0xE032), #magnet
              chr(0xE031), #phone
              chr(0xE03F), #
              chr(0xE036),
              #chr(0xE030), #compass
              #chr(0xE02E), #trash
              chr(0xE02F), #cam
              chr(0xE040), #wind
              chr(0xE041), #sunset
              chr(0xE042)] #sunrise
              
              
              
DISPLAY = pi3d.Display.create(layer=0,w=800, h=480,background=(0.0, 0.0, 0.0, 1.0),frames_per_second=60, tk=False) #, samples=4)
SHADER = pi3d.Shader("uv_flat")
CAMERA = pi3d.Camera(is_3d=False)
MATSH = pi3d.Shader("mat_flat")

def tex_load(fname):
  slide = pi3d.ImageSprite(fname,shader=SHADER,camera=CAMERA,w=800,h=480,z=4)
  slide.set_alpha(0)
  return slide

def slider_change(shape_obj, offset_val):
  abs_offset = abs(offset_val)
  if abs_offset > 0: # only do something if offset
    if abs_offset < 6: # needs to be > min move distance
      offset_val = 0
    else:
      speed = min(20, max(5, abs_offset * 0.1))
      offset_val -= math.copysign(speed, offset_val)
    shape_obj.positionX(-offset_val)
  return offset_val # rather than using a global or passing ref to change


pointFont = pi3d.Font(config.installpath + "fonts/opensans.ttf", shadow=(0, 0, 0, 255), shadow_radius=5, grid_size=12,
                       codepoints=mytext, add_codepoints=additional)
pointFontbig = pi3d.Font(config.installpath + "fonts/opensans.ttf", shadow=(0, 0, 0, 255), shadow_radius=4, grid_size=5, codepoints='0123456789:' +chr(0xE00E) + chr(0xe00f))
