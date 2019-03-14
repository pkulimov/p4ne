import random
from ipaddress import IPv4Network, AddressValueError


class IPv4RandomNetwork(IPv4Network):
    def __init__(self, ip, mask):
        try:
            IPv4Network.__init__(self, (ip, mask), strict=False)
        except AddressValueError:
            print("Error generate network")

    def reqular(self):
        return not self.is_private

    def key_value(self):
        return (self.netmask, self.network_address)


def get_key(addr):
    return addr.key_value()

addresses = []
for i in range(50):
    addresses.append(IPv4RandomNetwork(random.randint(0x0B000000, 0xDF000000), random.randint(8, 24)))

for addr in addresses:
    print(addr, addr.reqular())

print("-"*30)
addresses = sorted(addresses, key=get_key)
for addr in addresses:
    print(addr)
