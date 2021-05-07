using System;

namespace TestWebAPI
{
    /// <summary>
    /// MemberID,
    /// EnrollmentDate,
    /// FirstName,
    /// LastName
    /// </summary>
    public class ClaimsDetail
    {
        public int MemberID { get; set; }

        public DateTime EnrollmentDate { get; set; }

        public string Name { get; set; }

        public DateTime ClaimDate { get; set; }

        public float ClaimAmount { get; set; }
    }
}
