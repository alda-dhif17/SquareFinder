using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace SquareFinder
{
    public class RegionHandler
    {
        public static Dictionary<char, List<Square>> Regions = new Dictionary<char, List<Square>>();

        public static void AddSquare(char current, int x, int y, int length)
        {
            if (!Regions.ContainsKey(current))
            {
                List<Square> squares = new List<Square>();
                squares.Add(new Square(x, y, length));
                Regions.Add(current, squares);
                return;
            }

            if (length > Regions[current][0].Length)
            {
                Regions[current].Clear();
                Regions[current].Add(new Square(x, y, length));
                return;
            }else if(length == Regions[current][0].Length)
            {
                Regions[current].Add(new Square(x, y, length));
            }
        }
    }

    public class Square
    {
        public int X { private set; get; }
        public int Y { private set; get; }
        public int Length { private set; get; }

        public Square(int x, int y, int length)
        {
            X = x;
            Y = y;
            Length = length;
        }
    }
}
