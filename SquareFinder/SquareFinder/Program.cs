using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace SquareFinder
{
    public class Program
    {
        public static List<Line> lines;

        static void Main(string[] args)
        {

            Console.WriteLine("---> Square Finder <---");

            lines = IOHandler.Read();

            lines.ForEach(line =>
            {
                Console.WriteLine(line.ToString());
            });

            Console.ReadLine();
        }
    }
}
