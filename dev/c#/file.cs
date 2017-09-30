//直接写文件
System.IO.File.AppendAllText(@"D:\text.txt", System.Environment.NewLine + "完整度：" + completionBoost.ToString() + ',' + c2.ToString());
