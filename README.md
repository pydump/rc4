# Package rc4

Package rc4 exposes the RC4 algorithm.

```sh
pip3 install git+https://github.com/pydump/rc4.git
```

- [Examples](#Examples)

# Examples

Stream encrypting:

```py
import rc4

c = rc4.Cipher(b'cipher')
with open('src', 'rb') as src, open('dst', 'wb') as dst:
    c.stream(src, dst)
```

