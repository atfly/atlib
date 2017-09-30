using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApplication4
{
    class Program
    {
        static void Main(string[] args)
        {
            string s1;
            string s2;

            SimilarString ss = new SimilarString();
            double p = 0;
            int n = 0;
            s1 = " 2000年在由华埠公司新成立的时代动力数码科技公司期间，对我国2代和3代移动和宽带通信技术进行 深入调查，对移动互联网技术现状及发展进行详细的论证技；对手机和掌上电脑PDA通过MODEM互连构成 移动终端设备，进行大量分析和测试；对国内外各种型号掌上电脑PDA的软硬件进行详细的分析论证，掌握适合 国内发展的软硬技术方案。";
            s2 = " 2000年在由华埠公司在由华埠公司新成立的时代动力数码我国2科技公司期间，对我国2代和3信技术代移动和宽带通信技术进行 深入调查，对移动互联新成立的时代动力数码我国2科技公司期间，对我国2代和3信技术代移动和宽带通信技术进行 深入调查，对移动互联网技现状及发展进行详细的技析；对手机和掌上电脑PDA通过MODEM互连构成 移动终端设备，进行大量分析和测试；对国内外各种型号掌上电脑PDA的软硬件进行详细的分析论证，掌握适合 国内发展的软硬技术方案。";
            p = 0;
            n = ss.SimilarText(s1, s2, out p);
            Console.Out.WriteLine("{0}   percent:{1} ", n, p);

            n = ss.SimilarText2(s2, s1, out p);
            Console.Out.WriteLine("{0}   percent:{1} ", n, p);

            n = ss.SimilarText3(s2, s1, out p);
            Console.Out.WriteLine("{0}   percent:{1} ", n, p);




            Console.Read();
        }
    }
}
