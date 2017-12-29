# MagicalMusicalStaircase
Using Python, a Raspberry Pi, lasers, and photocells, any staircase can be turned into a musical staircase.
When the photocell senses an abrupt change in light, the RPi plays a note specific to that step.
The staircase is not sensitive to changes in ambient light as a expodential filter is used to find the threshold to play the note.

This project was made for Senior Project English @ ABRHS in 2017. Our purpose was to "spontaneously spread joy into people's lives" and we installed it in the school for a day. 
Here's a compililation of the student body's reaction: https://www.youtube.com/watch?v=zqAc1ACyDJQ



## Build Process
We started by building the sensor systems that would sit on each step. We attached lasers and photocells to blocks of wood that could be secured on the step. Then, we added long wires that could connect the sensors to the Raspberry Pi.
<img src="http://i65.tinypic.com/14ude81.png">
<img src="http://i67.tinypic.com/s3kqcx.png">

Next we built the circuits for the sensors on a breadboard.  Connecting the photocell is tricky because it outputs an analog signal while the RPi only processes digital signals. By putting a capacitor in series with the resistor we were able to succesfully convert the signal. [More can be read on this solution here.](https://www.element14.com/community/community/stem-academy/blog/2014/12/23/reading-a-photo-sensor-with-the-raspberry-pi-b) The lasers had a battery pack attached so they did not need connection with the RPi. We built the circuit 15 times on the breadboard, one for each step.
<img src="http://i63.tinypic.com/9pyqsy.png">
<img src="http://i66.tinypic.com/j7z4bd.png">

The final step in building the product was laser and sensor covers. With the components sitting bare on a very busy high school staircase, they were bound to be stepped on. We built covers with mini cereal boxes and spray painted them bright red. Once of our biggest probles was the accuracy of our lasers. We needed the beam to point directly at the 0.5cm by 0.5cm photocell, but the slightest vibration would throw off the calibration. To solve this we cut up a plastic container and used the pieces as lenses. They were glued on in front of the laser so the beam would diffuse to a relativeley larger area.
<img src="http://i67.tinypic.com/2powg91.png">
<img src="http://i64.tinypic.com/2zxuvdt.png">
