using System;
using System.Collections.Generic;
using System.Globalization;
using System.IO;
using System.Linq;
using System.Threading.Tasks;
using CsvHelper;
using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Logging;

namespace TestWebAPI.Controllers
{
    [ApiController]
    [Route("[controller]")]
    public class ClaimController : ControllerBase
    {
        private readonly ILogger<ClaimController> _logger;

        public ClaimController(ILogger<ClaimController> logger)
        {
            _logger = logger;
        }

        [HttpGet]
        public IEnumerable<Claim> Get()
        {
            var records = new List<Claim>();
            var currentDirectory = Directory.GetCurrentDirectory();
            var filePath = currentDirectory + "Claim.csv";
            using (var reader = new StreamReader(filePath))
            using (var csv = new CsvReader(reader, CultureInfo.InvariantCulture))
            {
                records = csv.GetRecords<Model>().ToList();
            }
            return records;
        }
    }
}
