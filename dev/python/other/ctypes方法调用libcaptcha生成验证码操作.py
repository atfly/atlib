
#coding:utf-8

__all__=('captcha',)


import os, \
     ctypes,ctypes.util


LIBCAPTCHA_LIB = os.environ.get("LIBCAPTCHA_LIB",  \
                            ctypes.util.find_library("captcha")  \
                            )


libcaptcha = ctypes.CDLL( LIBCAPTCHA_LIB )

gifsize = ctypes.c_int.in_dll(libcaptcha,"gifsize").value

get_res = lambda res:''.join( chr( _ ) for _ in res )

#www.iplaypy.com

def captcha():
    l = ( ctypes.c_ubyte * 6 )()
    im = ( ctypes.c_ubyte * 70 * 200 )()
    gif = ( ctypes.c_ubyte * gifsize )()

    libcaptcha.captcha(im,l)
    libcaptcha.makegif(im,gif)
    return dict( gif = get_res(gif),l = get_res(l)[:-1] )