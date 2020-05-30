using DataStructures;
using System;
using System.Collections.Generic;
using System.Linq;

namespace DSOperations
{
    public class TreeOperations
    {
        private BinaryTreeNode current;

        public void PopulateBinarySearchTree(List<object> Data)
        {
            var root = current;

            while (Data.Count > 0)
            {
                root = Insert(root, Data.First());
                Data.RemoveAt(0);
            }

            current = root;
        }

        private BinaryTreeNode Insert(BinaryTreeNode root, Object v)
        {
            if (root == null)
            {
                root = new BinaryTreeNode();
                root.Value = v;
            }
            else if ((int)v < (int)root.Value)
            {
                root.Left = Insert(root.Left, v);
            }
            else
            {
                root.Right = Insert(root.Right, v);
            }

            return root;
        }

        public void PreOrderTraversal()
        {
            BinaryTreeNode root = current;
            PreOrderTraversal(current);
        }

        private void PreOrderTraversal(BinaryTreeNode root)
        {
            if (root == null) return;
            Console.Write(root.Value.ToString()+" ");
            PreOrderTraversal(root.Left);
            PreOrderTraversal(root.Right);
        }

        public void InOrderTraversal()
        {
            BinaryTreeNode root = current;
            InOrderTraversal(current);
        }

        private void InOrderTraversal(BinaryTreeNode root)
        {
            if (root == null) return;
            InOrderTraversal(root.Left);
            Console.Write(root.Value.ToString() + " ");
            InOrderTraversal(root.Right);
        }

        public void PostOrderTraversal()
        {
            BinaryTreeNode root = current;
            PostOrderTraversal(current);
        }

        private void PostOrderTraversal(BinaryTreeNode root)
        {
            if (root == null) return;
            PostOrderTraversal(root.Left);
            PostOrderTraversal(root.Right);
            Console.Write(root.Value.ToString() + " ");
        }
    }
}
