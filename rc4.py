class KeySizeError(Exception):
    pass


class Cipher:
    def __init__(self, key):
        assert isinstance(key, bytes)
        self.s = list(range(256))
        self.i = 0
        self.j = 0
        self.key = key

        k = len(key)
        if k < 1 or k > 256:
            raise KeySizeError('crypto/rc4: invalid key size ' + str(k))

        j = 0
        for i in range(256):
            j = (j + self.s[i] + key[i % k]) % 256
            self.s[i], self.s[j] = self.s[j], self.s[i]

    def __str__(self):
        return f'rc4.Cipher(key={self.key})'

    def crypto(self, src, dst):
        i, j = self.i, self.j
        for k, v in enumerate(src):
            i = (i + 1) % 256
            j = (j + self.s[i]) % 256
            self.s[i], self.s[j] = self.s[j], self.s[i]
            dst[k] = v ^ self.s[(self.s[i] + self.s[j]) % 256] % 256
        self.i, self.j = i, j

    def stream(self, src, dst):
        c = 65536
        buf = list(range(c))
        while True:
            ctx = src.read(c)
            if not ctx:
                break
            n = len(ctx)
            self.crypto(ctx, buf)
            dst.write(bytes(buf[:n]))
