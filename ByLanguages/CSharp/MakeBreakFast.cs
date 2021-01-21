static void Main(string[] args)
{
    var breakFast = await Task.Run( () => MakeBreakFast());
    // once here I know breakfast is ready
    Eat(breakFast);
}
private static async Task<BreakFast> MakeBreakFast()
{
    var taskToastBread = ToastBreadAsync();
    // do not await. As soon as the procedure awaits come back to do the next statement:
    var taskBoilEggs = BoilEggsAsync();
    // again do not await. Come back as the procedure awaits
    var  taskMakeTea = MakeTeaAsync();
    // do not wait, but come bask as soon as the procedure await

    // now wait until all three tasks are finished:
    await Task.WhenAll (new Task[] {taskToasBread, taskBoilEggs, taskMakeTea});
    // if here: all tasks are finished. Property Result contains the return value of the Task:
    return new BreakFast()
    {
        Toast = taskToastBread.Result,
        Eggs = taskBoilEggs.Result,
        Tea = taksMakeTea.Result,
    }
}

private static Task<Toast> ToastBreadAsync()
{
    var sliceOfBread = Loaf.CutSliceOfBread();
    Toaster.Insert(sliceOfBread);
    await Toaster.Toast();
    // the function does not wait but return to the caller.
    // the next is done when the caller await and the toaster is ready toasting
    var toast = Toaster.Remove();
    return Toast();
}

private static Task<Eggs> BoilEggsAsync()
{
    var eggPan = ...
    await eggPan.BoilWater();
    var eggs = Fridge.ExtreactEggs();
    EggPan.Insert(eggs);
    await Task.Delay(TimeSpan.FromMinutes(7));
    return EggPan.Remove();
}