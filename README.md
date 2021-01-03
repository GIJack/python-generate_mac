Python-generate_mac
===================

Python library for working with Ethernet MAC addresses. Functions for generating
transforming and testing MAC addresses.

Uses Wireshark's manuf, or s similarly formated file as input for specific
Vendor ID(VID) bytes, for creating more 

Supported functions:

Generate
--------
**total_random()** - Procedurely generated MAC address, using random function.

**vid_file_random(_file_)** - uses random line from wireshark's manuf file

**vid_file_vendor(_file, vendor name, desc=optional_)** - specify a vendor name,
uses wireshark's manuf file instead of being completely random. May optionally
specify desc, which searches description within the vendor field

**vid_provided(_vid bytes_)** - specify the VID bytes when calling the function.
Random device bytes will be generated.

Test
-------
**list_vendors(_file_)** - return a python list [] with valid vendors

**is_mac_address(_mac_)** - Takes a string, and checks if it is a valid Ethernet
MAC address. returns True or False(bool type)

Transform
---------
**get_vid_bytes(_mac_)** - Returns the vendor bytes(first three) from a MAC address.

**another_same_vid(_mac)** - Generates another MAC with diffrent device bytes
with same vendor bytes as input

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
generate_mac.vid_file_vendor('/usr/share/wireshark/manuf',"Motorola")
'40:88:05:4F:CE:82'
```
*OPTIONAL:* this can also now search the description field

```
generate_mac.vid_file_vendor('/usr/share/wireshark/manuf',"Motorola","BSG")
'00:24:37:5C:3A:8B'
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
