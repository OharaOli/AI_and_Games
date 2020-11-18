import java.util.Random; 
import java.io.FileWriter;   // Import the FileWriter class
import java.io.File;
import java.util.*;  

// Consider that we start south always for now, we will return a bot which 
// does the options in a normal way without causing exceptions.

public class ReadBytes
{

    public String getMove() throws Exception
    {
        File file = new File("out.txt");
        FileWriter fr = new FileWriter(file, true);

        Scanner sc = new Scanner(System.in);
        String str = sc.nextLine();
        
        fr.write(str + "\n");
        fr.close();

        String[] optionStrings = {"MOVE;1","MOVE;2", "MOVE;3","MOVE;4","MOVE;5","MOVE;6","MOVE;7","SWAP"};

        Random random = new Random();

        int choiceNumber = random.nextInt(6);
        
        return  optionStrings[choiceNumber];
    }

    public static void main(String[] args) throws Exception
    {

        System.out.println("MOVE;1");
        ReadBytes readBytes = new ReadBytes();

        String readString = readBytes.getMove();
        while(true){
            if(readString != "START;South")
                System.out.println(readBytes.getMove());
            else
                System.out.print("");
        }//while
    }
}
