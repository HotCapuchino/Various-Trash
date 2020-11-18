package com.company;

import java.io.*;
import java.net.HttpURLConnection;
import java.net.URL;
import java.nio.charset.StandardCharsets;
import java.util.Base64;
import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;
import org.json.JSONObject;

public class Main {

    final static String TEXT = "src/res/text.txt";
    final static String LANG_CODES = "src/res/lang_codes.txt";
    static String API_URL = "https://api.cognitive.microsofttranslator.com/translate?api-version=3.0&to=";
    final static String API_KEY = "82e622ccc27b4ad0af0918182329a742";
    final static String API_REGION = "westeurope";
    final static  String TARGET_FILE = "src/output/out.txt";

    public static void main(String[] args) throws IOException {
        Map<String, String> lang_dictionary = new HashMap<String, String>();
        readLanguageCodes(lang_dictionary);
        Scanner sc = new Scanner(System.in);
        String target_language = "";
        boolean correct_lang = false;
        while (true) {
            System.out.print("Введите текст, на который вы хотите перевести текст (на Русском): ");
            String preferred_language = sc.nextLine();
            // это поиск кода языка, тут все норм
            for (String lang : lang_dictionary.keySet()) {
                if (lang.toLowerCase().equals(preferred_language.toLowerCase())) {
                    target_language = lang_dictionary.get(lang);
                    correct_lang = true;
                }
            }
            if (correct_lang) {
                break;
            } else {
                System.out.println("К сожалению этот язык не поддерживается или же вы допустили ошибку при вводе, попробуйте еще раз.");
            }
        }
        API_URL = API_URL + target_language;
        System.out.println(API_URL);
        JSONObject text_json = serializeText();
        String POST_DATA = "[" + text_json.toString() + "]";
        readResponse(establishConnection(POST_DATA));
    }

    private static void readLanguageCodes(Map<String, String> map) throws IOException { // читает из файлика коды языков все тоже норм
        Scanner file_scanner = new Scanner(new File(LANG_CODES));
        while(file_scanner.hasNext()) {
            String[] str = file_scanner.nextLine().split("\t", 2);
            map.put(str[1], str[0]);
        }
        file_scanner.close();
    }

    private static JSONObject serializeText() throws IOException { // сериализация текста, все норм
        Scanner text_scanner = new Scanner(new File(TEXT));
        StringBuilder large_text_Anna = new StringBuilder();
        while(text_scanner.hasNextLine()) {
            large_text_Anna.append(text_scanner.nextLine());
        }
        JSONObject text_json = new JSONObject();
        text_json.put("Text", large_text_Anna);
        text_scanner.close();
        return text_json;
    }

    private static HttpURLConnection establishConnection(String POST_DATA) throws IOException{ // вот тут может быть ошибка
        URL url = new URL(API_URL);
        HttpURLConnection urlConnection = (HttpURLConnection) url.openConnection();
        urlConnection.setRequestProperty(Base64.getEncoder().encodeToString(("Ocp-Apim-Subscription-Key:").getBytes(StandardCharsets.UTF_8)), API_KEY);
        urlConnection.setRequestProperty(Base64.getEncoder().encodeToString(("Ocp-Apim-Subscription-Region:").getBytes(StandardCharsets.UTF_8)), API_REGION);
        urlConnection.setRequestProperty(Base64.getEncoder().encodeToString(("Content-Type:").getBytes(StandardCharsets.UTF_8)), "application/json");
        urlConnection.setDoOutput(true);
        OutputStream out = urlConnection.getOutputStream();
        out.write(POST_DATA.getBytes());
        return urlConnection;
    }

    private static void readResponse(HttpURLConnection urlConnection) throws IOException {
//        System.out.println(urlConnection);
        if (urlConnection.getResponseCode() >= 400) {
            System.out.println("Невозможно установить соединение с сервером");
            return;
        }
        Scanner req_reader = new Scanner(urlConnection.getInputStream());
        BufferedWriter file_writer = new BufferedWriter(new FileWriter(TARGET_FILE));
        if (req_reader.hasNextLine()) {
            while(req_reader.hasNextLine()) {
                file_writer.write(req_reader.nextLine());
            }
        } else System.out.println("Ответа от сервера не получено...");
        file_writer.close();
        urlConnection.disconnect();
    }
}