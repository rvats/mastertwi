using Microsoft.AspNet.Identity;
using Microsoft.AspNet.Identity.EntityFramework;
using System;
using System.Data.Entity;
using System.Data.Entity.Migrations;
using System.Linq;
using ToDoList.Models;

namespace ToDoList.Migrations
{
    internal sealed class Configuration : DbMigrationsConfiguration<ToDoList.Models.ApplicationDbContext>
    {
        public Configuration()
        {
            AutomaticMigrationsEnabled = false;
        }

        protected override void Seed(ApplicationDbContext context)
        {
            //  This method will be called after migrating to the latest version.

            //  You can use the DbSet<T>.AddOrUpdate() helper extension method 
            //  to avoid creating duplicate seed data.
            AddUser(context);
        }

        protected void AddUser(ApplicationDbContext context)
        {
            var user = new ApplicationUser { UserName = "Rahul Vats", Email = "vats.rahul@live.com" };
            var userManager = new ApplicationUserManager(new UserStore<ApplicationUser>(context));
            userManager.Create(user, "1Qazmko0!");
        }
    }
}
