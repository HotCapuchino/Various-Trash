from Speakers import Speakers
from Authorizer import Authorizer
from VoiceSynthesizer import Synthesizer
from Calculate import calculateAmountOfLetters
from Calculate import calculateDurationOfAudio

file_name = input("Enter name of the file, you want to be synthesized: ")
try:
    with open("res/" + file_name, encoding='utf-8') as f:
        auth = Authorizer()
        auth.auth()
        token = auth.getToken()
        print(token)
        speakers = Speakers()
        speakers.fetchLanguages(token=token)
        speakers_list = speakers.getLanguages()
        lang_dictionary = {}
        for i in speakers_list:
            lang_dictionary.update({i["DisplayName"]: i["Locale"]})
        for i in lang_dictionary.keys():
            print(i, " - ", lang_dictionary.get(i))
        chosen_language = ""
        chosen_object = None
        while True:
            user_input = str(input("Choose the name or a language from the list above: "))
            counter = 0
            for i in lang_dictionary.keys():
                if user_input == i or user_input == lang_dictionary.get(i):
                    chosen_language = lang_dictionary.get(i)
                    chosen_object = speakers_list[counter]
                    break
                counter += 1
            if chosen_language:
                break
            else:
                print("Please enter valid name or language!")
        file_str = ""
        text_to_be_synthesized = ""
        while True:
            file_str = f.readline()[:-1]
            if file_str == " " or file_str == "":
                break
            text_to_be_synthesized += file_str
        user_prefferences = {}
        user_prefferences.update({"lang": chosen_object["Locale"]})
        user_prefferences.update({"gender": chosen_object["Gender"]})
        user_prefferences.update({"name": chosen_object["ShortName"]})
        user_prefferences.update({"text": text_to_be_synthesized})
        synth = Synthesizer(user_prefferences)
        response = synth.getAudio(token=token)
        if response == -1:
            print(response)
        else:
            with open("res/" + file_name.split(".")[0] + ".wav", "wb") as output:
                output.write(response)
            output.close()
            amount_of_letters = calculateAmountOfLetters("res/" + file_name)
            duration = calculateDurationOfAudio("res/" + file_name.split(".")[0] + ".wav")
            print("Duration per letter: ", duration / amount_of_letters, " sec")
        f.close()
except FileNotFoundError:
    print("File can't be found!")
