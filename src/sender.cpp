#include <zmq.h>
#include <string.h>
#include <unistd.h>
#include <iostream>

int main() {
    void* context = zmq_ctx_new();
    void* socket = zmq_socket(context, ZMQ_PUSH);
    std::cout << "Connecting to the TCP socket..." << std::endl;
    int result = zmq_connect(socket, "tcp://10.0.0.119:5555");
    std::cout << "Connection result: " << result << std::endl;
    
    if (result != 0) {
        std::cerr << "Failed to connect to the socket." << std::endl;
        zmq_close(socket);
        zmq_ctx_destroy(context);
        return -1;
    }
    std::cout << "Sending messages..." << std::endl;
    for (int i = 0; i < 10; ++i) {
        std::cout << "Sending message " << i << std::endl;
        std::string msg = "Sensor value: " + std::to_string(i * 10);
        zmq_send(socket, msg.c_str(), msg.size(), 0);
        sleep(1);
    }
    zmq_close(socket);
    zmq_ctx_destroy(context);
    return 0;
}
