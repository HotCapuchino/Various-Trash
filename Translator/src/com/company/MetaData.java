package com.company;

public class MetaData {
    private static final String API_KEY = "Your subscription key here";
    private static final String API_REGION = "Your region here";
    private static final String API_URL_TRANSLATION = "https://api.cognitive.microsofttranslator.com/translate?api-version=3.0&to=";
    private static final String API_URL_LANGUAGES = "https://api.cognitive.microsofttranslator.com/languages?api-version=3.0";
    private static final String TEXT = "src/res/text.txt";

    public static String getAPI_KEY() {
        return API_KEY;
    }

    public static String getAPI_REGION() {
        return API_REGION;
    }

    public static String getAPI_URL_TRANSLATION() {
        return API_URL_TRANSLATION;
    }

    public static String getAPI_URL_LANGUAGES() {
        return API_URL_LANGUAGES;
    }

    public static String getTEXT() {
        return TEXT;
    }
}
