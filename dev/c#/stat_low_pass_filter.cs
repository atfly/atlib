        private static List<double> LowPassFilter(List<double> probabilityList)
        {
            List<double> result = new List<double>();
            for (int i = 0; i < probabilityList.Count; i++)
            {
                result.Add((probabilityList[i - 2 < 0 ? i : i - 2] +
                            probabilityList[i - 1 < 0 ? i : i - 1] +
                            probabilityList[i] +
                            probabilityList[i + 2 > probabilityList.Count ? i : i + 1] +
                            probabilityList[i + 3 > probabilityList.Count ? i : i + 2]) / 5);
            }
            return result;
        }