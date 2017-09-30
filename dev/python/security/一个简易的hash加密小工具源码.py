
#!/usr/bin/env python
#-*-encoding = utf-8-*-
# hasher.py

import sys
import hashlib
import linecache

def alglist():
    print """
    (1)MD5     (4)SHA256
    (2)SHA1    (5)SHA384
    (3)SHA224  (6)SHA512 """

class hasher(object):
    def single(self):
        try:
            alglist()
            alg = raw_input("Select an algorithm:")
            functions = {"1":hashlib.md5,"2":hashlib.sha1,'3':hashlib.sha224,'4':hashlib.sha256,'5':hashlib.sha384,'6':hashlib.sha512}
            if alg in functions.keys():
                hashob = functions[alg]()
                outfile = raw_input("Enter output file:")
                while 1:
                    word = raw_input("Enter string: ")
                    hashob.update(word)
                    hashword = hashob.hexdigest()
                    hashlst = open(outfile, 'a+')
                    hashlst.write(hashword + '\n')
                    print '[*] Output successful...'
                    raw_input("[*] Press Return to continue OR 'Ctrl-C' to Quit...")
            else:
                alglist()
                print "[*] Your input not found..."
                sys.exit(1)

        except KeyboardInterrupt:
#            main()
            raise
        except IOError:
            print "[*] Input file not found..."
            sys.exit(1)
#            hasher.single()
    def hashlist(self):
        try:
            alglist()
            alg = raw_input("Select an algorithm:")
            functions = {'1':hashlib.md5, '2':hashlib.sha1, '3':hashlib.sha224, '4':hashlib.sha256, '5':hashlib.sha384, '6':hashlib.sha512}
            if alg in functions.keys():
                hashob = functions[alg]()
                infile = raw_input("Enter input file:")
                outfile = raw_input("Enter output file:")
                count = len(open(infile).readlines())
                i = 1
                while i <= count + 1:
                    word = linecache.getline(infile,i)
                    hashob.update(word)
                    hashword = hashob.hexdigest()
                    outlist = open(outfile,'a++')
                    outlist.write(hashword+'\n')
                    i += 1
                print "[*]Output successful..."
                raw_input("Press enter to return to the main menu OR 'Ctrl-C' to Quit...")
                main()
            else:
                alglist()
                print "[*] Your input not found..."                                  
                sys.exit(1)
        except KeyboardInterrupt:
#            main()
            raise
        except IOError:
            print "[*] Input file not found..."
            sys.exit(1)
#            main()
    
def main():
    try:
        print """
        O))                      O))                                 
        O))        O))     O)))) O))        O))      O))    O)) O))  
        O) O)    O))  O)) O))    O) O)    O))  O)) O)   O))  O))  O))
        O))  O))O))   O))   O))) O))  O))O))   O))O))))) O)) O))  O))
        O)   O))O))   O))     O))O)   O)) O))  O))O)         O))  O))
        O))  O))  O)) O)))O)0)O))O))  O))     O))   O))))   O)))  O))
                                          O))        


        (1) Single Mode - Enter strings to be hashed one by one
        (2) List Mode - Input a text file of strings to be hashed"""

        mode = raw_input("Select a mode:")
        if mode == '1':
            hasher.single()
        elif mode == '2':
            hasher.hashlist()
        else:
            main()
    except KeyboardInterrupt:
        print "\n[*] Exiting..."
        sys.exit(1)


if __name__ == "__main__":
    hasher = hasher()
    main()
#www.iplaypy.com