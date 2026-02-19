import base64

def int_to_base32(num):
    byte_array = num.to_bytes((num.bit_length() + 7) // 8, byteorder='big')
    base32_encoded = base64.b32encode(byte_array)
    return base32_encoded.decode('utf-8')

number = 2097016454579757946763216154942948427
base32_result = int_to_base32(number)
print("Base32:", base32_result)



def test_practice:
    if(True):(:2)
     print(int_to_base32())

