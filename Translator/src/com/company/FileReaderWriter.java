package com.company;


import java.io.*;
import java.util.Scanner;

public class FileReaderWriter {

    public static String readFile(String file_name) {
        try {
            Scanner file_reader = new Scanner(new File(file_name));
            StringBuilder large_text_Anna = new StringBuilder();
            while(file_reader.hasNextLine()) {
                large_text_Anna.append(file_reader.nextLine());
            }
            return large_text_Anna.toString();
        } catch (FileNotFoundException exception) {
            return "Oops! Seems like an error occurred during the writing from file!";
        }
    }

    public static boolean writeFile(String file_name, String text) {
        try {
            String str = "src/output/translated-to_" + file_name + ".txt";
            System.out.println(str);
            BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(str));
            bufferedWriter.write(text);
            bufferedWriter.close();
            return  true;
        } catch (Exception e) {
            return false;
        }
    }
}
