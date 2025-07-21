# Notes for Developers

The following file contains general notes for users to wish to develop this software.

## How To Set Up PI to Forward Data

The Guide below outlines the steps needed to setup the PI to run the script to forward data over TCP.

### Prerequisites

- Python 3.x installed
- pip (Python package installer)

### Virtual Environment Setup

1. Open terminal in project directory
2. Create virtual environment:

```bash
python -m venv venv
```

3. Activate virtual environment:

```bash
source venv/bin/activate
```

### Install Required Libraries

With virtual environment activated:

1. Install ZMQ:

```bash
pip install pyzmq
```

2. Install RPi.GPIO:

```bash
pip install RPi.GPIO
```

### Running the Script

```bash
python3 zeromq.py
```

### Notes

- RPi.GPIO only works on Raspberry Pi hardware
- Keep virtual environment active while running the program
- To deactivate virtual environment when done:

```bash
deactivate
```
