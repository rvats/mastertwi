using System;
using System.Collections.Generic;
using System.Data;
using System.Data.Entity;
using System.Linq;
using System.Net;
using System.Web;
using System.Web.Mvc;
using ToDoList.Models;

namespace ToDoList.Controllers
{
    public class ToDoTasksController : Controller
    {
        private ApplicationDbContext db = new ApplicationDbContext();

        // GET: ToDoTasks
        public ActionResult Index()
        {
            return View(db.ToDoTasks.ToList());
        }

        // GET: ToDoTasks/Details/5
        public ActionResult Details(int? id)
        {
            if (id == null)
            {
                return new HttpStatusCodeResult(HttpStatusCode.BadRequest);
            }
            ToDoTask toDoTask = db.ToDoTasks.Find(id);
            if (toDoTask == null)
            {
                return HttpNotFound();
            }
            return View(toDoTask);
        }

        // GET: ToDoTasks/Create
        public ActionResult Create()
        {
            return View();
        }

        // POST: ToDoTasks/Create
        // To protect from overposting attacks, please enable the specific properties you want to bind to, for 
        // more details see https://go.microsoft.com/fwlink/?LinkId=317598.
        [HttpPost]
        [ValidateAntiForgeryToken]
        public ActionResult Create([Bind(Include = "ToDoTaskId,Name,Description,IsCompleted")] ToDoTask toDoTask)
        {
            if (ModelState.IsValid)
            {
                db.ToDoTasks.Add(toDoTask);
                db.SaveChanges();
                return RedirectToAction("Index");
            }

            return View(toDoTask);
        }

        // GET: ToDoTasks/Edit/5
        public ActionResult Edit(int? id)
        {
            if (id == null)
            {
                return new HttpStatusCodeResult(HttpStatusCode.BadRequest);
            }
            ToDoTask toDoTask = db.ToDoTasks.Find(id);
            if (toDoTask == null)
            {
                return HttpNotFound();
            }
            return View(toDoTask);
        }

        // POST: ToDoTasks/Edit/5
        // To protect from overposting attacks, please enable the specific properties you want to bind to, for 
        // more details see https://go.microsoft.com/fwlink/?LinkId=317598.
        [HttpPost]
        [ValidateAntiForgeryToken]
        public ActionResult Edit([Bind(Include = "ToDoTaskId,Name,Description,IsCompleted")] ToDoTask toDoTask)
        {
            if (ModelState.IsValid)
            {
                db.Entry(toDoTask).State = EntityState.Modified;
                db.SaveChanges();
                return RedirectToAction("Index");
            }
            return View(toDoTask);
        }

        // GET: ToDoTasks/Delete/5
        public ActionResult Delete(int? id)
        {
            if (id == null)
            {
                return new HttpStatusCodeResult(HttpStatusCode.BadRequest);
            }
            ToDoTask toDoTask = db.ToDoTasks.Find(id);
            if (toDoTask == null)
            {
                return HttpNotFound();
            }
            return View(toDoTask);
        }

        // POST: ToDoTasks/Delete/5
        [HttpPost, ActionName("Delete")]
        [ValidateAntiForgeryToken]
        public ActionResult DeleteConfirmed(int id)
        {
            ToDoTask toDoTask = db.ToDoTasks.Find(id);
            db.ToDoTasks.Remove(toDoTask);
            db.SaveChanges();
            return RedirectToAction("Index");
        }

        protected override void Dispose(bool disposing)
        {
            if (disposing)
            {
                db.Dispose();
            }
            base.Dispose(disposing);
        }
    }
}
