using System;
using static GalaxyClass;

namespace Galaxy
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello World!");
            GalaxyClass.ShowGalaxies();
            var theGalaxies = new global::GalaxyClass.Galaxies();
            foreach (global::GalaxyClass.Galaxy theGalaxy in theGalaxies.NextGalaxy)
            {
                Console.WriteLine(theGalaxy.Name + " " + theGalaxy.MegaLightYears.ToString());
            }
        }
    }
}
