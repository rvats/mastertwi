using DSOperations;
using System;
using System.Collections.Generic;

namespace MainDemo
{
    class Program
    {
        static void Main(string[] args)
        {
            TreeOperations treeOperations = new TreeOperations();
            var Data = new List<object> { 5, 3, 7, 2, 4, 6, 8, 1, 9 };
            treeOperations.PopulateBinarySearchTree(Data);
            Console.WriteLine("=========================================================================");
            treeOperations.PreOrderTraversal();
            Console.WriteLine();
            Console.WriteLine("=========================================================================");
            treeOperations.InOrderTraversal();
            Console.WriteLine();
            Console.WriteLine("=========================================================================");
            treeOperations.PostOrderTraversal();
            Console.WriteLine();
            Console.WriteLine("=========================================================================");
        }
    }
}
