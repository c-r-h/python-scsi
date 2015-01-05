# coding: utf-8

from pyscsi.utils.enum import Enum
from pyscsi.pyscsi.scsi_opcode import OpCodeMapper

spc_opcodes = {'ACCESS_CONTROL_IN': 0x86,
               'ACCESS_CONTROL_OUT': 0x87,
               'CHANGE_ALIASES': 0xa4,
               'EXTENDED_COPY': 0x83,
               'INQUIRY': 0x12,
               'LOG_SELECT': 0x4c,
               'LOG_SENSE': 0x4d,
               'MODE_SELECT_6': 0x15,
               'MODE_SELECT_10': 0x55,
               'MODE_SENSE_6': 0x1a,
               'MODE_SENSE_10': 0x5a,
               'PERSISTENT_RESERVE_IN': 0x5e,
               'PERSISTENT_RESERVE_OUT': 0x5f,
               'PREVENT_ALLOW_MEDIUM_REMOVAL': 0x1e,
               'READ_ATTRIBUTE': 0x8c,
               'READ_BUFFER': 0x3c,
               'READ_MEDIA_SERIAL_NUMBER': 0xab,
               'RECEIVE_COPY_RESULTS': 0x84,
               'RECEIVE_DIAGNOSTIC_RESULTS': 0x1c,
               'REPORT_ALIASES': 0xa3,
               'REPORT_DEVICE_IDENTIFIER': 0xa3,
               'REPORT_LUNS': 0xa0,
               'REPORT_PRIORITY': 0xa3,
               'REPORT_SUPPORTED_OPERATION_CODES': 0xa3,
               'REPORT_SUPPORTED_TASK_MANAGEMENT_FUNCTIONS': 0xa3,
               'REPORT_TARGET_PORT_GROUPS': 0xa3,
               'REPORT_TIMESTAMP': 0xa3,
               'REQUEST_SENSE': 0x03,
               'SEND_DIAGNOSTIC': 0x1d,
               'SET_DEVICE_IDENTIFIER': 0xa4,
               'SET_PRIORITY': 0xa4,
               'SET_TARGET_PORT_GROUPS': 0xa4,
               'SET_TIMESTAMP': 0xa4,
               'TEST_UNIT_READY': 0x00,
               'WRITE_ATTRIBUTE': 0x8d,
               'WRITE_BUFFER': 0x3b, }

spc_service_action = {'CHANGE_ALIASES': 0x0b,
                      'READ_MEDIA_SERIAL_NUMBER': 0x01,
                      'REPORT_ALIASES': 0x0b,
                      'REPORT_DEVICE_IDENTIFIER': 0x05,
                      'REPORT_PRIORITY': 0x0e,
                      'REPORT_SUPPORTED_OPERATION_CODES': 0x0c,
                      'REPORT_SUPPORTED_TASK_MANAGEMENT_FUNCTIONS': 0x0d,
                      'REPORT_TARGET_PORT_GROUPS': 0x0a,
                      'REPORT_TIMESTAMP': 0x0f,
                      'SET_DEVICE_IDENTIFIER': 0x06,
                      'SET_PRIORITY': 0x0e,
                      'SET_TARGET_PORT_GROUPS': 0x0a,
                      'SET_TIMESTAMP': 0x0f,
                      }

sbc_opcodes = {'ACCESS_CONTROL_IN': 0x86,
               'ACCESS_CONTROL_OUT': 0x87,
               'CHANGE_ALIASES': 0xa4,
               'COMPARE_AND_WRITE': 0x89,
               'EXTENDED_COPY': 0x83,
               'FORMAT_UNIT': 0x04,
               'GET_LBA_STATUS': 0x9e,
               'INQUIRY': 0x12,
               'LOG_SELECT': 0x4c,
               'LOG_SENSE': 0x4d,
               'MAINTENANCE_IN': 0xa3,
               'MAINTENANCE_OUT': 0xa4,
               'MODE_SELECT_6': 0x15,
               'MODE_SELECT_10': 0x55,
               'MODE_SENSE_6': 0x1a,
               'MODE_SENSE_10': 0x5a,
               'ORWRITE_16': 0x8b,
               'ORWRITE_32': 0x7f,
               'PERSISTENT_RESERVE_IN': 0x5e,
               'PERSISTENT_RESERVE_OUT': 0x5f,
               'PRE_FETCH_10': 0x34,
               'PRE_FETCH_16': 0x90,
               'PREVENT_ALLOW_MEDIUM_REMOVAL': 0x1e,
               'READ_6': 0x08,
               'READ_10': 0x28,
               'READ_12': 0xa8,
               'READ_16': 0x88,
               'READ_32': 0x7f,
               'READ_ATTRIBUTE': 0x8c,
               'READ_BUFFER': 0x3c,
               'READ_CAPACITY_10': 0x25,
               'READ_CAPACITY_16': 0x9e,
               'READ_DEFECT_DATA_10': 0x37,
               'READ_DEFECT_DATA_12': 0xb7,
               'READ_LONG_10': 0x3e,
               'READ_LONG_16': 0x9e,
               'REASSIGN_BLOCKS': 0x07,
               'RECEIVE_COPY_RESULTS': 0x84,
               'RECEIVE_DIAGNOSTIC_RESULTS': 0x1c,
               'REDUNDANCY_GROUP_IN': 0xba,
               'REDUNDANCY_GROUP_OUT': 0xbb,
               'REPORT_REFERRALS': 0x9e,
               'REPORT_ALIASES': 0xa3,
               'REPORT_IDENTIFYING_INFORMATION': 0xa3,
               'REPORT_LUNS': 0xa0,
               'REPORT_PRIORITY': 0xa3,
               'REPORT_SUPPORTED_OPERATION_CODES': 0xa3,
               'REPORT_SUPPORTED_TASK_MANAGEMENT_FUNCTIONS': 0xa3,
               'REPORT_TARGET_PORT_GROUPS': 0xa3,
               'REQUEST_SENSE': 0x03,
               'SECURITY_PROTOCOL_IN': 0xa2,
               'SECURITY_PROTOCOL_OUT': 0xb5,
               'SEND_DIAGNOSTIC': 0x1d,
               'SET_IDENTIFYING_INFORMATION': 0xa4,
               'SET_PRIORITY': 0xa4,
               'SET_TARGET_PORT_GROUPS': 0xa4,
               'SPARE_IN': 0xbc,
               'SPARE_OUT': 0xbd,
               'START_STOP_UNIT': 0x1b,
               'SYNCHRONIZE_CACHE_10': 0x35,
               'SYNCHRONIZE_CACHE_16': 0x91,
               'TEST_UNIT_READY': 0x00,
               'UNMAP': 0x42,
               'VERIFY_10': 0x2f,
               'VERIFY_12': 0xaf,
               'VERIFY_16': 0x8f,
               'VERIFY_32': 0x7f,
               'VOLUME_SET_IN': 0xbe,
               'VOLUME_SET_OUT': 0xbf,
               'WRITE_6': 0xa0,
               'WRITE_10': 0x2a,
               'WRITE_12': 0xaa,
               'WRITE_16': 0x8a,
               'WRITE_32': 0x7f,
               'WRITE_AND_VERIFY_10': 0x2e,
               'WRITE_AND_VERIFY_12': 0xae,
               'WRITE_AND_VERIFY_16': 0x8e,
               'WRITE_AND_VERIFY_32': 0x7f,
               'WRITE_ATTRIBUTE': 0x8d,
               'WRITE_BUFFER': 0x3b,
               'WRITE_LONG_10': 0x3f,
               'WRITE_LONG_16': 0x9f,
               'WRITE_SAME_10': 0x41,
               'WRITE_SAME_16': 0x93,
               'WRITE_SAME_32': 0x7f,
               'XDREAD_10': 0x52,
               'XDREAD_32': 0x7f,
               'XDWRITE_10': 0x50,
               'XDWRITE_32': 0x7f,
               'XDWRITEREAD_10': 0x53,
               'XDWRITEREAD_32': 0x7f,
               'XPWRITE_10': 0x51,
               'XPWRITE_32': 0x7f,
               }

sbc_service_action = {'CHANGE_ALIASES': 0x0b,
                      'GET_LBA_STATUS': 0x12,
                      'ORWRITE_32': 0x000e,
                      'READ_32': 0x0009,
                      'READ_CAPACITY_16': 0x10,
                      'READ_LONG_16': 0x11,
                      'REPORT_REFERRALS': 0x13,
                      'REPORT_ALIASES': 0x0b,
                      'REPORT_IDENTIFYING_INFORMATION': 0x05,
                      'REPORT_PRIORITY': 0x0e,
                      'REPORT_SUPPORTED_OPERATION_CODES': 0x0c,
                      'REPORT_SUPPORTED_TASK_MANAGEMENT_FUNCTIONS': 0x0d,
                      'REPORT_TARGET_PORT_GROUPS': 0x0a,
                      'SET_IDENTIFYING_INFORMATION': 0x06,
                      'SET_PRIORITY': 0x0e,
                      'SET_TARGET_PORT_GROUPS': 0x0a,
                      'VERIFY_32': 0x000a,
                      'WRITE_32': 0x000b,
                      'WRITE_AND_VERIFY_32': 0x000c,
                      'WRITE_LONG_16': 0x11,
                      'WRITE_SAME_32': 0x000d,
                      'XDREAD_32': 0x0003,
                      'XDWRITE_32': 0x0004,
                      'XDWRITEREAD_32': 0x0007,
                      'XPWRITE_32': 0x0006,
                      }

ssc_opcodes = {'ACCESS_CONTROL_IN': 0x86,
               'ACCESS_CONTROL_OUT': 0x87,
               'CHANGE_ALIASES': 0xa4,
               'ERASE_16': 0x93,
               'EXTENDED_COPY': 0x83,
               'FORMAT_MEDIUM': 0x04,
               'INQUIRY': 0x12,
               'LOAD_UNLOAD': 0x1b,
               'LOCATE_16': 0x92,
               'LOG_SELECT': 0x4c,
               'LOG_SENSE': 0x4d,
               'MODE_SELECT_6': 0x15,
               'MODE_SELECT_10': 0x55,
               'MODE_SENSE_6': 0x1a,
               'MODE_SENSE_10': 0x5a,
               'MOVE_MEDIUM_ATTACHED': 0xa7,
               'PERSISTENT_RESERVE_IN': 0x5e,
               'PERSISTENT_RESERVE_OUT': 0x5f,
               'PREVENT_ALLOW_MEDIUM_REMOVAL': 0x1e,
               'READ_6': 0x08,
               'READ_16': 0x88,
               'READ_ATTRIBUTES': 0x8c,
               'READ_BLOCK_LIMITS': 0x05,
               'READ_BUFFER': 0x3c,
               'READ_ELEMENT_STATUS_ATTACHED': 0xb4,
               'READ_POSITION': 0x34,
               'READ_REVERSE_6': 0x0f,
               'READ_REVERSE_16': 0x81,
               'RECEIVE_COPY_RESULTS': 0x84,
               'RECEIVE_DIAGNOSTIC_RESULTS': 0x1c,
               'RECOVER_BUFFERED_DATA': 0x14,
               'REPORT_ALIAS': 0xa3,
               'REPORT_DENSITY_SUPPORT': 0x44,
               'REPORT_DEVICE_IDENTIFIER': 0xa3,
               'REPORT_LUNS': 0xa0,
               'REPORT_SUPPORTED_OPERATION_CODES': 0xa3,
               'REQUEST_SENSE': 0x03,
               'REPORT_TARGET_PORT_GROUPS': 0xa3,
               'REWIND': 0x01,
               'SEND_DIAGNOSTIC': 0x1d,
               'SET_CAPACITY': 0x0b,
               'SET_DEVICE_IDENTIFIER': 0xa4,
               'SET_TARGET_PORT_GROUPS': 0xa4,
               'SPACE_6': 0x11,
               'SPACE_16': 0x91,
               'TEST_UNIT_READY': 0x00,
               'VERIFY_6': 0x13,
               'VERIFY_16': 0x8f,
               'WRITE_6': 0x0a,
               'WRITE_16': 0x8a,
               'WRITE_ATTRIBUTE': 0x8d,
               'WRITE_BUFFER': 0x3b,
               'WRITE_FILEMARKS_6': 0x10,
               'WRITE_FILEMARKS_16': 0x80,
               }

ssc_service_action = {'CHANGE_ALIASES': 0x0b,
                      'REPORT_ALIAS': 0x0b,
                      'REPORT_DEVICE_IDENTIFIER': 0x05,
                      'REPORT_SUPPORTED_OPERATION_CODES': 0x0c,
                      'REPORT_TARGET_PORT_GROUPS': 0x0a,
                      'SET_DEVICE_IDENTIFIER': 0x06,
                      'SET_TARGET_PORT_GROUPS': 0x0a,

                      }

opcodes = {'INQUIRY': 0x12,
           'MODE_SENSE_6': 0x1a,
           'MOVE_MEDIUM': 0xa5,
           'READ_10': 0x28,
           'READ_12': 0xa8,
           'READ_16': 0x88,
           'READ_CAPACITY_10': 0x25,
           'READ_ELEMENT_STATUS': 0xb8,
           'SERVICE_ACTION_IN': 0x9e,
           'TEST_UNIT_READY': 0x00,
           'WRITE_10': 0x2a,
           'WRITE_12': 0xaa,
           'WRITE_16': 0x8a,
           'WRITE_SAME_10': 0x41,
           'WRITE_SAME_16': 0x93,
           }

OPCODE = Enum(opcodes)

service_action_ins = {'READ_CAPACITY_16': 0x10,
                      'GET_LBA_STATUS': 0x12, }

SERVICE_ACTION_IN = Enum(service_action_ins)

scsi_status = {'GOOD': 0x00,
               'CHECK_CONDITION': 0x02,
               'CONDITIONS_MET': 0x04,
               'BUSY': 0x08,
               'RESERVATION_CONFLICT': 0x18,
               'TASK_SET_FULL': 0x28,
               'ACA_ACTIVE': 0x30,
               'TASK_ABORTED': 0x40,
               'SGIO_ERROR': 0xff, }

SCSI_STATUS = Enum(scsi_status)


class SPC(OpCodeMapper):

    def __init__(self):
        OpCodeMapper.__init__(self, spc_opcodes, spc_service_action)


class SBC(OpCodeMapper):

    def __init__(self):
        OpCodeMapper.__init__(self, sbc_opcodes, sbc_service_action)


class SSC(OpCodeMapper):

    def __init__(self):
        OpCodeMapper.__init__(self, ssc_opcodes, ssc_service_action)