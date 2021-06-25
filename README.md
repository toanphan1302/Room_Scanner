# Room_Scanner
Designed a device that allows people to scan a space by measuring distance in different angles.
    o	Used the Pi Pico microcontroller to control sensor and motors.
    o	Used TF mini LiDAR for distance sensor using UART communication protocol.
    o	Controlled two servo motors for horizontal and vertical rotation using PWM.
    o	Designed python code:
              ▪	Get distance and motors positions.
              ▪	Function to convert distance and motors position to x,y,z positions.
              ▪	Create 3D map in form of point cloud with different colors for different distances.
