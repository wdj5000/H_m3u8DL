import os
import platform
import sys
class util:
    def __init__(self):
        self.platform = platform.system()
        basePath = os.path.realpath(__file__).replace('Util.py','Tools/')
        if self.platform == 'Windows':
            self.ffmpegPath = basePath + 'ffmpeg.exe'
            self.mp4decryptPath = basePath + 'mp4decrypt_win.exe'
            self.youkudecryptPath = basePath + 'youkudecrypt.exe'
        elif self.platform == 'Linux':
            self.ffmpegPath = 'ffmpeg'
            self.mp4decryptPath = basePath + 'mp4decrypt_linux'
            self.youkudecryptPath = None
        else:
            self.ffmpegPath = None
            self.mp4decryptPath = None
            self.youkudecryptPath = None

    class RC4:
        """ RC4 加/解密工具

        This class implements the RC4 streaming cipher.

        Derived from http://cypherpunks.venona.com/archive/1994/09/msg00304.html
        '
        a = util().RC4(key=b"123456").crypt(data="user=969997051&password=123456".encode())
        print(a)
        b = util().RC4(key=b"123456").crypt(a)
        print(b)
        '
        """

        def __init__(self, key:bytes, streaming=False):
            assert (isinstance(key, (bytes, bytearray)))

            # key scheduling
            S = list(range(0x100))
            j = 0
            for i in range(0x100):
                j = (S[i] + key[i % len(key)] + j) & 0xff
                S[i], S[j] = S[j], S[i]
            self.S = S

            # in streaming mode, we retain the keystream state between crypt()
            # invocations
            if streaming:
                self.keystream = self._keystream_generator()
            else:
                self.keystream = None

        def crypt(self, data:bytes):
            """
            Encrypts/decrypts data (It's the same thing!)
            """
            assert (isinstance(data, (bytes, bytearray)))
            keystream = self.keystream or self._keystream_generator()  # self.keystream or self._keystream_generator()
            return bytes([a ^ b for a, b in zip(data, keystream)])

        def _keystream_generator(self):
            """
            Generator that returns the bytes of keystream
            """
            S = self.S.copy()
            x = y = 0
            while True:
                x = (x + 1) & 0xff
                y = (S[x] + y) & 0xff
                S[x], S[y] = S[y], S[x]
                i = (S[x] + S[y]) & 0xff
                yield S[i]



if __name__ == '__main__':
    a = util().RC4(key=b"123456").crypt(data="user=969997051&password=123456".encode())
    print(a)
    b = util().RC4(key=b"123456").crypt(a)
    print(b)
