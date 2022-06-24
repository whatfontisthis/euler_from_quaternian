import math

# quarternion to euler(radian)
def euler_from_quaternion_radian(x, y, z, w):

    t0 = +2.0 * (w * x + y * z)
    t1 = +1.0 - 2.0 * (x * x + y * y)
    roll_x = math.atan2(t0, t1)

    t2 = +2.0 * (w * y - z * x)
    t2 = +1.0 if t2 > +1.0 else t2
    t2 = -1.0 if t2 < -1.0 else t2
    pitch_y = math.asin(t2)

    t3 = +2.0 * (w * z + x * y)
    t4 = +1.0 - 2.0 * (y * y + z * z)
    yaw_z = math.atan2(t3, t4)

    print("Roll={}, Pitch={}, Yaw={}".format(roll_x, pitch_y, yaw_z))
    return roll_x, pitch_y, yaw_z


# quarternion to euler(degrees)
def euler_from_quaternion_degrees(x, y, z, w):

    t0 = +2.0 * (w * x + y * z)
    t1 = +1.0 - 2.0 * (x * x + y * y)
    roll_x = math.atan2(t0, t1)
    roll_x = roll_x * 180 / math.pi

    t2 = +2.0 * (w * y - z * x)
    t2 = +1.0 if t2 > +1.0 else t2
    t2 = -1.0 if t2 < -1.0 else t2
    pitch_y = math.asin(t2)
    pitch_y = pitch_y * 180 / math.pi

    t3 = +2.0 * (w * z + x * y)
    t4 = +1.0 - 2.0 * (y * y + z * z)
    yaw_z = math.atan2(t3, t4)
    yaw_z = yaw_z * 180 / math.pi

    #print("Roll={}, Pitch={}, Yaw={}".format(roll_x, pitch_y, yaw_z))
    return yaw_z



# euler_from_quaternion_radian(0, 0, 0.7072, 0.7072)
# euler_from_quaternion_degrees(0, 0, 0.7072, 0.7072)
