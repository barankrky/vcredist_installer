using System;
using System.Diagnostics;
using System.Drawing;
using System.IO;
using System.Threading;
using System.Windows.Forms;

namespace vcredist_installer
{
    public class SilentInstaller
    {
        static NotifyIcon notifyIcon = new NotifyIcon();

        static void NotifyIconStarted()
        {
            notifyIcon.Icon = IconExtractor.Extract("imageres.dll", 301, true);
            notifyIcon.Text = "Installation started.";
            notifyIcon.BalloonTipTitle = Properties.Resources.console_title;
            notifyIcon.BalloonTipText = "Installation started. Please wait until it is completed.";
            notifyIcon.Visible = true;
            notifyIcon.ShowBalloonTip(3000);

        }

        static void NotifyIconFinished()
        {
            notifyIcon.Icon = IconExtractor.Extract("imageres.dll", 232, true);
            notifyIcon.Text = "Installation finished.";
            notifyIcon.BalloonTipTitle = Properties.Resources.console_title;
            notifyIcon.BalloonTipText = "Installation completed successfully.";
            notifyIcon.ShowBalloonTip(3000);

        }

        static void Execute(string fileName, string args)
        {
            Environment.CurrentDirectory = AppDomain.CurrentDomain.BaseDirectory + "vcredists";
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
        }

        public static void Start()
        {
            NotifyIconStarted();
            Install();
            NotifyIconFinished();
        }
    }
}
