using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
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
            var rng = new Random();
            return Enumerable.Range(1, 5).Select(index => new Claim
            {
                MemberID = index,
                ClaimDate = DateTime.Now.AddDays(index),
                ClaimAmount = 100
            })
            .ToArray();
        }
    }
}
