#!/usr/bin/env python3
import stretch_ik as IK
import random

target_orientation = IK.ikpy.utils.geometry.rpy_matrix(0.0, 0.0, -7*(IK.np.pi/4))
pretarget_orientation = IK.ikpy.utils.geometry.rpy_matrix(0.0, 0.0, 0.0)

def generate_random_3d_point():
    
    # when orientation.z is -7*(IK.np.pi/4), y = (-0.48, -0.1) and z = 0.165
    # when orientation.z is -IK.np.pi/4,  x = 0.165 and y = (-0.7, -0.4)
    # When orientation.z is -IK.np.pi/2, x = -0.0199 and y = (-0.7, -0.4)
    
    x = 0.165
    y = round(random.uniform(-0.48, -0.1), 2)
    z = 1.2
    z = 1.1

    target_point = [x, y, z]
    return target_point

def main():
    points = [generate_random_3d_point() for _ in range(10)]
    print("Press Enter to print a random 3D point. Press 'q' to exit.")

    while True:
        uInput = input()
        if uInput.lower() == 'q':
            break
        elif uInput == '':
            randP = random.choice(points)
            print("3D point: ", randP)
            IK.move_to_grasp_goal(randP, target_orientation, pretarget_orientation)
if __name__ == "__main__":
    main()
