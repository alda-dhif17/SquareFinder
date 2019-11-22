using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace SquareFinder
{
    public class IOHandler
    {
        public static List<Line> Read()
        {
            List<Line> lines = new List<Line>();

            System.IO.StreamReader file = new System.IO.StreamReader(@"D:\HTL-Kaindorf\Schuljahr_2019-2020\ALDA\square-finder\SquareFinder\square.txt");
            string line = "";
            int yPosition = 0;

            while ((line = file.ReadLine()) != null)
            {
                string[] items = line.Split(' ');
                string current = items[0];
                int xPosition = 1;
                int xStarted= 0;

                Line currentLine = new Line();

                while(xPosition < items.Length)
                {
                    if (items[xPosition].Equals(current))
                    {
                        xPosition++;
                        continue;
                    }

                    currentLine.AddInterval(current.ToCharArray()[0], xStarted, yPosition, xPosition - xStarted);
                    current = items[xPosition];
                    xStarted = xPosition;
                }

                currentLine.AddInterval(current.ToCharArray()[0], xStarted, yPosition, xPosition - xStarted);

                lines.Add(currentLine);

                yPosition++;
            }

            file.Close();

            return lines;
        }
    }
}
