package com.company;

import java.io.*;
import java.util.*;
import com.google.gson.*;
import com.google.gson.internal.LinkedTreeMap;
import com.google.gson.reflect.TypeToken;
import okhttp3.*;
import java.lang.reflect.Type;

public class AvailableLanguages {
    static OkHttpClient client = new OkHttpClient();

    public static String getAvailableLanguages() throws IOException {
        Request request = new Request.Builder()
                .url(MetaData.getAPI_URL_LANGUAGES()).get()
                .addHeader("Content-type", "application/json").build();
        Response response = client.newCall(request).execute();
        return response.body().string();
    }

    public static Map<String, String> jsonParser(String text_json) {
        Gson gson = new Gson();
        Type type = new TypeToken<Map<String, Object>>(){}.getType();
        Map<String, String> lang_codes = new HashMap<String, String>();
        Map<String, Object> json = gson.fromJson(text_json,type);
        LinkedTreeMap<String, Object> translation = (LinkedTreeMap<String, Object>)json.get("translation");
        for (String key : translation.keySet()) {
            lang_codes.put(key, ((LinkedTreeMap<String, Object>)translation.get(key)).get("name").toString());
        }
        return lang_codes;
    }
}
