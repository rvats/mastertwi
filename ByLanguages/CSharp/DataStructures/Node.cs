using System.Collections.Generic;

namespace DataStructures
{
    public class Node
    {
        public object Value { get; set; }
        public List<Node> AdjacentNodes { get; set; }
    }
}
