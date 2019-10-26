xterm -e ./run_rosbridge.sh &
sleep 2
xterm -e ./run_servos.sh &
sleep 2 
xterm -e ./run_camera1.sh &
sleep 5
xterm -e ./run_camera2.sh &
xterm -e rosrun web_video_server web_video_server
