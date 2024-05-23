
namespace AutoPicoDucky.Models;

public class Disk
{
    public string Name { get; set; }
    public string MajMin { get; set; }
    public bool Rm { get; set; }
    public string Size { get; set; }
    public bool Ro { get; set; }
    public string Type { get; set; }
    public List<string>? Mountpoints { get; set; }
    public List<Disk>? Children { get; set; }
}