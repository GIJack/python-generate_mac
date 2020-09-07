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
import generate_mac
g = generate_mac.generate_mac
```

Procedurely generated Vendor and Host bytes. Checks for broadcast bit

```
g.total_random()
'12:7E:C4:B5:F1:8E'
```

Read Vendor bytes from random line in a file. This has to be formated the same
as wireshark's manuf file.
```
g.vid_file_random('/usr/share/wireshark/manuf')
'00:55:DA:10:FB:D8'
```

Read from a manuf file like above, but find Vendor bytes belonging to a specific
vendor, by name.
```
g.vid_file_vendor('/usr/share/wireshark/manuf', 'Apple')
'94:0C:98:BC:74:1C'
```

Provide the vendor bytes in a string. Generate Host bytes only
```
g.vid_provided('AA:BB:CC')
'AA:BB:CC:B8:B3:01'
```

List valid vendor options as a list.
```
g.list_vendors('/usr/share/wireshark/manuf')
['Vendor1','Vendor2','etc']
```

Check if a MAC address is valid
```
if g.is_mac_address('94:0C:98:BC:74:1C') == True:
    print('Valid Ethernet Address')
```

Get the VID bytes from a MAC address
```
g.get_vid_bytes('94:0C:98:BC:74:1C')
'94:0C:98'
```
