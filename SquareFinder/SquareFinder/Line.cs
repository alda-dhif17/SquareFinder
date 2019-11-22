using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace SquareFinder
{
    public class Line
    {
        public List<Interval> Intervals { private set; get; }

        public Line()
        {
            this.Intervals = new List<Interval>();
        }

        public void AddInterval(char givenChar, int xFrom, int yFrom, int length)
        {
            this.Intervals.Add(new Interval(givenChar, xFrom, yFrom, length));
        }

        public override string ToString()
        {
            string result = "";

            foreach(var interval in Intervals)
            {
                result += interval.ToString();
            }

            return result;
        }
    }
}
