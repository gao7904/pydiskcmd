<!--
SPDX-FileCopyrightText: 2022 The python-scsi Authors

SPDX-License-Identifier: LGPL-2.1-or-later
-->

pydiskcmd
=========
pydiskcmd is a disk command tool for python3. It can send command to SATA/SAS/NVMe 
disk, as also as monitor the disk health.

In Linux, there is some tools to handle disk, like hdparm,smartctl,nvme-cli 
and etc. But I still hope to develop a tool to cover all the sata,sas,nvme disks.
It should be easily installed and should be able to send raw commands to target 
disks, provide a high-level API to build raw command with different protocal. 
Besides, it could monitor the health of the disks, especially take full advantage 
of NVMe(which offer a better monitoring mechanism). 

While in Windows, rarely find out an open source user level disk tool. I hope it 
is convenient to handle a disk in windows as if it is in Linux.

This project is more of a code collection, it was born and grow in the open source 
codes from github.


License
=======
pydiskcmd is distributed under LGPLv2.1.
Please see the LICENSE file for the full license text.


Getting the sources
===================
The module(source) is hosted at https://github.com/jackeichen/pydiskcmd

You can use git to checkout the latest version of the source code using:

    $ git clone git@github.com:jackeichen/pydiskcmd.git

It is also available as a downloadable zip archive from:

    https://github.com/jackeichen/pydiskcmd/archive/master.zip


Support List
============

| OS                    | arc | SCSI | ATA | NVME |
|-----------------------|-----|------|-----|------|
| CentOS/RHEL 7.6       | x64 | Y    | Y   | Y    |
| CentOS/RHEL 8.4       | x64 | Y    | Y   | Y    |
| RHEL 9.1              | x64 | Y    | Y   | Y    |
| Ubuntu 22.04          | x64 | Y    | Y   | Y    |
| Windows 10 Pro        | x64 | Y    | Y   | Y    |
| Windows 11            | x64 | Y    | Y   | Y    |
| Windows Server 2019   | x64 | Y    | Y   | T    |
| Windows Server 2022   | x64 | Y    | Y   | T    |

Y: support, N: Non-support, D: Developing, T: Under Testing

Note:

    * Only some of the commands are tested, Do Not guarantee all the other commands work;
    * This tool should work in Linux&Windows, but may be incompatible in OS other than this Support List;
    * Support Direct-Connection/HBA Mode/JBOD Mode, RAID Mode is not support.


Building and installing
=======================

Python3 Module Requirements:

    * setuptools_scm
    * pyscsi(Need download the latest python-scsi from github)

Extra Python3 Module Requirements by Linux:

    * cython-sgio(Need by pyscsi, download latest version from github)
    * pcicrawler

Sofware Requirements:

    * python3
    * python3-devel(only for linux)

To build and install from the repository:

    $ pip install .

After your installation, you can use command to enable or update Linux Bash 
Completion for command pynvme&pysata&pyscsi(Only for Linux):

    $ pydiskutils --enable=cmd_completion

You can uninstall it by run:

    $ pip uninstall pydiskcmd


Usage
=====
Five executable programs should be added to environment variables after installation.

pydiskutils
-----------
It is a program that show and manage pydiskcmd tool. Use bellow command to get help:

    $ pydiskutils --help
```
Usage: pydiskutils [OPTION] [args...]

Options:
  --version             show program's version number and exit
  -h, --help            show this help message and exit
  -d DEVICE_ID, --device=DEVICE_ID
                        Specify the device id to check, default all.
  --show_stored_disk    Show stored disks information.
  --show_temperature    Show the history of disk temperature
  -o OUPUT_FORMAT, --ouput_format=OUPUT_FORMAT
                        The format of output, should be
                        console|picture|jsonfile
  -f OUPUT_FILE, --ouput_file=OUPUT_FILE
                        The name of output file.
  --enable=ENABLE_FUNC  Enable programe functions, include
                        cmd_completion|auto_startup
  --disable=DISABLE_FUNC
                        Disable programe functions, include auto_startup
  --code_version=CODE_VERSION
                        Check code version: pydiskcmd|nvme|ata|scsi, default
                        pydiskcmd
```

pynvme
------
It is a program similar to nvme-cli, with some limitted commands inside. Use bellow
command to get help:

    $ pynvme help

```
pynvme-0.1.0
usage: pynvme <command> [<device>] [<args>]

The '<device>' may be either an NVMe character device (ex: /dev/nvme0) or an
nvme block device (ex: /dev/nvme0n1).

The following are all implemented sub-commands:
  list                  List all NVMe devices and namespaces on machine
  list-ns               Send NVMe Identify List, display structure
  list-ctrl             Send NVMe Identify Controller List, display structure
  smart-log             Retrieve SMART Log, show it
  id-ctrl               Send NVMe Identify Controller
  id-ns                 Send NVMe Identify Namespace, display structure
  nvme-create-ns        Creates a namespace with the provided parameters
  nvme-delete-ns        Deletes a namespace from the controller
  nvme-attach-ns        Attaches a namespace to requested controller(s)
  nvme-detach-ns        Detaches a namespace from requested controller(s)
  error-log             Retrieve Error Log, show it
  commands-se-log       Retrieve Commands Supported and Effects Log, and show it
  fw-log                Retrieve FW Log, show it
  fw-download           Download new firmware
  fw-commit             Verify and commit firmware to a specific slot
  get-feature           Get feature and show the resulting value
  set-feature           Set a feature and show the resulting value
  format                Format namespace with new block format
  persistent_event_log  Get persistent event log from device
  device-self-test      Perform the necessary tests to observe the performance
  self-test-log         Retrieve the SELF-TEST Log, show it
  pcie                  Get device PCIe status, show it
  flush                 Submit a flush command, return results
  read                  Submit a read command, return results
  verify                Submit a verify command, return results
  write                 Submit a write command, return results
  get-lba-status        Submit a Get LBA Status command, return results
  version               Shows the program version
  help                  Display this help

See 'pynvme help <command>' or 'pynvme <command> --help' for more information on a sub-command
```

pysata
------
It is a sata command tool, to send ATA command to SATA Disk, with some limitted 
commands inside. Use bellow command to get help:

    $ pysata help

```
pysata-0.2.0
usage: pysata <command> [<device>] [<args>]

The '<device>' is usually a character device (ex: /dev/sdb or physicaldrive1).

The following are all implemented sub-commands:
  list                        List all ATA devices on machine
  check-PowerMode             Check Disk Power Mode
  accessible-MaxAddress       Send Accessible Max Address command
  identify                    Get identify information
  self-test                   Start a disk self test
  smart                       Get smart information
  read-log                    Get the GPL Log and show it
  smart-read-log              Get the smart Log and show it
  standby                     Send standby command
  read                        Send a read command to disk
  write                       Send a write command to disk
  flush                       Send a flush command to disk
  trim                        Send a trim command to disk
  download_fw                 Download firmware to target disk
  version                     Shows the program version
  help                        Display this help

See 'pysata help <command>' or 'pysata <command> --help' for more information on a sub-command
```

pyscsi
------
It is a scsi command tool, to send scsi command to SAS Disk, with some limitted 
commands inside. Use bellow command to get help:

    $ pyscsi help

```
pyscsi 0.2.0
usage: pyscsi <command> [<device>] [<args>]

The '<device>' is usually a character device (ex: /dev/sdb or physicaldrive1).

The following are all implemented sub-commands:
  inq                         Send scsi inquiry command
  getlbastatus                Get LBA Status from target SCSI device
  read                        Send a read command to disk
  write                       Send a write command to disk
  version                     Shows the program version
  help                        Display this help

See 'pyscsi help <command>' or 'pyscsi <command> --help' for more information on a sub-command
```

pydiskhealthd
-------------
This is a Disk Health Monitoring and Reporting tool only for Linux. See below pydiskhealthd 
for more detail. Use bellow command to get help:

    $ pydiskhealthd -h


pydiskhealthd
=============
pydiskhealthd is a Disk Health Monitoring and Reporting tool. It check NVMe PCie Registers 
and smart for nvme disk, smart attributes for sata disk, in a specific time interval(default 1h). 
The pydiskhealthd usually runs in only-one-per-environment mode(default mode). 

Logs maybe Generated when below values changed/set/fall below threshold. These logs may record to 
either syslog(Linux in/var/log/message, Windows Not Implement) or pydiskhealthd running log(Linux 
in /var/log/pydiskcmd/pydiskhealthd.log or windows in C:\Windows\Temp\pydiskcmd\pydiskhealthd.log), 
or both of them.

For NVMe Disk:
  
  * PCIe Link Status(Only in Linux);
  * PCIe AER Registers(Only in Linux);
  * smart values;
  * Persistent Event Logs;
  * AER Event Check(Only in Linux);

The tool provide a real-time NVMe Asynchronous Event Request check by reading Linux trace file(Need Enable 
Linux Trace function). You can set the event that you want to trigger by sending nvme set-feature command. 
Examples(set temperature warning):

    $ pynvme get-feature /dev/nvme0 -f 0x0B 

and the value is 0x100 now, set the Critical Warning temperature check:

    $ pynvme set-feature /dev/nvme0 -f 0x0B -v 0x102

For SATA Disk:

  * Smart Pre-fail/Old_age attributes; 

The user(need root) can enable systemd service(pydiskhealthd.service), which make pydiskhealthd running as a 
backend service and start-up service. Enable and start it by: 

    $ pydiskutils --enable=auto_startup 

After that, the linux user can manage the pydiskhealthd with task name "pydiskhealthd".

Linux:

    $ systemctl status pydiskhealthd.service

Or Windows:

`> schtasks /Query /TN pydiskhealthd`



Advanced Usage
==============
You can find some examples about how to use this tool in the dir of pydiskcmd/examples/.

Build Your Own Command 
----------------------
Example to build and run your own NVMe command in Linux.

```
### nvme format command
## <Command> is the wrapper of raw command data structure, you can find it in pydiskcmd/pynvme/nvme_command,
#  <build_command> is the methmod to build cdw data structure
##
from pydiskcmd.pynvme.nvme_command import LinCommand,build_int_by_bitmap
## for running your own command in device, and get the result.
from pydiskcmd.utils import init_device

CmdOPCode = 0x80 # nvme format command OP code, see nvme spec
IOCTL_REQ = LinCommand.linux_req.get("NVME_IOCTL_ADMIN_CMD") # NVME_IOCTL_ADMIN_CMD Code type

class Format(LinCommand): 
    def __init__(self, 
                 lbaf,            # the lbaf to format, see nvme spec
                 mset=0,          # the mset to format, see nvme spec
                 pi=0,            # the pi to format, see nvme spec
                 pil=1,           # the pil to format, see nvme spec
                 ses=0,           # the ses to format, see nvme spec
                 nsid=0xFFFFFFFF, # the nsid to format, see nvme spec
                 timeout=600000): # timeout(millisecond) in IOCTL request
        ## build command cdw10
        #  this is a key-value dict input:
        #    key: the name of value
        #    value: (the bit-map of value, Byte offset in DWord, value to set)
        ##
        cdw10 = build_int_by_bitmap({"lbaf": (0x0F, 0, lbaf), # the location of lbaf in cdw10, see nvme spec
                                     "mset": (0x10, 0 ,mset), # the location of mset in cdw10, see nvme spec
                                     "pi": (0xE0, 0, pi),     # the location of pi in cdw10, see nvme spec
                                     "pil": (0x01, 1, pil),   # the location of pil in cdw10, see nvme spec
                                     "ses": (0x0E, 1, ses)})  # the location of ses in cdw10, see nvme spec
        ##
        super(Format, self).__init__(IOCTL_REQ)
        # build command
        self.build_command(opcode=CmdOPCode,
                           nsid=nsid,
                           cdw10=cdw10,
                           timeout_ms=timeout)

cmd = Format(0, nsid=1) ## format namespace 1 to lbaf 0
with init_device('/dev/nvme1', open_t='nvme') as d: ## open a nvme device: /dev/nvme1
    d.execute(cmd)
## Get the command result-> 
print (cmd.cq_cmd_spec) # Command Specific Status Values, see nvme spec
SC,SCT = cmd.check_return_status() # Get Command Status Code and Status Code Type
print ("Command Status Code=%d, Status Code Type=%d" % (SC,SCT))
```

Example to build and run your own SATA command in Linux Or Windows.

```
### Send an Identify command to SATA Disk
## pydiskcmd send SATA command by scsi passthrough12 or passthrough16 command
## This will import a suitable SCSIDevice depends on your OS,
#  The SCSIDevice help to send the command to device and get the result from the device
from pydiskcmd.utils import init_device
## ATACommand16 is the wrapper of ATA command, it help to build your own command
#  You can read ACS-3 about the ATA command set, and
#  read SAT-5 to make out how to translate from ATA command to SCSI passthrough command
from pydiskcmd.pysata.ata_command import ATACommand16


class Identify16(ATACommand16): 
    def __init__(self):
        ##
        # count is not used by idedntify in ATA command set,
        # so use it in ATAPassthrouh16, for setting transfer length
        ##
        ATACommand16.__init__(self,
                              0,         # fetures field
                              1,         # count field
                              0,         # lba field
                              0,         # device field
                              0xec,      # command field
                              0x04,      # protocal field
                              2,         # t_length field
                              1)         # t_dir field 

identify_cmd = Identify16()
with init_device("/dev/sdb", open_t='scsi') as d:
    d.execute(identify_cmd, en_raw_sense=True)
## Get the Result
# Handle the Command execute sense data
#  SAT-5 to make out ata_return_descriptor
ata_return_descriptor = cmd.ata_status_return_descriptor
print ("Command return Status:", ata_return_descriptor.get("status"))
# Get the datain, that read from device 
print ("Identify data read from device is:")
print (cmd.datain)
```

Example to build and run your own SCSI command in Linux Or Windows. It is a little different from
NVMe Or SATA, the methmod is from the project python-scsi.

```
from pyscsi.pyscsi.scsi_command import SCSICommand
from pyscsi.pyscsi.scsi_enum_command import mmc, sbc, smc, spc, ssc
from pydiskcmd.utils import init_device

class Read16(SCSICommand):
    ## You need define the _cdb_bits to build cdb

    _cdb_bits = {
        "opcode": [0xFF, 0],
        "rdprotect": [0xE0, 1],
        "dpo": [0x10, 1],
        "fua": [0x08, 1],
        "rarc": [0x04, 1],
        "lba": [0xFFFFFFFFFFFFFFFF, 2],
        "group": [0x1F, 14],
        "tl": [0xFFFFFFFF, 10],
    }

    def __init__(
        self, lba, tl, rdprotect=0, dpo=0, fua=0, rarc=0, group=0
    ):
        """
        initialize a new instance

        :param lba: Logical Block Address
        :param tl: transfer length
        :param rdprotect=0:
        :param dpo=0:
        :param fua=0:
        :param rarc=0:
        :param group=0:
        """
        if blocksize == 0:
            raise SCSICommand.MissingBlocksizeException
        
        ##
        # This command is sbc command->READ_16, usually get by inquiry command, and
        # and the device is 512 byte logical format.
        ##
        opcode = sbc.READ_16
        blocksize= 512
        ## Build command
        SCSICommand.__init__(self, opcode, 0, blocksize * tl)

        self.cdb = self.build_cdb(
            opcode=self.opcode.value,
            lba=lba,
            tl=tl,
            rdprotect=rdprotect,
            dpo=dpo,
            fua=fua,
            rarc=rarc,
            group=group,
        )
## send command: 4k read from LBA 0 to LBA 7
cmd = Read16(0, 8)
## Execute Command
with init_device("/dev/sdb", open_t='scsi') as d:
    d.execute(cmd)
## Get the result
print (cmd.datain)
```


Acknowledgements
================
Really appreciate the project python-scsi in github.

* Python-scsi: https://github.com/python-scsi/python-scsi

pcicrawler is a CLI tool to display/filter/export information about PCI or 
PCI Express devices and their topology.

* pcicrawler: https://github.com/facebook/pcicrawler

smartie is a pure-python library for getting basic disk information such as 
model, serial number, disk health, temperature, etc...

* smartie: https://github.com/TkTech/smartie

Communicate with NVMe SSD using Windows' inbox device driver

* nvmetool-win: https://github.com/ken-yossy/nvmetool-win


Reference
=========
How SSDs Fail – NVMe™ SSD Management, Error Reporting, and Logging Capabilities: 
https://nvmexpress.org/how-ssds-fail-nvme-ssd-management-error-reporting-and-logging-capabilities/


Support
=======
If any support or ideas, open an issue, or contact author by email: Eric-1128@outlook.com
