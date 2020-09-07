Python-generate_mac
===================

Python library for Generating Ethernet MAC addresses. Can use the wireshark manuf
for specific vendors, and or a random, but assigned address. Will work with
any file formated the same as said file.

Supported functions:

**total_random()** - Procedurely generated MAC address, using random function.

**vid_file_random(_file_)** - uses random line from wireshark's manuf file

**vid_file_vendor(_file, name_)** - specify a vendor name, uses wireshark's manuf file
instead of being completely random

**vid_provided(_vid bytes_)** - specify the VID bytes when calling the function.
Random device bytes will be generated.

**list_vendors(_file_)** - return a python list [] with valid vendors

**is_mac_address(_mac_)** - Takes a string, and checks if it is a valid Ethernet
MAC address. returns True or False(bool type)

Usage
-----

Import and set up an object.

```
from generate_mac import generate_mac
```

Procedurely generated Vendor and Host bytes. Checks for broadcast bit

```
generate_mac.total_random()
'7E:CD:60:1E:AC:6E'
```

Read Vendor bytes from random line in a file. This has to be formated the same
as wireshark's manuf file.
```
generate_mac.vid_file_random('/usr/share/wireshark/manuf')
'70:B3:D5:C5:40:49'
```

Read from a manuf file like above, but find Vendor bytes belonging to a specific
vendor, by name.
```
generate_mac.vid_file_vendor('/usr/share/wireshark/manuf', '3Com')
'00:06:8C:C7:3F:93'
```

Provide the vendor bytes in a string. Generate Host bytes only
```
generate_mac.vid_provided('00:06:8C')
'00:06:8C:35:5E:C4'
```

List valid vendor options as a list.
```
generate_mac.list_vendors('/usr/share/wireshark/manuf')
['Vendor1','Vendor2','etc']
```

Check if a MAC address is valid. returns a Bool(True,False)
```
generate_mac.is_mac_address('00:06:8C:35:5E:C4')
True
```

Get the VID bytes from a MAC address
```
generate_mac.get_vid_bytes('00:06:8C:35:5E:C4')
'00:06:8C'
```

Generate another MAC from the same VID bytes as current MAC
```
generate_mac.another_same_vid('00:06:8C:35:5E:C4')
'00:06:8C:3D:C2:F2'
```
