import os
import sys
import struct
import fcntl
# from pprint import pprint

# Linux ioctl call for /dev/random
RNDADDENTROPY = 1074287107
ENTROPY_BITS_PER_BYTE = 8

# http://man7.org/linux/man-pages/man4/random.4.html
# RNDADDENTROPY
#        Add some additional entropy to the input pool, incrementing
#        the entropy count.  This differs from writing to /dev/random
#        or /dev/urandom, which only adds some data but does not
#        increment the entropy count.  The following structure is used:
#
#            struct rand_pool_info {
#                int    entropy_count;
#                int    buf_size;
#                __u32  buf[0];
#            };

class RandomEntropyAdder:
    def __init__(self):
        self.rnd_file = os.open("/dev/random", os.O_WRONLY)

    def __enter__(self):
        return self

    def add_entropy(self, random_bytes):
        struct_format = 'ii%is' % len(random_bytes)
        entropy_bits = ENTROPY_BITS_PER_BYTE * len(random_bytes)
        rand_pool_info = struct.pack(struct_format, entropy_bits, len(random_bytes), random_bytes)
        fcntl.ioctl(self.rnd_file, RNDADDENTROPY, rand_pool_info)
        # pprint(rand_pool_info)

    def __exit__(self, exc_type, exc_value, traceback):
        os.close(self.rnd_file)
