﻿using MainDSA.DataStructures.Trees;
using MainDSA.Quizes;
using Microsoft.VisualStudio.TestTools.UnitTesting;

namespace DSATests.Quizes
{
    [TestClass]
    public class BinaryTreeOperationsTests
    {
        private TreeNode root;

        /// <summary>
        /// Always Get Called Once The Test is Executed
        /// </summary>
        [TestInitialize]
        public void CreateData()
        {
            root= new TreeNode(4);
            root.Left = new TreeNode(2);
            root.Left.Left = new TreeNode(1);
            root.Left.Right = new TreeNode(3);
            root.Right = new TreeNode(6);
            root.Right.Left = new TreeNode(5);
            root.Right.Right = new TreeNode(7);
        }

        [TestMethod]
        public void TestBinaryTreeInOrderTraversal()
        {
            // Arrange 
            // Was just contemplating whether we need to call the method explicitly after we have marked it with TestInitialize Attribute
            // Turns Out :- No :-)

            // Act
            BinaryTreeOperations treeOperations = new BinaryTreeOperations();
            var result = treeOperations.InOrderTraversal(root);

            // Assert
            Assert.AreEqual(7, result.Count, "Wrong Value");
            for (int i = 0; i < result.Count; i++)
            {
                Assert.AreEqual(i+1, result[i], "Wrong Value");
            }
        }

        [TestMethod]
        public void TestBinaryTreePreOrderTraversal()
        {
            // Arrange 
            // Was just contemplating whether we need to call the method explicitly after we have marked it with TestInitialize Attribute
            // Turns Out :- No :-)

            // Act
            BinaryTreeOperations treeOperations = new BinaryTreeOperations();
            var result = treeOperations.PreOrderTraversal(root);

            // Assert
            Assert.AreEqual(7, result.Count, "Wrong Value");
            Assert.AreEqual(4, result[0], "Wrong Value");
            Assert.AreEqual(2, result[1], "Wrong Value");
            Assert.AreEqual(1, result[2], "Wrong Value");
            Assert.AreEqual(3, result[3], "Wrong Value");
            Assert.AreEqual(6, result[4], "Wrong Value");
            Assert.AreEqual(5, result[5], "Wrong Value");
            Assert.AreEqual(7, result[6], "Wrong Value");
        }

        [TestMethod]
        public void TestBinarySearchTreeToDoublyCircularList()
        {
            // Arrange 
            // Was just contemplating whether we need to call the method explicitly after we have marked it with TestInitialize Attribute
            // Turns Out :- No :-)

            // Act
            BinaryTreeOperations treeOperations = new BinaryTreeOperations();
            var result = treeOperations.BinarySearchTreeTreeToDoublyCircularList(root);

            // Assert
            Assert.AreEqual(1, result.Value, "Wrong Value");
            result = result.Right;
            Assert.AreEqual(2, result.Value, "Wrong Value");
            result = result.Right;
            Assert.AreEqual(3, result.Value, "Wrong Value");
            result = result.Right;
            Assert.AreEqual(4, result.Value, "Wrong Value");
            result = result.Right;
            Assert.AreEqual(5, result.Value, "Wrong Value");
            result = result.Right;
            Assert.AreEqual(6, result.Value, "Wrong Value");
            result = result.Right;
            Assert.AreEqual(7, result.Value, "Wrong Value");
            result = result.Right;
            Assert.AreEqual(1, result.Value, "Wrong Value");
            result = result.Left;
            Assert.AreEqual(7, result.Value, "Wrong Value");
            result = result.Left;
            Assert.AreEqual(6, result.Value, "Wrong Value");
            result = result.Left;
            Assert.AreEqual(5, result.Value, "Wrong Value");
            result = result.Left;
            Assert.AreEqual(4, result.Value, "Wrong Value");
            result = result.Left;
            Assert.AreEqual(3, result.Value, "Wrong Value");
            result = result.Left;
            Assert.AreEqual(2, result.Value, "Wrong Value");
            result = result.Left;
            Assert.AreEqual(1, result.Value, "Wrong Value");
        }

        [TestMethod]
        public void TestBinaryTreePaths1()
        {
            // Arrange 
            // Was just contemplating whether we need to call the method explicitly after we have marked it with TestInitialize Attribute
            // Turns Out :- No :-)

            // Act
            BinaryTreeOperations treeOperations = new BinaryTreeOperations();
            var results = treeOperations.BinaryTreePaths(root);

            // Assert
            Assert.AreEqual(4, results.Count, "Wrong Value");
            Assert.AreEqual("4->2->1", results[0], "Wrong Value");
            Assert.AreEqual("4->2->3", results[1], "Wrong Value");
            Assert.AreEqual("4->6->5", results[2], "Wrong Value");
            Assert.AreEqual("4->6->7", results[3], "Wrong Value");
        }

        [TestMethod]
        public void TestBinaryTreePaths2()
        {
            // Arrange 
            var root = new TreeNode(1);
            root.Left = new TreeNode(2);
            root.Left.Right = new TreeNode(5);
            root.Right = new TreeNode(3);

            // Act
            BinaryTreeOperations treeOperations = new BinaryTreeOperations();
            var results = treeOperations.BinaryTreePaths(root);

            // Assert
            Assert.AreEqual(2, results.Count, "Wrong Value");
            Assert.AreEqual("1->2->5", results[0], "Wrong Value");
            Assert.AreEqual("1->3", results[1], "Wrong Value");
        }

        [TestMethod]
        public void TestIsValidBinarySearchTree1()
        {
            // Arrange 
            // Was just contemplating whether we need to call the method explicitly after we have marked it with TestInitialize Attribute
            // Turns Out :- No :-)

            // Act
            BinaryTreeOperations treeOperations = new BinaryTreeOperations();
            var result = treeOperations.IsValidBinarySearchTree(root);

            // Assert
            Assert.AreEqual(true, result, "Wrong Value");
        }

        [TestMethod]
        public void TestIsValidBinarySearchTree2()
        {
            // Arrange 
            var root = new TreeNode(1);
            root.Left = new TreeNode(2);
            root.Left.Right = new TreeNode(5);
            root.Right = new TreeNode(3);

            // Act
            BinaryTreeOperations treeOperations = new BinaryTreeOperations();
            var result = treeOperations.IsValidBinarySearchTree(root);

            // Assert
            Assert.AreEqual(false, result, "Wrong Value");
        }

        [TestMethod]
        public void TestGetDiameterOfBinaryTree1()
        {
            // Arrange

            // Act
            BinaryTreeOperations treeOperations = new BinaryTreeOperations();
            var result = treeOperations.GetDiameterOfBinaryTree(root);

            // Assert
            Assert.AreEqual(4, result, "Wrong Value");
        }

        [TestMethod]
        public void TestInorderSuccessor1()
        {
            // Arrange

            // Act
            BinaryTreeOperations treeOperations = new BinaryTreeOperations();
            var result = treeOperations.InorderSuccessor(root, root.Right.Left);

            // Assert
            Assert.AreEqual(6, result.Value, "Wrong Value");
        }

        [TestMethod]
        public void TestGetDiameterOfBinaryTree2()
        {
            // Arrange 
            var root = new TreeNode(1);
            root.Left = new TreeNode(2);
            root.Left.Right = new TreeNode(5);
            root.Right = new TreeNode(3);

            // Act
            BinaryTreeOperations treeOperations = new BinaryTreeOperations();
            var result = treeOperations.GetDiameterOfBinaryTree(root);

            // Assert
            Assert.AreEqual(3, result, "Wrong Value");
        }

        /// <summary>
        /// Always Get Called Once The Test is Over
        /// </summary>
        [TestCleanup]
        public void DestroyData()
        {
            root = null;
        }
    }
}
