using System.Collections.Generic;

public static partial class GalaxyClass
{
    public class Galaxies
    {
        private Dictionary<string, int> galaxyDetails = new Dictionary<string, int>();

        public Galaxies()
        {
            galaxyDetails.Add("Tadpole", 400);
            galaxyDetails.Add("Pinwheel", 25);
            galaxyDetails.Add("Milky Way", 0);
            galaxyDetails.Add("Andromeda", 3);
        }

        public System.Collections.Generic.IEnumerable<Galaxy> NextGalaxy
        {
            get
            {
                foreach(var galaxyDetail in galaxyDetails)
                {
                    yield return new Galaxy { Name = galaxyDetail.Key, MegaLightYears = galaxyDetail.Value };
                }
            }
        }
    }
}