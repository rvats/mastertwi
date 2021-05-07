using System.Collections.Generic;
using System.Globalization;
using System.IO;
using System.Linq;
using CsvHelper;
using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Logging;

namespace TestWebAPI.Controllers
{
    [ApiController]
    [Route("[controller]")]
    public class ClaimsDetailsController : ControllerBase
    {
        private readonly ILogger<ClaimsDetailsController> _logger;

        public ClaimsDetailsController(ILogger<ClaimsDetailsController> logger)
        {
            _logger = logger;
        }

        [HttpGet]
        public IEnumerable<ClaimsDetail> Get()
        {
            var currentDirectory = Directory.GetCurrentDirectory();

            var memberRecords = new List<Member>();
            var filePath = currentDirectory + "\\Data\\Member.csv";
            using (var reader = new StreamReader(filePath))
            using (var csv = new CsvReader(reader, CultureInfo.InvariantCulture))
            {
                memberRecords = csv.GetRecords<Member>().ToList();
            }
            var claimRecords = new List<Claim>();
            filePath = currentDirectory + "\\Data\\Claim.csv";
            using (var reader = new StreamReader(filePath))
            using (var csv = new CsvReader(reader, CultureInfo.InvariantCulture))
            {
                claimRecords = csv.GetRecords<Claim>().ToList();
            }
            var claimsDetails = new List<ClaimsDetail>();
            claimsDetails = (from memberRecord in memberRecords
                        join claimRecord in claimRecords on memberRecord.MemberID equals claimRecord.MemberID
                        select new ClaimsDetail {
                            MemberID = memberRecord.MemberID, 
                            Name = memberRecord.FirstName + " " + memberRecord.LastName,
                            EnrollmentDate = memberRecord.EnrollmentDate,
                            ClaimDate = claimRecord.ClaimDate,
                            ClaimAmount = claimRecord.ClaimAmount
                        }).OrderBy(x => x.Name).ThenByDescending(x => x.MemberID).ToList(); ;

            return claimsDetails;
        }
    }
}
