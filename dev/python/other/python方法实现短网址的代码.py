
import string

def rebase(i, frombase=None, tobase=None, fromalphabet=None, toalphabet=None, resize=1, too_big=40000, debug=False):
    ''' if frombase is not specified, it is guessed from the type and/or char in i with highest ord.
        tobase defaults to [10, 2][frombase == 10].
        the alphabets are map(chr, range(256)) if its base is between 62 and 255;
        otherwise, string.digits+string.letters.
        always returns a string which is also valid input.
        valid bases are ints in range(-256, 257).
        alphabets must be subscriptable, and can only contain str's.
        invalid tobases are replied with 'why?'; rebase('why?') == '217648673'.
        returned string is zfilled to the next largest multiple of resize
    '''

    if frombase == None:
        if isinstance(i, (int, long)):
            frombase = 10
        elif isinstance(i, str):
            a = str(i)
            if any([(chr(x) in a) for x in range(ord('0')) + range(58, 65) + range(91, 97) + range(123, 256)]):
                frombase = max(map(ord, a)) + 1
            else:
                frombase = max(map((string.digits + string.letters).index, a)) + 1

    if tobase == None:
        tobase = [10, 2][frombase == 10]
    # got bases, ensuring that everything is an int
    tobase = int(tobase)
    frombase = int(frombase)
    abstobase = abs(tobase)
    absfrombase = abs(frombase)


    if absfrombase in [0, 1]:
        i = len(str(i))

    elif 2 <= frombase <= 36:
        # may be difficult to translate to C
        i = int(str(i), frombase)

    else:
        i = str(i)
        n = 0
        if fromalphabet == None:
            if 62 <= absfrombase <= 256:
                fromalphabet = map(chr, range(256))
            else:
                fromalphabet = string.digits + string.letters
        fromalphabet = fromalphabet[:absfrombase]


        for j in range(len(i)):
            n += (frombase ** j) * fromalphabet.index(i[-1-j])
        i = n
    # got ints, converting to tobase
    if debug: print 'converting %d from base %d to %d' % (i, frombase, tobase)

    if abstobase in [0, 1]:
        return '0' * ((i > 0) and int(i) or 0)
    elif abstobase > 256:
        return 'why?'
    # if execution gets here, we might want the result to be zfilled to a multiple of resize
    r = ''
    if tobase == 10:
        r = str(i)

4000
    else:
        if i < 0:
            print 'negative',
            i = -i
        if toalphabet is None:
            if 62 <= abstobase <= 256:
                toalphabet = map(chr, range(abstobase))
            else:
                toalphabet = (string.digits + string.letters)[:abstobase]
        if tobase < 0:
            i = -i
        j = 0
        while i != 0:
            r = toalphabet[i % tobase] + r
            i /= tobase
            j += 1
            if j >= too_big: raise "call again; set too_big bigger"

#www.iplaypy.com

    if resize > 1:
        if 62 <= abstobase <= 256:
            r = toalphabet[0] * (resize - (len(r) % resize)) + r
        else:
            r = r.zfill(len(r) + resize - (len(r) % resize))
    return r

from pymongo import Connection
from rebase import rebase

def short_url(url, size):
    '''
        shorten url example
    '''
    ## 62 charaters
    CHAR62 = list('0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    ## mapping chr(?) to 62-base charaters
    re_dic = {}
    j = 0
    for i in CHAR62:
        re_dic.update({map(chr, range(62))[j]: i})
        j += 1
    # another way to get it 
    '''
    re_dic = {'\x01': '1', '\x00': '0', '\x03': '3', '\x02': '2', '\x05': '5',
     '\x04': '4', '\x07': '7', '\x06': '6', '\t': '9', '\x08': '8', '\x0b': 'b',
     '\n': 'a', '\r': 'd', '\x0c': 'c', '\x0f': 'f', '\x0e': 'e', '\x11': 'h',
     '\x10': 'g', '\x13': 'j', '\x12': 'i', '\x15': 'l', '\x14': 'k', '\x17': 'n',
     '\x16': 'm', '\x19': 'p', '\x18': 'o', '\x1b': 'r', '\x1a': 'q', '\x1d': 't',
     '\x1c': 's', '\x1f': 'v', '\x1e': 'u', '!': 'x', ' ': 'w', '#': 'z', '"': 'y',
     '%': 'B', '$': 'A', "'": 'D', '&': 'C', ')': 'F', '(': 'E', '+': 'H', '*': 'G',
     '-': 'J', ',': 'I', '/': 'L', '.': 'K', '1': 'N', '0': 'M', '3': 'P', '2': 'O',
     '5': 'R', '4': 'Q', '7': 'T', '6': 'S', '9': 'V', '8': 'U', ';': 'X', ':': 'W',
     '=': 'Z', '<': 'Y'}
    
    '''
    
    # for test only, connecting to mongoDB
    # default host->'localhost' port->'27017'
    conn = Connection()
    db = conn['test']
    coll = db['short_url']
    
    _one = coll.find_one({'url': url})
    # if the url already existes in the database
    # return it directly
    if _one:
        res_final =  str(_one['tiny'])
    else:
        uid = coll.insert({}) # insert a empty dict and get a unique id
        _id = str(uid) # mongoDB returned a 24-charater id object
        ## rebase 36-base to 62-base
        re_str = rebase(_id, frombase=16, tobase=62)
        ## use re_dic to convert re_str to 62-base charaters
        res = ''.join([re_dic[x] for x in list(re_str)])
        # what you need just a slice, i.e. 6 charaters
        si = 0 - int(size)
        res_final = res[si:]
        # find the document and update it
        coll.find_and_modify(query={'_id': uid}, update={'tiny': res_final, 'url': url})
    
    return res_final

## 
# map(chr, range(48,58)) == ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# or [str(i) for i in range(10)]
# map(chr, range(65,91)) == ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# map(chr, range(97,123)) == ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#
# example: 36-base to 64-base
#     char36 = 'u38ki9'
#     lis36 = map(chr, range(48,58)) + map(chr, range(97, 123))
#     map36 = any2any_map(lis36, [str(i) for i in range(36)])
#     num_lis = [int(map36[i]) for i in char36]
#     num_lis.reverse()
#     dec = any2dec(num_lis, 36)
#     lis = [str(i) for i in dec2any(dec, 64, [])]
#     lis.reverse()
#     lis64 = lis36 + map(chr, range(65,91))
#     map64 = any2any_map([str(i) for i in range(64)], lis64)
#     out_lis = [map64[i] for i in lis]
#     char64 = ''.join(out_lis) #-> '1Iszjh'
##

def any2any_map(from_lis, to_lis):
    _dic = {}
    for k,v in zip(from_lis, to_lis):
        _dic.update({k: v})
    return _dic
    
def any2dec(num_lis, base):
    j = 0
    _dec = 0
    for n in num_lis:
        _dec += n * pow(base, j)
        j += 1
    return _dec
    
def dec2any(dec, base, lis=[]):
    if dec > 0:
        lis.append(dec%base)
        dec2any(dec//base, base, lis=lis)
    return lis

