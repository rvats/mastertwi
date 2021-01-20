using System;
using System.Collections.Generic;
using System.Globalization;
using System.IO;
using System.Linq;
using System.Text;

namespace GenerateRandomNumber
{
    class Program
    {
        static Random random = new Random();

        public static List<int> GenerateRandom(int count = 1000000)
        {
            // generate count random values.
            HashSet<int> candidates = new HashSet<int>();
            while (candidates.Count < count)
            {
                // May strike a duplicate.
                candidates.Add(random.Next());
            }

            // load them in to a list.
            List<int> result = new List<int>();
            result.AddRange(candidates);

            // shuffle the results:
            int i = result.Count;
            while (i > 1)
            {
                i--;
                int k = random.Next(i + 1);
                int value = result[k];
                result[k] = result[i];
                result[i] = value;
            }
            return result;
        }

        public static void LogRandomNumbers(List<int> randomNumbers)
        {
            string fileNameFormat = "{0}{1}{2}{3}";
            string currentDirectory = Directory.GetCurrentDirectory();
            string filePrefix = @"\RandomNumberLogs_";
            string fileId = DateTime.Now.ToString("s", CultureInfo.CreateSpecificCulture("en-US"))
                .Trim().Replace(":",string.Empty).Replace("-",string.Empty);
            string fileExt = ".txt";
            string fileName = string.Format(fileNameFormat, currentDirectory, filePrefix, fileId, fileExt);

            try
            {
                // Check if file already exists. If yes, delete it.     
                if (File.Exists(fileName))
                {
                    File.Delete(fileName);
                }

                File.WriteAllLines(fileName, randomNumbers.Select(x => x.ToString()));

                // Open the stream and read it back.    
                using (StreamReader sr = File.OpenText(fileName))
                {
                    string s = "";
                    while ((s = sr.ReadLine()) != null)
                    {
                        Console.WriteLine(s);
                    }
                }
            }
            catch (Exception Ex)
            {
                Console.WriteLine(Ex.ToString());
            }
        }

        public static void Main()
        {
            List<int> randomNumbers = GenerateRandom();
            Console.WriteLine("Result: " + randomNumbers.Count);
            randomNumbers.ForEach(Console.WriteLine);
            LogRandomNumbers(randomNumbers);
        }
    }
}