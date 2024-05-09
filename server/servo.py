#!/usr/bin/env python3
# File name   : servo.py
# Description : Control Servos
# Author      : William
# Date        : 2019/02/23
from __future__ import division
import time
import RPi.GPIO as GPIO
import sys
import Adafruit_PCA9685

'''
change this form 1 to 0 to reverse servos
'''
pwm0_direction = 1
pwm1_direction = 1
pwm2_direction = 1
pwm3_direction = 1
pwm6_direction = 1
pwm7_direction = 1
pwm8_direction = 1
pwm9_direction = 1
pwm4_direction = 1

pwm = Adafruit_PCA9685.PCA9685()
pwm.set_pwm_freq(50)

# Left front shoulder
pwm0_init = 320
pwm0_min  = 150
pwm0_max  = 450
pwm0_pos  = pwm0_init

# Left front leg
pwm1_init = 400
pwm1_min  = 120
pwm1_max  = 480
pwm1_pos  = pwm1_init
pwm1_up = 270

# Left back shoulder
pwm2_init = 300
pwm2_min  = 150
pwm2_max  = 450
pwm2_pos  = pwm2_init

# Left back leg
pwm3_init = 200
pwm3_min  = 120
pwm3_max  = 450
pwm3_pos  = pwm3_init
pwm3_up = 330

# Right front shoulder
pwm8_init = 270
pwm8_min = 150
pwm8_max = 450
pwm8_pos = pwm8_init

# Right front leg
pwm9_init = 200
pwm9_min = 120
pwm9_max = 480
pwm9_pos = pwm9_init
pwm9_up = 330

# Right back shoulder
pwm6_init = 300
pwm6_min = 120
pwm6_max = 420
pwm6_pos = pwm6_init

# Right back leg
pwm7_init = 400
pwm7_min = 120
pwm7_max = 500
pwm7_pos = pwm7_init
pwm7_up = 250

# Tail
pwm4_pos = 300

org_pos = 300

motor_step = 10

def ctrl_range(raw, max_genout, min_genout):
	if raw > max_genout:
		raw_output = max_genout
	elif raw < min_genout:
		raw_output = min_genout
	else:
		raw_output = raw
	return int(raw_output)

def camera_ang(direction, ang):
	global org_pos
	if ang == 'no':
		ang = 50
	if look_direction:
		if direction == 'lookdown':
			org_pos+=ang
			org_pos = ctrl_range(org_pos, look_max, look_min)
		elif direction == 'lookup':
			org_pos-=ang
			org_pos = ctrl_range(org_pos, look_max, look_min)
		elif direction == 'home':
			org_pos = 300
	else:
		if direction == 'lookdown':
			org_pos-=ang
			org_pos = ctrl_range(org_pos, look_max, look_min)
		elif direction == 'lookup':
			org_pos+=ang
			org_pos = ctrl_range(org_pos, look_max, look_min)
		elif direction == 'home':
			org_pos = 300	

	pwm.set_all_pwm(13,org_pos)

def lookleft(speed):
	global pwm0_pos
	if pwm0_direction:
		pwm0_pos += speed
		pwm0_pos = ctrl_range(pwm0_pos, pwm0_max, pwm0_min)
		pwm.set_pwm(12, 0, pwm0_pos)
	else:
		pwm0_pos -= speed
		pwm0_pos = ctrl_range(pwm0_pos, pwm0_max, pwm0_min)
		pwm.set_pwm(12, 0, pwm0_pos)


def lookright(speed):
	global pwm0_pos
	if pwm0_direction:
		pwm0_pos -= speed
		pwm0_pos = ctrl_range(pwm0_pos, pwm0_max, pwm0_min)
		pwm.set_pwm(12, 0, pwm0_pos)
	else:
		pwm0_pos += speed
		pwm0_pos = ctrl_range(pwm0_pos, pwm0_max, pwm0_min)
		pwm.set_pwm(12, 0, pwm0_pos)


def up(speed):
	global pwm1_pos
	if pwm1_direction:
		pwm1_pos -= speed
		pwm1_pos = ctrl_range(pwm1_pos, pwm1_max, pwm1_min)
		pwm.set_pwm(13, 0, pwm1_pos)
	else:
		pwm1_pos += speed
		pwm1_pos = ctrl_range(pwm1_pos, pwm1_max, pwm1_min)
		pwm.set_pwm(13, 0, pwm1_pos)
	#print(pwm1_pos)

def down(speed):
	global pwm1_pos
	if pwm1_direction:
		pwm1_pos += speed
		pwm1_pos = ctrl_range(pwm1_pos, pwm1_max, pwm1_min)
		pwm.set_pwm(13, 0, pwm1_pos)
	else:
		pwm1_pos -= speed
		pwm1_pos = ctrl_range(pwm1_pos, pwm1_max, pwm1_min)
		pwm.set_pwm(13, 0, pwm1_pos)
	#print(pwm1_pos)

def lookup(speed):
	global pwm2_pos
	if pwm2_direction:
		pwm2_pos -= speed
		pwm2_pos = ctrl_range(pwm2_pos, pwm2_max, pwm2_min)
		pwm.set_pwm(13, 0, pwm2_pos)
	else:
		pwm2_pos += speed
		pwm2_pos = ctrl_range(pwm2_pos, pwm2_max, pwm2_min)
		pwm.set_pwm(13, 0, pwm2_pos)


def lookdown(speed):
	global pwm2_pos
	if pwm2_direction:
		pwm2_pos += speed
		pwm2_pos = ctrl_range(pwm2_pos, pwm2_max, pwm2_min)
		pwm.set_pwm(13, 0, pwm2_pos)
	else:
		pwm2_pos -= speed
		pwm2_pos = ctrl_range(pwm2_pos, pwm2_max, pwm2_min)
		pwm.set_pwm(13, 0, pwm2_pos)


def grab(speed):
	global pwm3_pos
	if pwm3_direction:
		pwm3_pos -= speed
		pwm3_pos = ctrl_range(pwm3_pos, pwm3_max, pwm3_min)
		pwm.set_pwm(3, 0, pwm3_pos)
	else:
		pwm3_pos += speed
		pwm3_pos = ctrl_range(pwm3_pos, pwm3_max, pwm3_min)
		pwm.set_pwm(3, 0, pwm3_pos)
	print(pwm3_pos)


def loose(speed):
	global pwm3_pos
	if pwm3_direction:
		pwm3_pos += speed
		pwm3_pos = ctrl_range(pwm3_pos, pwm3_max, pwm3_min)
		pwm.set_pwm(3, 0, pwm3_pos)
	else:
		pwm3_pos -= speed
		pwm3_pos = ctrl_range(pwm3_pos, pwm3_max, pwm3_min)
		pwm.set_pwm(3, 0, pwm3_pos)
	print(pwm3_pos)


def servo_init():
	pwm.set_pwm(0, 0, pwm0_pos)
	pwm.set_pwm(1, 0, pwm1_pos)
	pwm.set_pwm(2, 0, pwm2_pos)
	pwm.set_pwm(3, 0, pwm3_pos)
	pwm.set_pwm(8, 0, pwm8_pos)
	pwm.set_pwm(9, 0, pwm9_pos)
	pwm.set_pwm(6, 0, pwm6_pos)
	pwm.set_pwm(7, 0, pwm7_pos)
	pwm.set_pwm(4, 0, pwm4_pos)


def clean_all():
	global pwm
	pwm = Adafruit_PCA9685.PCA9685()
	pwm.set_pwm_freq(50)
	pwm.set_all_pwm(0, 0)


def ahead():
	global pwm0_pos, pwm1_pos
	pwm.set_pwm(0, 0, pwm0_init)
	pwm.set_pwm(1, 0, (pwm1_max-20))
	pwm0_pos = pwm0_init
	pwm1_pos = pwm1_max-20


def get_direction():
	return (pwm0_pos - pwm0_init)

def stand_up():
  global pwm1_pos, pwm3_pos, pwm7_pos, pwm9_pos
  pwm.set_pwm(1, 0, pwm1_up)
  pwm.set_pwm(3, 0, pwm3_up)
  pwm.set_pwm(7, 0, pwm7_up)
  pwm.set_pwm(9, 0, pwm9_up)
  pwm1_pos = pwm1_up
  pwm3_pos = pwm3_up
  pwm7_pos = pwm7_up
  pwm9_pos = pwm9_up

def move_motor(motor, pos_start, pos_end):
  pos = pos_start
  direction = 0
  if pos_start > pos_end:
    direction = 1
  if direction == 0:
    while pos < pos_end:
      pwm.set_pwm(motor, 0, pos)
      pos = pos + motor_step
      time.sleep(0.1)
  else:
    while pos > pos_end:
      pwm.set_pwm(motor, 0, pos)
      pos = pos - motor_step
      time.sleep(0.1)
  return pos

def left_front_leg(shoulder_pos_start, shoulder_pos_end, leg_pos_start, leg_pos_end):
  shoulder_pos = shoulder_pos_start
  leg_pos = leg_pos_start
  shoulder_dir = 0
  leg_dir = 0
  if shoulder_pos_start > shoulder_pos_end:
    shoulder_dir = 1
  if leg_pos_start > leg_pos_end:
    leg_dir = 1
  if shoulder_dir == 0:
    while shoulder_pos < shoulder_pos_end:
      pwm.set_pwm(0, 0, shoulder_pos)
      pwm.set_pwm(1, 0, leg_pos)
      shoulder_pos = shoulder_pos + motor_step
      if leg_dir == 0:
        leg_pos = leg_pos + motor_step
      else:
        leg_pos = leg_pos - motor_step
      time.sleep(0.05)
  else:
    while shoulder_pos > shoulder_pos_end:
      pwm.set_pwm(0, 0, shoulder_pos)
      pwm.set_pwm(1, 0, leg_pos)
      shoulder_pos = shoulder_pos - motor_step
      if leg_dir == 0:
        leg_pos = leg_pos + motor_step
      else:
        leg_pos = leg_pos - motor_step
      time.sleep(0.05)
  if leg_dir == 0:
    while leg_pos < leg_pos_end:
      pwm.set_pwm(1, 0, leg_pos)
      leg_pos = leg_pos + motor_step
  else:
    while leg_pos > leg_pos_end:
      pwm.set_pwm(1, 0, leg_pos)
      leg_pos = leg_pos - motor_step

def right_front_leg(shoulder_pos_start, shoulder_pos_end, leg_pos_start, leg_pos_end):
  shoulder_pos = shoulder_pos_start
  leg_pos = leg_pos_start
  shoulder_dir = 0
  leg_dir = 0
  if shoulder_pos_start > shoulder_pos_end:
    shoulder_dir = 1
  if leg_pos_start > leg_pos_end:
    leg_dir = 1
  if shoulder_dir == 0:
    while shoulder_pos < shoulder_pos_end:
      pwm.set_pwm(8, 0, shoulder_pos)
      pwm.set_pwm(9, 0, leg_pos)
      shoulder_pos = shoulder_pos + motor_step
      if leg_dir == 0:
        leg_pos = leg_pos + motor_step
      else:
        leg_pos = leg_pos - motor_step
      time.sleep(0.05)
  else:
    while shoulder_pos > shoulder_pos_end:
      pwm.set_pwm(8, 0, shoulder_pos)
      pwm.set_pwm(9, 0, leg_pos)
      shoulder_pos = shoulder_pos - motor_step
      if leg_dir == 0:
        leg_pos = leg_pos + motor_step
      else:
        leg_pos = leg_pos - motor_step
      time.sleep(0.05)		
  if leg_dir == 0:
    while leg_pos < leg_pos_end:
      pwm.set_pwm(9, 0, leg_pos)
      leg_pos = leg_pos + motor_step
  else:
    while leg_pos > leg_pos_end:
      pwm.set_pwm(9, 0, leg_pos)
      leg_pos = leg_pos - motor_step

def left_back_leg(shoulder_pos_start, shoulder_pos_end, leg_pos_start, leg_pos_end):
  shoulder_pos = shoulder_pos_start
  leg_pos = leg_pos_start
  shoulder_dir = 0
  leg_dir = 0
  if shoulder_pos_start > shoulder_pos_end:
    shoulder_dir = 1
  if leg_pos_start > leg_pos_end:
    leg_dir = 1
  if shoulder_dir == 0:
    while shoulder_pos < shoulder_pos_end:
      pwm.set_pwm(2, 0, shoulder_pos)
      pwm.set_pwm(3, 0, leg_pos)
      shoulder_pos = shoulder_pos + motor_step
      if leg_dir == 0:
        leg_pos = leg_pos + motor_step
      else:
        leg_pos = leg_pos - motor_step
      time.sleep(0.05)
  else:
    while shoulder_pos > shoulder_pos_end:
      pwm.set_pwm(2, 0, shoulder_pos)
      pwm.set_pwm(3, 0, leg_pos)
      shoulder_pos = shoulder_pos - motor_step
      if leg_dir == 0:
        leg_pos = leg_pos + motor_step
      else:
        leg_pos = leg_pos - motor_step
      time.sleep(0.05)		
  if leg_dir == 0:
    while leg_pos < leg_pos_end:
      pwm.set_pwm(3, 0, leg_pos)
      leg_pos = leg_pos + motor_step
  else:
    while leg_pos > leg_pos_end:
      pwm.set_pwm(3, 0, leg_pos)
      leg_pos = leg_pos - motor_step

def right_back_leg(shoulder_pos_start, shoulder_pos_end, leg_pos_start, leg_pos_end):
  shoulder_pos = shoulder_pos_start
  leg_pos = leg_pos_start
  shoulder_dir = 0
  leg_dir = 0
  if shoulder_pos_start > shoulder_pos_end:
    shoulder_dir = 1
  if leg_pos_start > leg_pos_end:
    leg_dir = 1
  if shoulder_dir == 0:
    while shoulder_pos < shoulder_pos_end:
      pwm.set_pwm(6, 0, shoulder_pos)
      pwm.set_pwm(7, 0, leg_pos)
      shoulder_pos = shoulder_pos + motor_step
      if leg_dir == 0:
        leg_pos = leg_pos + motor_step
      else:
        leg_pos = leg_pos - motor_step
      time.sleep(0.05)
  else:
    while shoulder_pos > shoulder_pos_end:
      pwm.set_pwm(6, 0, shoulder_pos)
      pwm.set_pwm(7, 0, leg_pos)
      shoulder_pos = shoulder_pos - motor_step
      if leg_dir == 0:
        leg_pos = leg_pos + motor_step
      else:
        leg_pos = leg_pos - motor_step
      time.sleep(0.05)		
  if leg_dir == 0:
    while leg_pos < leg_pos_end:
      pwm.set_pwm(7, 0, leg_pos)
      leg_pos = leg_pos + motor_step
  else:
    while leg_pos > leg_pos_end:
      pwm.set_pwm(7, 0, leg_pos)
      leg_pos = leg_pos - motor_step

def step_1():
  global pwm0_pos, pwm1_pos, pwm2_pos, pwm3_pos, pwm6_pos, pwm7_pos, pwm8_pos, pwm9_pos
  left_front_leg(pwm0_pos, 200, pwm1_pos, 120)
  pwm0_pos = 200
  pwm1_pos = 120
  # time.sleep(0.5)
  right_front_leg(pwm8_pos, 200, pwm9_pos, 250)
  pwm8_pos = 200
  pwm9_pos = 250
  # time.sleep(0.5)
  left_back_leg(pwm2_pos, 200, pwm3_pos, 320)
  pwm2_pos = 200
  pwm3_pos = 320
  # time.sleep(0.5)
  right_back_leg(pwm6_pos, 380, pwm7_pos, 320)
  pwm6_pos = 380
  pwm7_pos = 320
  # time.sleep(0.5)
  tail_2()


def step_2():
  global pwm0_pos, pwm1_pos, pwm2_pos, pwm3_pos, pwm6_pos, pwm7_pos, pwm8_pos, pwm9_pos
  left_front_leg(pwm0_pos, 380, pwm1_pos, 350)
  pwm0_pos = 380
  pwm1_pos = 350
  # time.sleep(0.5)
  right_front_leg(pwm8_pos, 350, pwm9_pos, 450)
  pwm8_pos = 350
  pwm9_pos = 450
  # time.sleep(0.5)
  left_back_leg(pwm2_pos, 400, pwm3_pos, 400)
  pwm2_pos = 400
  pwm3_pos = 400
  # time.sleep(0.5)
  right_back_leg(pwm6_pos, 200, pwm7_pos, 230)
  pwm6_pos = 200
  pwm7_pos = 230
  # time.sleep(0.5)
  tail_1()

def walk():
  for i in range(0, 4):
    step_1()
    step_2()

def tail_1():
  pwm.set_pwm(4, 0, 200)

def tail_2():
  pwm.set_pwm(4, 0, 400)

if __name__ == '__main__':
	servo_init()
	# while pwm_pos > pwm0_min:
	# 	pwm.set_pwm(0, 0, pwm_pos)
	# 	pwm_pos = pwm_pos - 5
	# 	time.sleep(0.1)
	time.sleep(1)
	stand_up()
	time.sleep(1)
	# pwm0_pos = pwm0_init
	# pwm1_pos = pwm1_up
	# pwm8_pos = pwm8_init
	# pwm9_pos = pwm9_up
	# for i in range(0, 4):
	# 	left_front_leg(pwm0_pos, 200, pwm1_pos, 120)
	# 	pwm0_pos = 200
	# 	pwm1_pos = 120
	# 	time.sleep(0.5)
	# 	right_front_leg(pwm8_pos, 200, pwm9_pos, 250)
	# 	pwm8_pos = 200
	# 	pwm9_pos = 250
	# 	time.sleep(0.5)
	# 	left_front_leg(pwm0_pos, 380, pwm1_pos, 350)
	# 	pwm0_pos = 380
	# 	pwm1_pos = 350
	# 	time.sleep(0.5)
	# 	right_front_leg(pwm8_pos, 350, pwm9_pos, 430)
	# 	pwm8_pos = 350
	# 	pwm9_pos = 430
	# 	time.sleep(0.5)
	
	walk()
