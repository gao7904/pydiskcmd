# SPDX-FileCopyrightText: 2014 The python-scsi Authors
#
# SPDX-License-Identifier: LGPL-2.1-or-later
from pydiskcmd.utils.converter import decode_bits

nvme_smart_bit_mask = {"Critical Warning": ('b', 0, 1),
                       "Composite Temperature": ('b', 1, 2),
                       "Available Spare": ('b', 3, 1),
                       "Available Spare Threshold": ('b', 4, 1),
                       "Percentage Used": ('b', 5, 1),
                       "Endurance Group Critical Warning Summary": ('b', 6, 1),
                       "Data Units Read": ('b', 32, 16),
                       "Data Units Written": ('b', 48, 16),
                       "Host Read Commands": ('b', 64, 16),
                       "Host Write Commands": ('b', 80, 16),
                       "Controller Busy Time": ('b', 96, 16),
                       "Power Cycles": ('b', 112, 16),
                       "Power On Hours": ('b', 128, 16),
                       "Unsafe Shutdowns": ('b', 144, 16),
                       "Media and Data Integrity Errors": ('b', 160, 16),
                       "Number of Error Information Log Entries": ('b', 176, 16),
                       "Warning Composite Temperature Time": ('b', 192, 4),
                       "Critical Composite Temperature Time": ('b', 196, 4),
                       }


nvme_id_ctrl_bit_mask = {"VID": ('b', 0, 2),
                         "SSVID": ('b', 2, 2),
                         "SN": ('b', 4, 20),
                         "MN": ('b', 24, 40),
                         "FR": ('b', 64, 8),
                         "RAB": ('b', 72, 1),
                         "IEEE": ('b', 73, 3),
                         "CMIC": ('b', 76, 1),
                         "MDTS": ('b', 77, 1),
                         "CNTLID": ('b', 78, 2),
                         "VER": ('b', 80, 4),
                         "RTD3R": ('b', 84, 4),
                         "RTD3E": ('b', 88, 4),
                         "OAES": ('b', 92, 4),
                         "CTRATT": ('b', 96, 4),
                         "RRLS": ('b', 100, 2),
                         "CNTRLTYPE": ('b', 111, 1),
                         "FGUID": ('b', 112, 16),
                         "CRDT1": ('b', 128, 2),
                         "CRDT2": ('b', 130, 2),
                         "CRDT3": ('b', 132, 2),
                         "OACS": ('b', 256, 2),           ## Optional Admin Command Support
                         "ACL": ('b', 258, 1),            ## Abort Command Limit
                         "AERL": ('b', 259, 1),           ## Asynchronous Event Request Limit
                         "FRMW": ('b', 260, 1),           ## Firmware Updates
                         "LPA": ('b', 261, 1),            ## Log Page Attributes
                         "ELPE": ('b', 262, 1),           ## Error Log Page Entries
                         "NPSS": ('b', 263, 1),           ## Number of Power States Support
                         "AVSCC": ('b', 264, 1),          ## Admin Vendor Specific Command Configuration
                         "APSTA": ('b', 265, 1),          ## Autonomous Power State Transition Attributes
                         "WCTEMP": ('b', 266, 2),         ## Warning Composite Temperature Threshold
                         "CCTEMP": ('b', 268, 2),         ## Critical Composite Temperature Threshold
                         "MTFA": ('b', 270, 2),           ## Maximum Time for Firmware Activation
                         "HMPRE": ('b', 272, 4),          ## Host Memory Buffer Preferred Size
                         "HMMIN": ('b', 276, 4),          ## Host Memory Buffer Minimum Size
                         "TNVMCAP": ('b', 280, 16),       ## Total NVM Capacity
                         "UNVMCAP": ('b', 296, 16),       ## Unallocated NVM Capacity
                         "RPMBS": ('b', 312, 4),          ## Replay Protected Memory Block Support
                         "EDSTT": ('b', 316, 2),          ## Extended Device Self-test Time
                         "DSTO": ('b', 318, 1),           ## Device Self-test Options
                         "FWUG": ('b', 319, 1),           ## Firmware Update Granularity
                         "KAS": ('b', 320, 2),            ## Keep Alive Support
                         "HCTMA": ('b', 322, 2),          ## Host Controlled Thermal Management Attributes
                         "MNTMT": ('b', 324, 2),          ## Minimum Thermal Management Temperature
                         "MXTMT": ('b', 326, 2),          ## Maximum Thermal Management Temperature
                         "SANICAP": ('b', 328, 4),        ## Sanitize Capabilities
                         "HMMINDS": ('b', 332, 4),        ## Host Memory Buffer Minimum Descriptor Entry Size
                         "HMMAXD": ('b', 336, 2),         ## Host Memory Maximum Descriptors Entries
                         "NSETIDMAX": ('b', 338, 2),      ## NVM Set Identifier Maximum
                         "ENDGIDMAX": ('b', 340, 2),      ## Endurance Group Identifier Maximum
                         "ANATT": ('b', 342, 1),          ## ANA Transition Time
                         "ANACAP": ('b', 343, 1),         ## Asymmetric Namespace Access Capabilities
                         "ANAGRPMAX": ('b', 344, 4),      ## ANA Group Identifier Maximum
                         "NANAGRPID": ('b', 348, 4),      ## Number of ANA Group Identifiers
                         "PELS": ('b', 352, 4),           ## Persistent Event Log Size
                         "SQES": ('b', 512, 1),           ## Submission Queue Entry Size
                         "CQES": ('b', 513, 1),           ## Completion Queue Entry Size
                         "MAXCMD": ('b', 514, 2),         ## Maximum Outstanding Commands
                         "NN": ('b', 516, 4),             ## Number of Namespaces
                         "ONCS": ('b', 520, 2),           ## Optional NVM Command Support
                         "FUSES": ('b', 522, 2),          ## Fused Operation Support
                         "FNA": ('b', 524, 1),            ## Format NVM Attributes
                         "VWC": ('b', 525, 1),            ## Volatile Write Cache
                         "AWUN": ('b', 526, 2),           ## Atomic Write Unit Normal
                         "AWUPF": ('b', 528, 2),          ## Atomic Write Unit Power Fail
                         "NVSCC": ('b', 530, 1),          ## NVM Vendor Specific Command Configuration
                         "NWPC": ('b', 531, 1),           ## Namespace Write Protection Capabilities
                         "ACWU": ('b', 532, 2),           ## Atomic Compare & Write Unit
                         "SGLS": ('b', 536, 4),           ## SGL Support
                         "MNAN": ('b', 540, 4),           ## Maximum Number of Allowed Namespaces
                         "SUBNQN": ('b', 768, 256),       ## NVM Subsystem NVMe Qualified Name
                       }

nvme_id_ctrl_ps_bit_mask = {"MP": ('b', 0, 2),            ## Maximum Power
                            "MXPS": [0x01, 3],            ## Max Power Scale
                            "NOPS": [0x02, 3],            ## Non-Operational State
                            "ENLAT": ('b', 4, 4),         ## Entry Latency
                            "EXLAT": ('b', 8, 4),         ## Exit Latency
                            "RRT": [0x1F, 12],            ## Relative Read Throughput
                            "RRL": [0x1F, 13],            ## Relative Read Latency
                            "RWT": [0x1F, 14],            ## Relative Write Throughput
                            "RWL": [0x1F, 15],            ## Relative Write Latency
                            "IDLP": ('b', 16, 2),         ## Idle Power
                            "IPS": [0xC0, 18],            ## Idle Power Scale
                            "ACTP": ('b', 20, 2),         ## Active Power
                            "APW": [0x07, 22],            ## Active Power Workload
                            "APS": [0xC0, 22],            ## Active Power Scale
                           }


nvme_id_ns_bit_mask = {"NSZE": ('b', 0, 8),               ## Namespace Size
                       "NCAP": ('b', 8, 8),               ## Namespace Capacity
                       "NUSE": ('b', 16, 8),              ## Namespace Utilization
                       "NSFEAT": ('b', 24, 1),            ## Namespace Features
                       "NLBAF": ('b', 25, 1),             ## Number of LBA Formats
                       "FLBAS": ('b', 26, 1),             ## Formatted LBA Size
                       "MC": ('b', 27, 1),                ## Metadata Capabilities
                       "DPC": ('b', 28, 1),               ## End-to-end Data Protection Capabilities
                       "DPS": ('b', 29, 1),               ## End-to-end Data Protection Type Settings
                       "NMIC": ('b', 30, 1),              ## Namespace Multi-path I/O and Namespace Sharing Capabilities
                       "RESCAP": ('b', 31, 1),            ## Reservation Capabilities
                       "FPI": ('b', 32, 1),               ## Format Progress Indicator
                       "DLFEAT": ('b', 33, 1),            ## Deallocate Logical Block Features
                       "NAWUN": ('b', 34, 2),             ## Namespace Atomic Write Unit Normal
                       "NAWUPF": ('b', 36, 2),            ## Namespace Atomic Write Unit Power Fail
                       "NACWU": ('b', 38, 2),             ## Namespace Atomic Compare & Write Unit
                       "NABSN": ('b', 40, 2),             ## Namespace Atomic Boundary Size Normal
                       "NABO": ('b', 42, 2),              ## Namespace Atomic Boundary Offset
                       "NABSPF": ('b', 44, 2),            ## Namespace Atomic Boundary Size Power Fail
                       "NOIOB": ('b', 46, 2),             ## Namespace Optimal I/O Boundary 
                       "NVMCAP": ('b', 48, 16),           ## NVM Capacity
                       "NPWG": ('b', 64, 2),              ## Namespace Preferred Write Granularity 
                       "NPWA": ('b', 66, 2),              ## Namespace Preferred Write Alignment
                       "NPDG": ('b', 68, 2),              ## Namespace Preferred Deallocate Granularity
                       "NPDA": ('b', 70, 2),              ## Namespace Preferred Deallocate Alignment
                       "NOWS": ('b', 72, 2),              ## Namespace Optimal Write Size
                       "ANAGRPID": ('b', 92, 4),          ## ANA Group Identifier
                       "NSATTR": ('b', 99, 1),            ## Namespace Size
                       "NVMSETID": ('b', 100, 2),         ## NVM Set Identifier
                       "ENDGID": ('b', 102, 2),           ## Endurance Group Identifier
                       "NGUID": ('b', 104, 16),           ## Namespace Globally Unique Identifier
                       "EUI64": ('b', 120, 8),            ## Number of LBA Formats
                      }


nvme_id_ns_lbaf_bit_mask = {"MS": ('b', 0, 2),            ## Metadata Size
                            "LBADS": ('b', 2, 1),         ## LBA Data Size
                            "RP": [0x03, 3],              ## Relative Performance
                           }

nvme_fw_slot_info_bit_mask  = {"AFI": ('b', 0, 1),      ## Active Firmware Info
                               "FRS1": ('b', 8, 8),     ## Firmware Revision for Slot 1
                               "FRS2": ('b', 16, 8),    ## Firmware Revision for Slot 2
                               "FRS3": ('b', 24, 8),    ## Firmware Revision for Slot 3
                               "FRS4": ('b', 32, 8),    ## Firmware Revision for Slot 4
                               "FRS5": ('b', 40, 8),    ## Firmware Revision for Slot 5
                               "FRS6": ('b', 48, 8),    ## Firmware Revision for Slot 6
                               "FRS7": ('b', 56, 8),    ## Firmware Revision for Slot 7
                              }


nvme_power_management_cq_bit_mask = {"PS": [0x1F, 0],   ## Power State
                                     "WH": [0xE0, 0],   ## Workload Hint
                                    }


nvme_error_log_entry_bit_mask = {}


class ErrorInfomationLogEntryUnit(object):
    def __init__(self, data):
        self.error_count = int.from_bytes(data[0:8], byteorder='little', signed=False)
        self.sqid = int.from_bytes(data[8:10], byteorder='little', signed=False)
        self.cid = int.from_bytes(data[10:12], byteorder='little', signed=False)
        self.phase_tag = data[12] & 0x01
        self.status_field = ((data[12] >> 1) & 0x7F) + (data[13] << 15)
        self.para_error_location = int.from_bytes(data[14:16], byteorder='little', signed=False)
        self.lba = int.from_bytes(data[16:24], byteorder='little', signed=False)
        self.ns = int.from_bytes(data[24:28], byteorder='little', signed=False)
        self.vendor_spec_info_ava = data[28]
        self.transport_type = data[29]
        self.command_spec_info = data[32:40]
        self.transport_type_spec_info = data[40:42]


def nvme_smart_decode(data):
    result = {}
    decode_bits(data, nvme_smart_bit_mask, result)
    return result

def nvme_id_ctrl_decode(data):
    result = {}
    decode_bits(data, nvme_id_ctrl_bit_mask, result)
    ## power state
    for i in range(32):
        key = "PSD%s" % i
        _offset = 2048 + 32*i
        _data = data[_offset:(_offset+32)]
        power_state = {}
        decode_bits(_data, nvme_id_ctrl_ps_bit_mask, power_state)
        if power_state.get("MP") != b'\x00\x00':
            result[key] = power_state
    return result

def nvme_id_ns_decode(data):
    result = {}
    decode_bits(data, nvme_id_ns_bit_mask, result)
    ## lba format
    for i in range(16):
        key = "LBAF%s" % i
        _offset = 128 + 4*i
        _data = data[_offset:(_offset+4)]
        lba_format = {}
        decode_bits(_data, nvme_id_ns_lbaf_bit_mask, lba_format)
        if lba_format.get("LBADS") != b'\x00':
            result[key] = lba_format
    return result

def nvme_fw_slot_info_decode(data, check_invalid_frs=True):
    result = {}
    decode_bits(data, nvme_fw_slot_info_bit_mask, result)
    ##
    if check_invalid_frs:  
        for name in list(result.keys()):
            if "FRS" in name:
                if result[name] == b'\x00\x00\x00\x00\x00\x00\x00\x00':
                    result.pop(name)
    return result

def nvme_power_management_cq_decode(data):
    result = {}
    data = data.to_bytes(4, byteorder='little')
    decode_bits(data, nvme_power_management_cq_bit_mask, result)
    return result

def nvme_error_log_decode(data):
    error_log_entry_list = []
    offset = 0
    while True:
        if offset >= len(data):
            break
        #error_log_entry_list.insert(0, ErrorInfomationLogEntryUnit(data[offset:(offset+64)]))
        error_log_entry_list.append(ErrorInfomationLogEntryUnit(data[offset:(offset+64)]))
        offset += 64
    return error_log_entry_list