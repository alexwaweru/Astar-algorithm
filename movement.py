#!/usr/bin/env python3

import ev3dev.ev3 as ev3
import math

# Initialize left and right motors
left_motor = ev3.LargeMotor('outB')
right_motor = ev3.LargeMotor('outC')


'''This method takes in a distance in centimeters and causes the robot to move straight for that distance''''
def drive_straight(distance):
    
    # Measurements taken
    radius = 2.8
    pi = math.pi
    circumference = 2*pi*radius

    # Convert linear distance to motor turn angle
    angle = (distance*360)/circumference

    # To cause linear movement, turn both motors at the same speed at the given angle 
    left_motor.run_to_rel_pos(position_sp=angle, speed_sp=200 )
    right_motor.run_to_rel_pos(position_sp=angle, speed_sp=200)

    #Wait for the motors to complete the revolutions
    right_motor.wait_while('running')
    left_motor.wait_while('running')


'''This method takes in a turn angles and causes the robot to turn right at that angle''''
def turn_right(angle = 90):

    # Measurements taken
    width = 12.3 # Width of the robot
    wheel_radius = 2.8 

    # Circumference covered if a robot does a complete turn
    circumference = 2*(math.pi)*width

    # Distance covered when a robot turns a particular angle
    distance = (angle/360)*circumference

    # Translating the linear distance to motor turn angle
    turn_angle = (distance*360)/(2*(math.pi)*wheel_radius)

    # Move the left motor while right motor remains stationary
    left_motor.run_to_rel_pos(position_sp=turn_angle, speed_sp=200)

    # Wait for the motor to complete revolutions before any further actions
    left_motor.wait_while('running')
    


    
