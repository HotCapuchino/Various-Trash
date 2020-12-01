package com.company;

import java.io.*;
import java.util.Map;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) throws IOException {
        Map<String, String> lang_codes = AvailableLanguages.jsonParser(AvailableLanguages.getAvailableLanguages());
        for (String key : lang_codes.keySet()) {
            System.out.println(key + " -> " + lang_codes.get(key));
        }
        MetaData meta = new MetaData();
        Scanner sc = new Scanner(System.in);
        String target_language = "";
        boolean correct_lang = false;
        while (true) {
            System.out.print("Choose either language name or language code and state your choice here: ");
            String preferred_language = sc.nextLine();
            for (String lang : lang_codes.keySet()) {
                if (lang.toLowerCase().equals(preferred_language.toLowerCase()) ||
                        lang_codes.get(lang).toLowerCase().equals(preferred_language.toLowerCase())) {
                    target_language = lang;
                    correct_lang = true;
                }
            }
            if (correct_lang) {
                break;
            } else {
                System.out.println("Seems like language you've chosen isn't supported ot your input was incorrect");
            }
        }
//        String text_to_be_translated = "Привет";
        String text_to_be_translated = FileReaderWriter.readFile(MetaData.getTEXT());
        String translated = GetTranslation.serializeResponse(GetTranslation.getTranslation(text_to_be_translated, target_language));
        System.out.println(target_language);
        FileReaderWriter.writeFile(target_language, translated);
    }
}