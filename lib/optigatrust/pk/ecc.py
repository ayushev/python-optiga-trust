# ============================================================================
# The MIT License
# 
# Copyright (c) 2018 Infineon Technologies AG
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE
# ============================================================================
from ctypes import *

from optigatrust.pk import EccKey
from optigatrust.util import KeyUsage, str2curve, KeyId, chip


def generate_keypair(curve='nistp256r1', keyid=KeyId.USER_PRIVKEY_1):
	_bytes = None
	api = chip.init()

	c = str2curve(curve, return_value=True)

	if keyid not in KeyId:
		raise Exception('Key ID should be selected of class KeyId')

	api.optiga_crypt_ecc_generate_keypair.argtypes = c_int, c_ubyte, c_bool, c_void_p, POINTER(c_ubyte), POINTER(c_ushort)
	api.optiga_crypt_ecc_generate_keypair.restype = c_int

	c_keyusage = c_ubyte(KeyUsage.KEY_AGREEMENT.value | KeyUsage.AUTHENTICATION.value)
	c_keyid = c_ushort(keyid.value)
	p = (c_ubyte * 100)()
	c_plen = c_ushort(len(p))

	ret = api.optiga_crypt_ecc_generate_keypair(c, c_keyusage, 0,  byref(c_keyid), p, byref(c_plen))

	pubkey = (c_ubyte * c_plen.value)()
	memmove(pubkey, p, c_plen.value)

	if ret == 0:
		return EccKey(pkey=bytes(pubkey), keyid=keyid, curve=str2curve(curve))
	else:
		return None