from pysnmp.hlapi import *

community = "public"
ipaddr = "10.31.70.107"
port = 161

snmp_object_1 = ObjectIdentity('SNMPv2-MIB', 'sysDescr', 0)
snmp_object_2 = ObjectIdentity('1.3.6.1.2.1.2.2.1.2')
snmp_objects = [snmp_object_1, snmp_object_2]

def snmpGetCmd(obj):
    result = getCmd(SnmpEngine(),
                CommunityData(community, mpModel=0),
                UdpTransportTarget((ipaddr, port)),
                ContextData(),
                ObjectType(ObjectIdentity(obj)))
    return result


def snmpNextCmd(obj):
    result = nextCmd(SnmpEngine(),
                CommunityData(community, mpModel=0),
                UdpTransportTarget((ipaddr, port)),
                ContextData(),
                ObjectType(ObjectIdentity(obj)),
                lexicographicMode=False)
    return result


def print_result(snmp_result):
    for res in snmp_result:
        print("+"*50)
        print(res[0], res[1], res[2])
        for bind in res[3]:
            print("-"*50)
            print(bind)


for obj in snmp_objects:
    print_result(snmpGetCmd(obj))
    print_result(snmpNextCmd(obj))
