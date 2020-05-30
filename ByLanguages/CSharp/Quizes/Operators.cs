﻿using System.Collections.Generic;

namespace MainDSA.Quizes
{
    public class Operators
    {
        private List<string> result = new List<string>();

        public List<string> Result { get => result; set => result = value; }

        public IList<string> AddOperators(string number, int target)
        {
            AddOperators(number, target, "", 0, 0);
            return Result;
        }

        private void AddOperators(string number, int target, string temporary, long currentResult, long previousNumber)
        {
            if (currentResult == target && number.Length == 0)
            {
                Result.Add(temporary);
                return;
            }

            for (int i = 1; i <= number.Length; i++)
            {
                string currentDigit = number.Substring(0, i);
                if (currentDigit.Length > 1 && currentDigit[0] == '0') return;
                string nextDigit = number.Substring(i,number.Length-i);
                long currentNumber = long.Parse(currentDigit);
                if (temporary.Length != 0)
                {
                    AddOperators(
                        nextDigit, 
                        target, 
                        temporary + "+" + currentNumber, 
                        currentResult + currentNumber, 
                        currentNumber);

                    AddOperators(
                        nextDigit, 
                        target, 
                        temporary + "-" + currentNumber, 
                        currentResult - currentNumber, 
                        -currentNumber);

                    AddOperators(
                        nextDigit, 
                        target, 
                        temporary + "*" + currentNumber, 
                        (currentResult - previousNumber) + previousNumber * currentNumber, 
                        previousNumber * currentNumber);
                }
                else
                {
                    AddOperators(nextDigit, target, currentDigit, currentNumber, currentNumber);
                }

            }
        }
    }
}
