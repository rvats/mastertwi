using System;

namespace RestAPIDemoConsoleApp
{
    class Program
    {
        static string ConsumerKey= "*******************************************";
        static string ConsumerKeySecret= "**************************************";
        static string AccessToken = "*******************************************";
        static string AccessTokenSecret = "****************************************";

        static void Main(string[] args)
        {
            PostTweet();
            Console.ReadKey();
        }

        async static void PostTweet()
        {
            var twitter = new TwitterApi(ConsumerKey, ConsumerKeySecret, AccessToken, AccessTokenSecret);
            var response = await twitter.Tweet("The bill #HR1044 is about America first, secondary it's an immigration bill. " +
                "As it protects American worker first, stops visa abuse, not increasing single green card, " +
                "doesn't harm NIW but solves the problem of hundreds of year green card backlog. Don't delay. #PassHR1044");
            Console.WriteLine(response);
        }
    }
}
