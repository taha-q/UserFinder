# Userfinder Simplified
This a Simplified and easy version of the Userfinder


# installation
    .Termux: ```bash
             pkg update && yes | pkg upgrade;\
             pkg install python3 python3-venv python3-pip -y\
             python3 -m venv userfinder-venv && source userfinder-venv/bin/activate;\
             pip install requests
             ```

    .APT based distro: ```bash
             apt update && yes | apt upgrade;\
             apt install python3 python3-venv python3-pip -y\
             python3 -m venv userfinder-venv && source userfinder-venv/bin/activate;\
             pip install requests
             ```
