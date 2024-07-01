using System;
using System.Diagnostics;
using System.IO;
using System.Threading;

namespace vcredist_installer
{
    public class ConsoleInstaller
    {

        static void Execute(string fileName, string args)
        {
            Environment.CurrentDirectory = AppDomain.CurrentDomain.BaseDirectory + "vcredists";
            Console.Write("\n-> Installing " + fileName + "...");
            ProcessStartInfo psi = new ProcessStartInfo();
            psi.FileName = "cmd.exe";
            psi.Arguments = @"/c " + fileName + " " + args;
            psi.WindowStyle = ProcessWindowStyle.Hidden;
            psi.RedirectStandardOutput = true;
            psi.RedirectStandardError = true;
            psi.UseShellExecute = false;
            psi.CreateNoWindow = true;

            Process proc = new Process();
            proc.StartInfo = psi;
            proc.Start();
            proc.WaitForExit();
        }
        static void Install()
        {
            bool is64bit = Environment.Is64BitOperatingSystem;
            string vcredist_version = "all";

            switch (is64bit)
            {
                case false:
                    switch (vcredist_version)
                    {
                        case "all":
                            Execute("vcredist2005_x86.exe", @"/q:a /c:""msiexec /i vcredist.msi /qn""");

                            Execute("vcredist2008_x86.exe", @"/q:a /c:""msiexec /i vcredist.msi /qn""");

                            Execute("vcredist2010_x86.exe", @"/q");

                            Execute("vcredist2012_x86.exe", @"/install /quiet /norestart");

                            Execute("vcredist2013_x86.exe", @"/install /quiet /norestart");

                            Execute("vcredist2015_2017_2019_2022_x86.exe", @"/install /quiet /norestart");
                            break;

                        default:
                            break;
                    }
                    break;

                case true:
                    switch (vcredist_version)
                    {
                        case "all":
                            Execute("vcredist2005_x86.exe", @"/q:a /c:""msiexec /i vcredist.msi /qn""");
                            Execute("vcredist2005_x64.exe", @"/q:a /c:""msiexec /i vcredist.msi /qn""");

                            Execute("vcredist2008_x86.exe", @"/q:a /c:""msiexec /i vcredist.msi /qn""");
                            Execute("vcredist2008_x64.exe", @"/q:a /c:""msiexec /i vcredist.msi /qn""");

                            Execute("vcredist2010_x86.exe", @"/q");
                            Execute("vcredist2010_x64.exe", @"/q");

                            Execute("vcredist2012_x86.exe", @"/install /quiet /norestart");
                            Execute("vcredist2012_x64.exe", @"/install /quiet /norestart");

                            Execute("vcredist2013_x86.exe", @"/install /quiet /norestart");
                            Execute("vcredist2013_x64.exe", @"/install /quiet /norestart");

                            Execute("vcredist2015_2017_2019_2022_x86.exe", @"/install /quiet /norestart");
                            Execute("vcredist2015_2017_2019_2022_x64.exe", @"/install /quiet /norestart");
                            break;

                        default:
                            break;
                    }
                    break;

                default:
                    break;
            }
            Console.Clear();
            Console.WriteLine(Properties.Resources.app_title);
            Console.Write(">> All vcredists are installed completely. Closing in 3 seconds...");
            Thread.Sleep(2800);
            Environment.Exit(0);
        }


        public static void Start()
        {
            Console.Title = Properties.Resources.console_title;
            Console.WriteLine(Properties.Resources.app_title);
            Install();
        }
    }
}
