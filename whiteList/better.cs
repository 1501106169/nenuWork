using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.IO;

namespace foo
{
    class Program
    {
        static void Main(string[] args)
        {
            DateTime beforDT = System.DateTime.Now;
            if (args.Count() < 1)
                return;
            string path = args[0];
            string[] sm = File.ReadAllLines(path);                      //read q file
            int[] array = new int[1000000];

            int index = 0;
            string strNum;
            while ((strNum = Console.ReadLine().Trim()).Length > 0)     //read witelist file
            {
                array[index] = Convert.ToInt32(strNum);
                index++;
            }

            string str = "";
            for (int i = 1; i < sm.Length && sm[i].Length > 0; ++i)
            {
                int temp = Convert.ToInt32(sm[i]);
                if (find(temp, array) == -1)
                    //Console.WriteLine(temp);
                    str += temp.ToString() + "\n";
            }

            DateTime afterDT = System.DateTime.Now;
            TimeSpan ts = afterDT.Subtract(beforDT);
            Console.WriteLine("DateTime: {0}ms.", ts.TotalMilliseconds);
        }
        static int find(int key, int[] array)
        {
            for (int j = 0; j < array.Length; j++)
            {
                if (key == array[j])
                    return key;
            }
            return -1;
        }
    }
}
