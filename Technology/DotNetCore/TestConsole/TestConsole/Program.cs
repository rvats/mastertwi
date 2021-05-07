using System;
using System.Threading.Tasks;

namespace TestConsole
{
    class Program
    {
        private static string result;

        static async Task Main()
        {
            await SaySomething();
            Console.WriteLine(result);
        }

        static async Task<string> SaySomething()
        {
            result = "Hello world!";
            await Task.Delay(5000);
            return "Something";
        }
    }
}