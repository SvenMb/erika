from courier_de import courier_de

with courier_de() as c:
    print(c.decode(b'\x20').hex())
    print(c.decode(b'\x81').hex())
    print(c.decode(b'\xc3').hex())
    print(c.decode(b'\x84').hex())
    print(c.decode(b'\xe2').hex())
    print(c.decode(b'\x82').hex())
    print(c.decode(b'\xac').hex())
    print(c.decode(b'\x20').hex())
