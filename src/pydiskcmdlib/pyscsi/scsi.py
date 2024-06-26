# SPDX-FileCopyrightText: 2022 The pydiskcmd Authors
#
# SPDX-License-Identifier: LGPL-2.1-or-later
from pyscsi.pyscsi.scsi import SCSI as _SCSI
from pydiskcmdlib.pyscsi.scsi_cdb_logsense import LogSense
from pydiskcmdlib.pyscsi.scsi_cdb_synchronizecache import SynchronizeCache10,SynchronizeCache16
from pydiskcmdlib.pyscsi.scsi_cdb_SecurityProtocolIn import SecurityProtocolIn
from pydiskcmdlib.pyscsi.scsi_cdb_passthru import CDBPassthru
from pydiskcmdlib.pyscsi.scsi_cdb_receivediagnosticresults import ReceiveDiagnosticResults # noqa
from pydiskcmdlib.pyscsi.scsi_cdb_writebuffer import WriteBuffer


class SCSI(_SCSI):
    def __init__(self, 
                 dev,
                 blocksize=0):
        super(SCSI, self).__init__(dev, blocksize=blocksize)
        # auto detect blocksize
        if self._blocksize == 0:
            cap = self.readcapacity16().result
            self._blocksize = cap["block_length"]

    def __del__(self):
        if self.device:
            self.device.close()

    def cdb_passthru(self, raw_cdb, dataout=b'', datain_alloclen=0):
        """
        Returns a CDBPassthru Instance
        
        :param raw_cdb: a CDB Format bytes
        :param dataout_alloclen: the data_out buffer
        :param datain_alloclen: integer representing the size of the data_in buffer
        """
        cmd = CDBPassthru(raw_cdb, dataout=dataout, datain_alloclen=datain_alloclen)
        self.execute(cmd)
        return cmd

    def logsense(self, page_code, **kwargs):
        """
        Returns a LogSense Instance

        :param page_code:  The page requested
        :param kwargs: a dict with key/value pairs
                       sub_page_code = 0, Requested subpage
                       sp = 0, 
                       pc = 0, 
                       parameter = 0, 
                       alloclen = 512, 
                       control = 0
        :return: a LogSense instance
        """
        opcode = self.device.opcodes.LOG_SENSE
        cmd = LogSense(opcode, page_code, **kwargs)
        self.execute(cmd)
        cmd.unmarshall()
        return cmd

    def synchronizecache10(self, lba, block_number, **kwargs):
        """
        Returns a synchronizecache10 Instance

        :param lba:  The target LBA address
        :param block_number:  LBA length to sync cache
        :param kwargs: a dict with key/value pairs
                       passthrough to scsi_cdb_synchronizecache.SynchronizeCache10
        :return: a synchronizecache10 instance
        """
        opcode = self.device.opcodes.SYNCHRONIZE_CACHE_10
        cmd = SynchronizeCache10(opcode, lba, block_number, **kwargs)
        self.execute(cmd)
        return cmd

    def synchronizecache16(self, lba, block_number, **kwargs):
        """
        Returns a synchronizecache16 Instance

        :param lba:  The target LBA address
        :param block_number:  LBA length to sync cache
        :param kwargs: a dict with key/value pairs
                       passthrough to scsi_cdb_synchronizecache.SynchronizeCache16
        :return: a synchronizecache10 instance
        """
        opcode = self.device.opcodes.SYNCHRONIZE_CACHE_16
        cmd = SynchronizeCache16(opcode, lba, block_number, **kwargs)
        self.execute(cmd)
        return cmd

    def security_protocol_in(self, security_protocol, security_protocol_sp, alloc, **kwargs):
        """
        Returns a LogSense Instance

        :param security_protocol: a blocksize
        :param security_protocol_sp: Logical Block Address
        :param alloc: number of block
        :param kwargs: a dict with key/value pairs
                       passthrough to scsi_cdb_SecurityProtocolIn.SecurityProtocolIn
        :return: a security_protocol_in instance
        """
        opcode = self.device.opcodes.SECURITY_PROTOCOL_IN
        cmd = SecurityProtocolIn(opcode, security_protocol, security_protocol_sp, alloc, **kwargs)
        self.execute(cmd)
        return cmd

    def write_buffer(self, mode, mode_spec, buffer_id, buffer_offset, para_list_length, data=None, control=0):
        opcode = self.device.opcodes.WRITE_BUFFER
        cmd = WriteBuffer(opcode, mode, mode_spec, buffer_id, buffer_offset, para_list_length, data=data, control=control)
        self.execute(cmd)
        return cmd
