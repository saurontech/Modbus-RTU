#!/usr/bin/env python3

import pymodbus
from pymodbus.pdu import ModbusRequest
from pymodbus.client.sync import ModbusSerialClient as ModbusClient
from pymodbus.transaction import ModbusRtuFramer

client = ModbusClient(method='rtu', port="/dev/ttyADV0", baudrate=115200, parity='N', timeout=0.5)
connection = client.connect()

read_vals  = client.read_holding_registers(0, 4, unit=1) # start_address, count, slave_id
#print(read_vals.registers)
value = ((f'Modbus error: {read_vals}') if read_vals.isError() else read_vals.registers)
print(read_vals.registers[0])
print(read_vals, read_vals.registers)


# write registers
# write  = client.write_register(1,425,unit=1)# address = 1, value to set = 425, slave ID = 1
