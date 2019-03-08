# Sensor Bus Utilty

Linux contains a variety of drivers to interface to sensors on the i2c, spi, 1 wire, and more "buses". Each driver presents an easy to use interface through the /sys/bus file system. Drivers present their data in easy to read files that any application can ready. This eliminates the need for special library code to talk on each of the buses and query data greatly reducing the amount of code required.

The issue that this utility solves is how to have the files in the /sys file system appear at boot time. Each new device in say the i2c bus require a kernel driver and then requires telling the kernel the address in the i2c bus, for example. This means the user must send the module name and address to the i2c bus, in this case, as root. This is not convenient, say, from a python script running as a normal user.

This utility installs itself as a systemd service, and reads the /etc/sensorbuses.conf file at boot time, loading the driver and configuring the kernel accordingly.

While it should work on any linux system, it has only been tested on a Raspberry PI and assumes python3 is installed.

CODE IS UNDER DEVELOPMENT

