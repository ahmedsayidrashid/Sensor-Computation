#include <zmq.h>
#include <string.h>
#include <iostream>

using namespace std;

int main() {
    cout << "Creating context..." << endl;
    void* context = zmq_ctx_new();
    void* socket = zmq_socket(context, ZMQ_PULL);
    cout << "Binding to the TCP socket..." << endl;
    int result = zmq_bind(socket, "tcp://10.0.0.119:5555");
    cout << "Bind result: " << result << endl;
    if (result != 0) {
        cerr << "Failed to bind to the socket." << endl;
        zmq_close(socket);
        zmq_ctx_destroy(context);
        return -1;
    }
    while (true) {
        char buffer[256];
        int bytes = zmq_recv(socket, buffer, 255, 0);
        buffer[bytes] = '\0';
        std::cout << "[Received] " << buffer << std::endl;
    }
    zmq_close(socket);
    zmq_ctx_destroy(context);
    return 0;
}
