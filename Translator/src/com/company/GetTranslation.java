package com.company;

import com.google.gson.Gson;
import com.google.gson.reflect.TypeToken;
import okhttp3.*;

import java.io.IOException;
import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.Map;

public class GetTranslation {
    static OkHttpClient client = new OkHttpClient();

    public static String getTranslation(String text_to_be_translated, String chosen_lang) throws IOException {
        MediaType mediaType = MediaType.parse("application/json");
        RequestBody requestBody = RequestBody.create(mediaType, "[{\"Text\":\"" + text_to_be_translated + "\"}]");
//        System.out.println(requestBody.);
        Request request = new Request.Builder()
                .url(MetaData.getAPI_URL_TRANSLATION() + chosen_lang).post(requestBody)
                .addHeader("Ocp-Apim-Subscription-Key", MetaData.getAPI_KEY())
                .addHeader("Ocp-Apim-Subscription-Region", MetaData.getAPI_REGION())
                .addHeader("Content-type", "application/json").build();
        Response response = client.newCall(request).execute();
        return response.body().string();
    }

    public static String serializeResponse(String text_json) {
        Gson gson = new Gson();
        Type type = new TypeToken<ArrayList<Map<String, Object>>>(){}.getType();
        ArrayList<Map<String, Object>> json = gson.fromJson(text_json,type);
        return ((ArrayList<Map<String, String>>)json.get(0).get("translations")).get(0).get("text");
    }
}
