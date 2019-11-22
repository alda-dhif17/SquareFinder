using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace SquareFinder
{
    public class Interval
    {
        public char Current { private set; get; }
        public int XFrom { private set; get; }
        public int YFrom { private set; get; }
        public int Length { private set; get; }

        public Interval(char current, int xFrom, int yFrom, int length)
        {
            Current = current;
            XFrom = xFrom;
            YFrom = yFrom;
            Length = length;
        }

        public override string ToString()
        {
            string result = "";

            for(int i = 0; i < Length; i++)
            {
                result += Current + " ";
            }

            return result;
        }
    }
}
