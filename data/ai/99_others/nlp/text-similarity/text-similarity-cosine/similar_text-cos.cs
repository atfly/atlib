 //”‡œ“º–Ω«
        public static decimal CompareWithWordSegmentation(string correctPhraseContent, string parserPhraseContent)
        {
            if (string.IsNullOrWhiteSpace(correctPhraseContent) && string.IsNullOrWhiteSpace(parserPhraseContent)) return 1;
            if (string.IsNullOrWhiteSpace(correctPhraseContent) || string.IsNullOrWhiteSpace(parserPhraseContent)) return 0;

            //œ»«–¥             
            var list1 = TextTokenizer.GetTokens(correctPhraseContent); // str1.ToCharArray(); //SegmentationHelper.Segmentation(str1);
            var list2 = TextTokenizer.GetTokens(parserPhraseContent); //SegmentationHelper.Segmentation(str2);
            if (list1 == null && list2 == null) return 1;
            if (list1 == null || list2 == null) return 0;

            Dictionary<string, int> dic1 = new Dictionary<string, int>();
            foreach (var str in list1)
            {
                if (dic1.ContainsKey(str))
                {
                    dic1[str]++;
                }
                else
                {
                    dic1[str] = 1;
                }
            }

            Dictionary<string, int> dic2 = new Dictionary<string, int>();
            foreach (var str in list2)
            {
                if (dic2.ContainsKey(str))
                {
                    dic2[str]++;
                }
                else
                {
                    dic2[str] = 1;
                }
            }

            long DenominatorPart1 = 0;
            long DenominatorPart2 = 0;
            foreach (string key in dic1.Keys) DenominatorPart1 += dic1[key] * dic1[key];
            foreach (string key in dic2.Keys) DenominatorPart2 += dic2[key] * dic2[key];
            long Denominator = DenominatorPart1 * DenominatorPart2;
            long Numerator = 0;
            foreach (string key in dic1.Keys)
            {
                if (dic2.ContainsKey(key))
                {
                    Numerator += dic1[key] * dic2[key];
                }
            }
            if (Denominator == 0)
                return 0;

            double tmpDle = (Numerator * Numerator) / Denominator + (1.0 * ((Numerator * Numerator) % Denominator)) / Denominator;
            return (decimal)Math.Sqrt(tmpDle);
        }