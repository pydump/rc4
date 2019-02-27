import rc4


def test_smoke():
    for k, src, dst in [
        [b'Key', b'Plaintext', bytes.fromhex('BBF316E8D940AF0AD3')],
        [b'Wiki', b'pedia', bytes.fromhex('1021BF0420')],
        [b'Secret', b'Attack at dawn', bytes.fromhex(
            '45A01F645FC35B383552544B9BF5')]
    ]:
        c = rc4.Cipher(k)
        r = list(range(len(src)))
        c.crypto(src, r)
        assert bytes(r) == dst
