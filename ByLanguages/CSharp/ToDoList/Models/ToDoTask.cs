using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;

namespace ToDoList.Models
{
    public class ToDoTask
    {
        public int ToDoTaskId { get; set; }
        public string Name { get; set; }
        public string Description { get; set; }
        public bool IsCompleted { get; set; }
        public virtual ApplicationUser User { get; set; }
    }
}