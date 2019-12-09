Python-generate_mac
===================

Python class for Generating Ethernet MAC addresses. Can use the wireshark manuf
for specific vendors, and or a random, but assigned address. Will work with
any file formated the same as said file.

Supported functions:

**total_random()** - Procedurely generated MAC address, using random function.

**vid_file_random(_file_)** - uses random line from wireshark's manuf file

**vid_file_vendor(_file, name_)** - specify a vendor name, uses wireshark's manuf file
instead of being completely random

**vid_provided(_vid bytes_)** - specify the VID bytes when calling the function.
Random device bytes will be generated.
