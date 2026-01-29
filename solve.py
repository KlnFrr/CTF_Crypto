import binascii

c1 = bytes.fromhex("3e7355c9b4b5541961c42adf2e1b5ba3d803e10a52836c075870a1704c22ed03d05e5d133cb54bf32cf97e42")
c2 = bytes.fromhex("337801dcb3a41c1276c403db341140f09c0da438078976064935e5524926fc079c43574178fc09eb6dae312cdf0cc54b204db3fa71de7e11709f0115ee3fd307ad2f0a98a4c813dffe8e614b7e00107a64")
c3 = bytes.fromhex("266301c4e6b5075d749608cd330157fcd80ea46b418878130c70f247047dbb24f0767f1a74a31bfc26fb66298a4a835b6510eaf0619f2e467a8e0849f8338e5bac3918c1f9a6")

plaintext1 = b"Lettre de Galois a Auguste Chevalier, 1832."

keystream_list = []
for a, b in zip(c1, plaintext1):
    keystream_list.append(a ^ b)
keystream = bytes(keystream_list)

plaintext2_list = []
for i, c in enumerate(c2[:len(keystream)]):
    plaintext2_list.append(c ^ keystream[i])
plaintext2 = bytes(plaintext2_list)

print(plaintext2.decode(errors="replace"))


plaintext3_list = []
for i, c in enumerate(c3[:len(keystream)]):
    plaintext3_list.append(c ^ keystream[i])
plaintext3 = bytes(plaintext3_list)

print(plaintext3.decode())

known_plaintext1 = (
    b"An author never does more damage to his readers than "
    b"when he hides a difficulty."
)

keystream = bytes(a ^ b for a, b in zip(c2, known_plaintext1))
plaintext2 = bytes(
    c ^ keystream[i]
    for i, c in enumerate(c2[:len(keystream)])
)

print(plaintext2.decode(errors="replace"))

plaintext3 = bytes(
    c ^ keystream[i]
    for i, c in enumerate(c3[:len(keystream)])
)

print(plaintext3.decode(errors="replace"))
