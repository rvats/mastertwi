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
    public class ModelController : ControllerBase
    {
        private static readonly string[] Summaries = new[]
        {
            "Freezing", "Bracing", "Chilly", "Cool", "Mild", "Warm", "Balmy", "Hot", "Sweltering", "Scorching"
        };

        private readonly ILogger<ModelController> _logger;

        public ModelController(ILogger<ModelController> logger)
        {
            _logger = logger;
        }

        [HttpGet]
        public IEnumerable<Model> Get()
        {
            var rng = new Random();
            return Enumerable.Range(1, 5).Select(index => new Model
            {
                MemberID = index,
                EnrollmentDate = DateTime.Now.AddDays(index),
                FirstName = "FirstName",
                LastName = "LastName"
            })
            .ToArray();
        }
    }
}
