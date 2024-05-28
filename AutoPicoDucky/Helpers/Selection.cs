using System;

namespace AutoPicoDucky.Helpers;

public class Selection {
    public static (bool, int) Handle(List<dynamic> list, string notice, string message) {
        // Tuple<bool, int> result = Tuple.Create(true, -1);
        (bool success, int selection) result = (success: false, selection: -1);

        if (notice.Trim() != "") {
            Console.WriteLine(notice);
        }
        
        if (message.Trim() != "") {
            Console.Write(message);
        }

        string selectionInput = Console.ReadLine().Trim();
        int selection;

        if (!Int32.TryParse(selectionInput, out selection)) {
            Console.WriteLine($"\nSelection '{selectionInput}' is not a valid selection.");
            return result;
        }
        
        if (selection >= list.Count) {
            Console.WriteLine("\nSelection is too high!");
            return result;
        }
        
        if (selection < 0) {
            Console.WriteLine("\nSelection cannot be negative, silly!");
            return result;
        }

        result.success = true;
        result.selection = selection;
        return result;

    }
}