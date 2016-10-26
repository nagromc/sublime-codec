import codecs

def punycode_encode(s):
    return codecs.encode(s, 'punycode').decode('UTF-8')

def punycode_decode(s):
    return codecs.decode(s, 'punycode')

def idna_encode(s):
    return codecs.encode(s, 'idna').decode('UTF-8')

def idna_decode(s):
    return codecs.decode(bytearray(s, 'utf8'), 'idna')
