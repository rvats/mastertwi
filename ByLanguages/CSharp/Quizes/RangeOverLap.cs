﻿using System;

namespace MainDSA.Quizes
{
    public class RangeOverlap
    {
        public readonly int StartPoint;
        public readonly int Length;

        public RangeOverlap()
        {
            StartPoint = 0;
            Length = 0;
        }

        public RangeOverlap(int highestStartPoint, int overlapLength)
        {
            StartPoint = highestStartPoint;
            Length = overlapLength;
        }

        public RangeOverlap FindRangeOverlap(int point1, int length1, int point2, int length2)
        {
            // Find the highest start point and lowest end point.
            // The highest ("rightmost" or "upmost") start point is
            // the start point of the overlap.
            // The lowest end point is the end point of the overlap.
            int highestStartPoint = Math.Max(point1, point2);
            int lowestEndPoint = Math.Min(point1 + length1, point2 + length2);

            // Return empty overlap if there is no overlap
            if(highestStartPoint >= lowestEndPoint)
            {
                return new RangeOverlap();
            }

            // Compute the overlap length
            int overlapLength = lowestEndPoint - highestStartPoint;

            return new RangeOverlap(highestStartPoint, overlapLength);
        }

        public LoveRectangle FindRectangularOverlap(LoveRectangle rect1, LoveRectangle rect2)
        {
            // Get the x and y overlap points and lengths
            RangeOverlap xOverlap = FindRangeOverlap(rect1.LeftX, rect1.Width, rect2.LeftX, rect2.Width);
            RangeOverlap yOverlap = FindRangeOverlap(rect1.BottomY, rect1.Height, rect2.BottomY, rect2.Height);

            // Return null rectangle if there is no overlap
            if(xOverlap.StartPoint==0 || yOverlap.StartPoint == 0)
            {
                return new LoveRectangle();
            }

            return new LoveRectangle(xOverlap.StartPoint, yOverlap.StartPoint, xOverlap.Length, yOverlap.Length);
        }
    }
}
