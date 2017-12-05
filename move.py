import rospy
from geometry_mgs.mgs import Twist
from math import pi

def move():
	velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
	vel_msg = Twist()
	print("Let's move your robot")
	speed = input("Input your speed:")
	distance = input("Type your distance:")
	isForward = input("Foward?: ")#True or False

	if (isForward):
		vel_msg.linear.x = abs(speed)
	else:
		vel_msg.linear.x = -abs(speed)

	vel_msg.linear.y = 0
	vel_msg.linear.z = 0
	vel_msg.angular.x = 0
	vel_msg.angular.y = 0
	vel_msg.angular.z = 0


	while not rospy.is_shutdown():
		
		t0 = rospy.Time.now().to_sec()
		current_distance = 0
		while (current_distance < distance):
			velocity_publisher.publish(vel_msg)
			t1 = rospy.Time.now().to_sec()
			current_distance = speed * (t1 - t0)

		vel_msg.linear.x = 0
		velocity_publisher.publish(vel_msg)

def rotate():
	velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
	vel_msg = Twist()

	print("Let's rotate your robot")
    speed = input("Input your speed (degrees/sec):")
    angle = input("Type your distance (degrees):")
    clockwise = input("Clockwise?: ") #True or false

    angular_speed = speed*2*pi/360
    relative_angle = angle*2*pi/360

    vel_msg.linear.x = 0
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0

    vel_msg.angular.x = 0
    vel_msg.angular.y = 0

    if clockwise:
    	vel_msg.angular.z = -abs(angular_speed)
    else:
    	vel_msg.angular.z = abs(angular_speed)
    t0 = rospy.Time.now().to_sec()
    current_angle = 0

    while (current_distance < distance):
    	velocity_publisher.publish(vel_msg)
    	t1 = rospy.Time.now().to_sec()
    	current_angle = angular_speed*(t1 - t0)

    vel_msg.angular.z = 0
    velocity_publisher.publish(vel_msg)
    rospy.spin()