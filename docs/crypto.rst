Cryptography
============

Here are some examples for what you can do with this submodule

Generate random
---------------

::

    from optigatrust import crypto

    random_tuple = (8, 9, 15, 31, 33, 64, 128, 129, 255, 256)
    for n in random_tuple:
        crypto.random(n)

Generate a keypair (ECC, RSA)
------------------------------------

::

    from optigatrust import crypto
    from optigatrust import objects

    key_object = objects.ECCKey(0xe0f1)
    pkey, _ = crypto.generate_pair(key_object, curve='secp256r1')
    pkey, _ = crypto.generate_pair(key_object, curve='secp384r1')
    pkey, _ = crypto.generate_pair(key_object, curve='secp521r1')
    pkey, _ = crypto.generate_pair(key_object, curve='brainpoolp256r1')
    pkey, _ = crypto.generate_pair(key_object, curve='brainpoolp384r1')
    pkey, _ = crypto.generate_pair(key_object, curve='brainpoolp512r1')

    pkey, _ = crypto.generate_pair(key_object, curve='secp384r1', key_usage=['authentication', 'signature'])
    pkey, _ = crypto.generate_pair(key_object, curve='secp384r1', key_usage=['authentication', 'key_agreement', 'signature'])

    pkey, key = crypto.generate_pair(key_object=key_object, curve='secp256r1', export=True)

ECDSA Sign
----------

::

    from optigatrust import crypto
    from optigatrust import objects

    key_object = objects.ECCKey(0xe0f1)
    _, _ = crypto.generate_pair(key_object, curve='secp256r1')
    s = crypto.ecdsa_sign(key_object, 'Hello World')


PKCS1 v1.5 Sign
---------------

::

    from optigatrust import crypto
    from optigatrust import objects

    key_object = objects.RSAKey(0xe0fc)
    _, _ = crypto.generate_pair(key_object, key_size=1024)
    s = crypto.pkcs1v15_sign(key_object, 'Hello World')

HMAC
----

Key Dereviation (HKDF, TLS PRF)
-------------------------------

En-/Decryption (RSA, AES)
-------------------------

API
---


.. automodule:: optigatrust.crypto
   :members: random, generate_pair, ecdsa_sign, pkcs1v15_sign, ecdh, hmac, tls_prf, hkdf
