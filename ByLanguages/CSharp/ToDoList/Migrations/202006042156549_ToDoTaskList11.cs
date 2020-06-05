namespace ToDoList.Migrations
{
    using System;
    using System.Data.Entity.Migrations;
    
    public partial class ToDoTaskList11 : DbMigration
    {
        public override void Up()
        {
            CreateTable(
                "dbo.ToDoTasks",
                c => new
                    {
                        ToDoTaskId = c.Int(nullable: false, identity: true),
                        Name = c.String(),
                        Description = c.String(),
                        IsCompleted = c.Boolean(nullable: false),
                        User_Id = c.String(maxLength: 128),
                    })
                .PrimaryKey(t => t.ToDoTaskId)
                .ForeignKey("dbo.AspNetUsers", t => t.User_Id)
                .Index(t => t.User_Id);
            
        }
        
        public override void Down()
        {
            DropForeignKey("dbo.ToDoTasks", "User_Id", "dbo.AspNetUsers");
            DropIndex("dbo.ToDoTasks", new[] { "User_Id" });
            DropTable("dbo.ToDoTasks");
        }
    }
}
