using System.Diagnostics;
using Newtonsoft.Json.Linq;
using AutoPicoDucky.Models;

namespace AutoPicoDucky.Helpers;

public static class GetDevices
{
    public static List<Disk> ForLinux()
    {

        Process lsblk = new();
        lsblk.StartInfo.FileName = "/bin/bash";
        lsblk.StartInfo.Arguments = "-c \"lsblk -J\"";
        lsblk.StartInfo.RedirectStandardOutput = true;
        lsblk.StartInfo.UseShellExecute = false;
        lsblk.StartInfo.CreateNoWindow = true;

        List<Disk> devices = new();

        try
        {
            lsblk.Start();
            string output = lsblk.StandardOutput.ReadToEnd();
            lsblk.WaitForExit();

            JObject data = JObject.Parse(output);

            JArray blockDevices = (JArray)data["blockdevices"];

            foreach (JToken blockDeviceToken in data["blockdevices"])
            {
                // JObject blockDevice = (JObject)blockDeviceToken;
                Disk disk = blockDeviceToken.ToObject<Disk>();

                // bool isRemovable = disk["rm"].Value<bool>();
                // string type = disk["type"].Value<string>();
                // bool isReadOnly = disk["ro"].Value<bool>();
                // JArray mountpoints = (JArray)disk["mountpoints"];

                bool isRemovable = disk.Rm;
                string type = disk.Type;
                bool isReadOnly = disk.Ro;
                List<string> mountpoints = disk.Mountpoints;

                if (isRemovable && !isReadOnly && type == "disk" && mountpoints != null && mountpoints != null && !mountpoints.Contains("/"))
                {
                    devices.Add(disk);
                }
            }
        }
        catch (Exception ex)
        {
            Console.WriteLine($"An error occurred: {ex.Message}");
        }
        finally
        {
            if (!lsblk.HasExited)
            {
                lsblk.Kill();
            }
            lsblk.Dispose();
        }

        return devices;

    }
}