# SPDX-FileCopyrightText: 2022 The pydiskcmd Authors
#
# SPDX-License-Identifier: LGPL-2.1-or-later
import optparse
import datetime
from pydiskcmd.system.env_var import os_type
from pydiskcmd.pydiskhistory.disk_information import get_stored_disk_info
from pydiskcmd.pydiskhistory.disk_smart_history import get_disk_temperature_history
from pydiskcmd.pydiskhistory.matplotlib_plot import PlotTemperature
from pydiskcmd.system.bash_completion import enable_cmd_completion
from pydiskcmd.system.pydiskhealth_daemon import enable_starup_programe,disable_starup_programe
#
from pydiskcmd.__version__ import version as ToolVersion
from pydiskcmd.pynvme.nvme import code_version as nvme_version
from pydiskcmd.pysata.sata import code_version as ata_version
from pydiskcmd.pyscsi.scsi import code_version as scsi_version
##

def pydiskutils():
    usage="usage: %prog [OPTION] [args...]"
    parser = optparse.OptionParser(usage,version="pydiskutils " + ToolVersion)
    parser.add_option("-d", "--device", dest="device_id", action="store",default="",
        help="Specify the device id to check, default all.")
    parser.add_option("", "--show_stored_disk", dest="show_stored_disk", action="store_true", default=False,
        help="Show stored disks information.")
    parser.add_option("", "--show_temperature", dest="show_temperature", action="store_true", default=False,
        help="Show the history of disk temperature")
    parser.add_option("-f", "--ouput_format", dest="ouput_format", action="store", default="console",
        help="The format of output, should be console|pciture|jsonfile")
    parser.add_option("-o", "--ouput_file", dest="ouput_file", action="store", default="",
        help="The name of output file.")
    parser.add_option("", "--enable", dest="enable_func", action="store", default="",
        help="Enable programe functions, include cmd_completion|auto_startup")
    parser.add_option("", "--disable", dest="disable_func", action="store", default="",
        help="Disable programe functions, include auto_startup")
    parser.add_option("", "--code_version", dest="code_version", action="store",default="pydiskcmd",
        help="Check code version: pydiskcmd|nvme|ata|scsi, default pydiskcmd")

    (options, args) = parser.parse_args()
    ##
    # Do not support windows now
    if os_type != "Linux":
        raise NotImplementedError("pydiskhealth cannot run in OS:%s" % os_type)
    #
    if options.ouput_format not in ("console", "pciture", "jsonfile"):
        parser.error("-o/--ouput_format should be one of console|pciture|jsonfile.")
    ##
    if options.show_stored_disk:
        info = get_stored_disk_info(target_dev_id=options.device_id)
        if options.ouput_format == "console":
            print_format = "%-12s: %s"
            for dev_id,disk_info in info.items():
                print (print_format % ("Device ID", disk_info[0]))
                print (print_format % ("Model", disk_info[1]))
                print (print_format % ("Serial", disk_info[2]))
                if disk_info[3] == 0:
                    media_t = "HDD"
                elif disk_info[3] == 1:
                    media_t = "SSD"
                else:
                    media_t = "Unknown"
                print (print_format % ("Media Type", media_t))
                if disk_info[4] == 0:
                    protocal = "SCSI"
                elif disk_info[4] == 1:
                    protocal = "ATA"
                elif disk_info[4] == 2:
                    protocal = "NVMe"
                else:
                    protocal = "Unknown"
                print (print_format % ("Protocal", protocal))
                print (print_format % ("Create Date", datetime.datetime.fromtimestamp(disk_info[5]).strftime("%Y-%m-%d %H:%M:%S.%f")))
                print ('-'*30)
        else:
            pass
    elif options.show_temperature:
        info = get_disk_temperature_history(target_dev_id=options.device_id)
        if options.ouput_format == "console":
            for dev_id,value in info.items():
                print ("Device ID: ", dev_id)
                for t,temperature in value:
                    print ("  %s(%s C): %s" % (datetime.datetime.fromtimestamp(t).strftime("%Y-%m-%d %H:%M:%S"),
                                               temperature, "#"*temperature)
                           )
                print ("-"*60)
        elif options.ouput_format == "pciture":
            if options.ouput_file:
                file_name = options.ouput_file
            else:
                file_name = "DiskTemperatureHistory.png"
            try:
                PlotTemperature(info, file_name)
            except ModuleNotFoundError:
                print ("Please install matplotlib first.")
        elif options.ouput_format == "jsonfile":
            pass
    elif options.enable_func:
        if options.enable_func == "cmd_completion":
            enable_cmd_completion()
        elif options.enable_func == "auto_startup":
            enable_starup_programe()
        else:
            parser.error("--enable should be one of the cmd_completion|auto_startup")
    elif options.disable_func:
        if options.disable_func == "auto_startup":
            disable_starup_programe()
        else:
            parser.error("--disable should be one of the auto_startup")
    elif options.code_version:
        if options.code_version == "pydiskcmd":
            print ('')
            print ('pydiskcmd version: %s' % ToolVersion)
            print ('')
        elif options.code_version == "nvme":
            print ('')
            print ('NVMe code version: %s' % nvme_version)
            print ('')
        elif options.code_version == "ata":
            print ('')
            print ('ATA code version: %s' % ata_version)
            print ('')
        elif options.code_version == "scsi":
            print ('')
            print ('SCSI code version: %s' % scsi_version)
            print ('')
        else:
            parser.error("Args of check code version should be one of pydiskcmd|nvme|ata|scsi")
    else:
        parser.print_help()
