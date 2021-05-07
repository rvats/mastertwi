using System;

namespace TestWebAPI
{
    /// <summary>
    /// MemberID,
    /// EnrollmentDate,
    /// FirstName,
    /// LastName
    /// </summary>
    public class Member
    {
        public int MemberID { get; set; }

        public DateTime EnrollmentDate { get; set; }

        public string FirstName { get; set; }

        public string LastName { get; set; }
    }
}
