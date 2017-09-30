
class EncodePasswd(object):
    def __init__(self, passwd=None, verifycode=None):
        self.passwd = passwd
        self.verifycode = verifycode
        self.hexcase = 1
        self.b64pad = ''
        self.chrsz = 8
        self.mode = 32

    def str2binl(self, D):
        C = []
        A = (1<<self.chrsz) - 1
        for B in range(0, len(D)*self.chrsz, self.chrsz):
            if len(C) == (B>>5): C.append(0)
            C[B>>5] |= (ord(D[B/self.chrsz])&A)<<(B%32)
        return C

    def binl2hex(self, C):
        B = "0123456789abcdef"
        if self.hexcase: 
            B = "0123456789ABCDEF"
        D = ''
        for A in range(0, len(C)*4, 1):
            D += B[(C[A>>2]>>((A%4)*8+4))&15] + B[(C[A>>2]>>((A%4)*8))&15]
        return D
        
    def md5(self, A):
        return self.hex_md5(A)

    def hex_md5(self, A): 
        return self.binl2hex(self.core_md5(self.str2binl(A), len(A)*self.chrsz))
    
    def str_md5(self, A):
        return self.binl2str(self.core_md5(self.str2binl(A), len(A)*self.chrsz))
    
    def hex_hmac_md5(self, A, B):
        return self.binl2hex(self.core_hmac_md5(A, B))
        
    def b64_hmac_md5(self, A, B):
        return binl2b64(core_hmac_md5(A, B))
    
    def str_hmac_md5(self, A, B):
        return self.binl2str(self.core_hmac_md5(A, B))
       
    def md5_vm_test(self):
        return self.hex_md5('abc') == '900150983cd24fb0d6963f7d28e17f72'
    
    # this is equvalent of >>> in js
    def rsl(self, A, B):
        return (A & 0xFFFFFFFFL) >> B
    
    def jsArraySet(self, list, index, value):
        if index < 0: return
        if len(list) > index:
            list[index] = value
        else:
            for i in range(index-len(list)):
                list.append(0)
            list.append(value)
    def jsArrayGet(self, list, index):
        if len(list) > index:
            return list[index]
        else:
            return 0
    
    def core_md5(self, K, F):
        #K[F>>5] |= 128<<((F)%32)
        self.jsArraySet(K, F>>5, self.jsArrayGet(K, F>>5)|(128<<(F%32)))
        #K[(self.rsl(F+64, 9)<<4)+14] = F
        self.jsArraySet(K, (self.rsl(F+64, 9)<<4)+14, F)
        J=1732584193;
        I=-271733879;
        H=-1732584194;
        G=271733878;
        
        for C in range(0, len(K), 16):
            E=J;
            D=I;
            B=H;
            A=G;
            J=self.md5_ff(J,I,H,G,self.jsArrayGet(K, C+0),7,-680876936);
            G=self.md5_ff(G,J,I,H,self.jsArrayGet(K, C+1),12,-389564586);
            H=self.md5_ff(H,G,J,I,self.jsArrayGet(K, C+2),17,606105819);
            I=self.md5_ff(I,H,G,J,self.jsArrayGet(K, C+3),22,-1044525330);
            J=self.md5_ff(J,I,H,G,self.jsArrayGet(K, C+4),7,-176418897);
            G=self.md5_ff(G,J,I,H,self.jsArrayGet(K, C+5),12,1200080426);
            H=self.md5_ff(H,G,J,I,self.jsArrayGet(K, C+6),17,-1473231341);
            I=self.md5_ff(I,H,G,J,self.jsArrayGet(K, C+7),22,-45705983);
            J=self.md5_ff(J,I,H,G,self.jsArrayGet(K, C+8),7,1770035416);
            G=self.md5_ff(G,J,I,H,self.jsArrayGet(K, C+9),12,-1958414417);
            H=self.md5_ff(H,G,J,I,self.jsArrayGet(K, C+10),17,-42063);
            I=self.md5_ff(I,H,G,J,self.jsArrayGet(K, C+11),22,-1990404162);
            J=self.md5_ff(J,I,H,G,self.jsArrayGet(K, C+12),7,1804603682);
            G=self.md5_ff(G,J,I,H,self.jsArrayGet(K, C+13),12,-40341101);
            H=self.md5_ff(H,G,J,I,self.jsArrayGet(K, C+14),17,-1502002290);
            I=self.md5_ff(I,H,G,J,self.jsArrayGet(K, C+15),22,1236535329);
            J=self.md5_gg(J,I,H,G,self.jsArrayGet(K, C+1),5,-165796510);
            G=self.md5_gg(G,J,I,H,self.jsArrayGet(K, C+6),9,-1069501632);
            H=self.md5_gg(H,G,J,I,self.jsArrayGet(K, C+11),14,643717713);
            I=self.md5_gg(I,H,G,J,self.jsArrayGet(K, C+0),20,-373897302);
            J=self.md5_gg(J,I,H,G,self.jsArrayGet(K, C+5),5,-701558691);
            G=self.md5_gg(G,J,I,H,self.jsArrayGet(K, C+10),9,38016083);
            H=self.md5_gg(H,G,J,I,self.jsArrayGet(K, C+15),14,-660478335);
            I=self.md5_gg(I,H,G,J,self.jsArrayGet(K, C+4),20,-405537848);
            J=self.md5_gg(J,I,H,G,self.jsArrayGet(K, C+9),5,568446438);
            G=self.md5_gg(G,J,I,H,self.jsArrayGet(K, C+14),9,-1019803690);
            H=self.md5_gg(H,G,J,I,self.jsArrayGet(K, C+3),14,-187363961);
            I=self.md5_gg(I,H,G,J,self.jsArrayGet(K, C+8),20,1163531501);
            J=self.md5_gg(J,I,H,G,self.jsArrayGet(K, C+13),5,-1444681467);
            G=self.md5_gg(G,J,I,H,self.jsArrayGet(K, C+2),9,-51403784);
            H=self.md5_gg(H,G,J,I,self.jsArrayGet(K, C+7),14,1735328473);
            I=self.md5_gg(I,H,G,J,self.jsArrayGet(
369a
K, C+12),20,-1926607734);
            J=self.md5_hh(J,I,H,G,self.jsArrayGet(K, C+5),4,-378558);
            G=self.md5_hh(G,J,I,H,self.jsArrayGet(K, C+8),11,-2022574463);
            H=self.md5_hh(H,G,J,I,self.jsArrayGet(K, C+11),16,1839030562);
            I=self.md5_hh(I,H,G,J,self.jsArrayGet(K, C+14),23,-35309556);
            J=self.md5_hh(J,I,H,G,self.jsArrayGet(K, C+1),4,-1530992060);
            G=self.md5_hh(G,J,I,H,self.jsArrayGet(K, C+4),11,1272893353);
            H=self.md5_hh(H,G,J,I,self.jsArrayGet(K, C+7),16,-155497632);
            I=self.md5_hh(I,H,G,J,self.jsArrayGet(K, C+10),23,-1094730640);
            J=self.md5_hh(J,I,H,G,self.jsArrayGet(K, C+13),4,681279174);
            G=self.md5_hh(G,J,I,H,self.jsArrayGet(K, C+0),11,-358537222);
            H=self.md5_hh(H,G,J,I,self.jsArrayGet(K, C+3),16,-722521979);
            I=self.md5_hh(I,H,G,J,self.jsArrayGet(K, C+6),23,76029189);
            J=self.md5_hh(J,I,H,G,self.jsArrayGet(K, C+9),4,-640364487);
            G=self.md5_hh(G,J,I,H,self.jsArrayGet(K, C+12),11,-421815835);
            H=self.md5_hh(H,G,J,I,self.jsArrayGet(K, C+15),16,530742520);
            I=self.md5_hh(I,H,G,J,self.jsArrayGet(K, C+2),23,-995338651);
            J=self.md5_ii(J,I,H,G,self.jsArrayGet(K, C+0),6,-198630844);
            G=self.md5_ii(G,J,I,H,self.jsArrayGet(K, C+7),10,1126891415);
            H=self.md5_ii(H,G,J,I,self.jsArrayGet(K, C+14),15,-1416354905);
            I=self.md5_ii(I,H,G,J,self.jsArrayGet(K, C+5),21,-57434055);
            J=self.md5_ii(J,I,H,G,self.jsArrayGet(K, C+12),6,1700485571);
            G=self.md5_ii(G,J,I,H,self.jsArrayGet(K, C+3),10,-1894986606);
            H=self.md5_ii(H,G,J,I,self.jsArrayGet(K, C+10),15,-1051523);
            I=self.md5_ii(I,H,G,J,self.jsArrayGet(K, C+1),21,-2054922799);
            J=self.md5_ii(J,I,H,G,self.jsArrayGet(K, C+8),6,1873313359);
            G=self.md5_ii(G,J,I,H,self.jsArrayGet(K, C+15),10,-30611744);
            H=self.md5_ii(H,G,J,I,self.jsArrayGet(K, C+6),15,-1560198380);
            I=self.md5_ii(I,H,G,J,self.jsArrayGet(K, C+13),21,1309151649);
            J=self.md5_ii(J,I,H,G,self.jsArrayGet(K, C+4),6,-145523070);
            G=self.md5_ii(G,J,I,H,self.jsArrayGet(K, C+11),10,-1120210379);
            H=self.md5_ii(H,G,J,I,self.jsArrayGet(K, C+2),15,718787259);
            I=self.md5_ii(I,H,G,J,self.jsArrayGet(K, C+9),21,-343485551);
            J=self.safe_add(J,E);
            I=self.safe_add(I,D);
            H=self.safe_add(H,B);
            G=self.safe_add(G,A)
            
        if self.mode == 16:
            return [I, H]
        else:
            return [J, I, H, G]
            
    def md5_cmn(self, F, C, B, A, E, D):
        return self.safe_add(self.bit_rol(self.safe_add(self.safe_add(C, F), self.safe_add(A, D)), E), B)
        
    def md5_ff(self, C, B,G, F,A,E,D):
        return self.md5_cmn((B&G)|((~B)&F), C, B, A, E, D)
        
    def md5_gg(self, C,B,G,F,A,E,D):
        return self.md5_cmn((B&F)|(G&(~F)),C,B,A,E,D)
        
    def md5_hh(self, C,B,G,F,A,E,D):
        return self.md5_cmn(B^G^F, C,B,A,E,D)
        
    def md5_ii(self,C,B,G,F,A,E,D):
        return self.md5_cmn(G^(B|(~F)),C,B,A,E,D)
    
    def core_hmac_md5(self, C, F):
        E = self.str2binl(C)
        if len(E) > 16:
            E = self.core_md5(E,len(C)*self.chrsz)
        A = [None]*16
        D = [None]*16
        for B in range(0, 16):
            A[B] = E[B]^909522486
            D[B] = E[B]^1549556828
        G = self.core_md5(A+self.str2binl(F), 512+len(F)*self.chrsz)
        return self.core_md5(D+G, 512+128)    
    
    def safe_add(self, A,D):
        C = (A&65535)+(D&65535)
        B = (A>>16)+(D>>16)+(C>>16)
        return (B<<16)|(C&65535)

    def bit_rol(self, A, B):
        return (A<<B)|self.rsl(A, 32-B)
        
    def binl2str(self, C):
        D = ''
        A = (1<<self.chrsz)-1
        for B in range(0, len(C)*32, self.chrsz):
            D += chr(self.rsl(C[B>>5], B%32)&A)
        return D
        
    def binl2b64(self, D):
        C="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
        F = ''
        for B in range(0, len(D)*4, 3):
            E=(((D[B>>2]>>8*(B%4))&255)<<16)|(((D[B+1>>2]>>8*((B+1)%4))&255)<<8)|((D[B+2>>2]>>8*((B+2)%4))&255)
            for A in range(0, 4):
                if B*8+A*6>len(D)*32:
                    F += self.b64pad
                else:
                    F += C[(E>>6*(3-A))&63]
        return F

#www.iplaypy.com

    def hexchar2bin(self,str):
        arr = []
        for i in range(0, len(str) , 2):
            arr.append("\\x" + str[i:i+2])
        arr="".join(arr)
        exec("temp = '" + arr + "'");
        return temp

    def md5_3(self, B):
        hash = self.core_md5(self.str2binl(B), len(B)*self.chrsz)
        hash = self.core_md5(hash, 16*self.chrsz)
        hash = self.core_md5(hash, 16*self.chrsz)
        return self.binl2hex(hash)
