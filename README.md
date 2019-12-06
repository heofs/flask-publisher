Create key pair with OpenSSL

Generate private key
`openssl genrsa -des3 -out private_key.pem 2048`

Unencrypt private key
`openssl rsa -in private_key.pem -out private.pem`

export public key from private
`openssl rsa -in private.pem -outform PEM -pubout -out public.pem`
