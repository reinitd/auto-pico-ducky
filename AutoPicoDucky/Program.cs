using System.Runtime.InteropServices;

using AutoPicoDucky.Helpers;
using AutoPicoDucky.Models;

namespace AutoPicoDucky;

class Program
{
    public static void Main(string[] args)
    {

        bool isLinux = RuntimeInformation.IsOSPlatform(OSPlatform.Linux);
        bool isWindows = RuntimeInformation.IsOSPlatform(OSPlatform.Windows);

        if (isWindows)
        {
            Console.WriteLine("Windows is not yet supported.");
            return;
        }
        else if (!isLinux && !isWindows)
        {
            Console.WriteLine("Unknown and unsupported operating system type.");
            return;
        }

        Console.WriteLine(@"Auto Pico Ducky

Please complete the following...
    ...Hold down the BOOT SEL button.
    ...While holding the button down, plug in the Pico.
    ...Release the BOOT SEL button.

Please press any key once done.");

        Console.ReadLine();

        List<Disk> devices = new();

        if (isWindows)
        {
            // Yes, I know it already checks at the start of the program.
            Console.WriteLine("Windows is not yet supported.");
            return;
        }
        else
        {
            devices = GetDevices.ForLinux();
        }

        if (devices.Count == 0)
        {
            Console.WriteLine("No removeable media found.");
            return;
        }

        Console.WriteLine("Detected removeable media:");
        for (int i = 0; i < devices.Count; i++)
        {
            Disk device = devices[i];
            List<string>? mountpoints = device.Mountpoints;
            string mountpointsStr = string.Join(", ", mountpoints!.Where(mp => mp != null).Select(mp => mp.ToString())).Trim();

            if (mountpointsStr == "")
            {
                mountpointsStr = "Not mounted.";
            }

            Console.WriteLine($" [{i}] {device.Name}: Size: {device.Size}, Mount(s): {mountpointsStr}");
        }

        (bool success, int selection) result = Selection.Handle(
            devices.Cast<dynamic>().ToList(), "\nIf selected, not mounted drives will automatically be mounted.",
            "Input the number of the RPI Pico: "
        );

        if (!result.success || result.selection == -1)
        {
            return;
        }

        Disk pico = devices[result.selection];

        Console.WriteLine($"\nSelected RPI Pico: {pico.Name}");


        List<string> options = new List<string> { "Nuke", "Setup" };
        for (int i = 0; i < options.Count; i++)
        {
            string option = options[i];
            Console.WriteLine($" [{i}] {option}");
        }

        result = Selection.Handle(
            options.Cast<dynamic>().ToList(), "", "Select option: "
        );

        if (!result.success || result.selection == -1)
        {
            return;
        }


        switch (result.selection)
        {
            case 0:
                NukePico.Nuke("/dev/sdb");
                break;
            case 1:
                // Download files and put them on the Pico.
                break;
            default:
                break;
        }

        Console.WriteLine("Nothing done, still WIP.");

    }
}
