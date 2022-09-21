# SPDX-FileCopyrightText: 2014 The python-scsi Authors
#
# SPDX-License-Identifier: LGPL-2.1-or-later

class CommandDecoder(object):
    def __init__(self):
        self.status = 0      ## Completion Queue Entry: Status Field
        self.cmd_spec = 0     ## Completion Queue Entry: Command Specific
        self.data = b''      ## Data
        self.meta_data = b'' ## meta data

    def check_status(self):
        SC = (self.status & 0xFF)
        SCT = ((self.status >> 8) & 0x07)
        CRD = ((self.status >> 11) & 0x03)
        More = (self.status >> 13)
        DNR = (self.status >> 14)
        if SCT == 0 and SC == 0:
            print ("Command Success")
        else:
            print ("Command failed, and details bellow.")
            format_string = "%-15s%-20s%-8s%s"
            print (format_string % ("Status Code", "Status Code Type", "More", "Do Not Retry"))
            print (format_string % (SC, SCT, More, DNR))
        print ('')
        return SC,SCT