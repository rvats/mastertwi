using System;

namespace TestWebAPI
{
    /// <summary>
    /// MemberID,
    /// ClaimDate,
    /// ClaimAmount
    /// </summary>
    public class Claim
    {
        public int MemberID { get; set; }

        public DateTime ClaimDate { get; set; }

        public float ClaimAmount { get; set; }
    }
}
