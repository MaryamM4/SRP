clang++ -std=c++17 webcam_head_pose.cpp TcpSocket.cpp -g3 -ggdb -O3 -I/usr/local/lib/JetsonGPIO/include/ -I/usr/local/include/opencv4/ -I/usr/local/include/ -L/usr/local/lib/ -lpthread -lopencv_video -lopencv_core -lopencv_videoio -lopencv_highgui -lopencv_imgproc -lopencv_calib3d -ldlib -llapack -lblas -lgif -o FaceposeEstimation.exe