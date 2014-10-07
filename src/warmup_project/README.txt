Computational Robotics
Warmup Project
Diana Vermilya

Which behaviors did you implement?
I implemented the wall follower and the person follower.  Both were implemented as PID controllers.

For each behavior, what strategy did you use to implement the behavior?
For the wall follower, I based my robot movements off both the robot's distance from the wall as well as its orientation.  The farther the robot was to the target distance from the wall (0.3 m), the more the robot turned toward the wall.  The farther the robot was from facing parallel to the wall, the more it turned to orient itself correctly.  This strategy had the benefit of allowing the robot to navigate both right and left turns fairly well, with no need for corner detection and a separate state.
For the person follower, I simply set the robots turn to be proportional to it's distance from the correct angle to follow the object detected.

For the finite state controller, which behaviors did you combine and how did you detect when to transition between behaviors?
I created a fairly simple algorithm to transition between the two states.  I defined an person as close readings that that occupied a segment of the laser scan less than 45 degrees.  If person was detected, the person follower took control.  If not, the controller reverted to wall following behavior.

How did you structure your code?
I put all my proportional control functions together in a proportional controller class.  I put the robot control functions in a follower class, where the follower class calls the proportional controller class in order to get coefficients. 

What if any challenges did you face along the way?
The main challenge was cleaning up the data.  By averaging 5 points for each point, and leaving out the non-reading points in averaging, I was able to clean up the data substantially.  It was also difficult to find the LIDAR scan segments for detecting objects, when wrapping around from 0 degrees to 360 degrees.  I dealt with this by using modulo to offset the discrepancy to behind the robot, where it was less relavent.

What would you do to improve your project if you had more time?
I would really have loved to use hough transforms to more accurately detect a wall.  This would have meant adding a seperate state for corners, which would have handled things differently, but I believe it would have given me a more accurate wall follower.  I wasn't getting anywhere close to the computational limits of the system, which indicates to me that I was wasting resources.

Did you learn any interesting lessons for future robotic programming projects?
I put a lot of thought into code structure, and I'm still not completely satisfied with my resulting code.  I think if the project was much larger, it would have been unsustainable.  Based on this, I'll definitely look into existing implementations of future indeavors, or projects that I'd expect to be structured similarly, just to get a feel for a good code layout.  Overall, though, I think the biggest lesson was that projects like this have a lot of overhead (learning how to work with ROS), but can be incredibly fun, so start early and work hard.