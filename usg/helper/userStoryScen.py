import nltk
import re
import pickle

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

def when(sentence):
    words = nltk.word_tokenize(sentence)
    tags = nltk.pos_tag(words)
    for i in range(len(tags) - 1):
        if tags[i][1].startswith('VBP') and tags[i + 1][1].startswith('VBG'):
            return False
        elif tags[i][1].startswith('VBD'):
            return False 
        elif tags[i][1].startswith('VBP') and tags[i + 1][1].startswith('VBN'):
            return False
    if any(tag[1].startswith('VB') and not tag[1].startswith('VBG') and not tag[0].lower() == 'will' for tag in tags):
        return True
    return False


def then(sentence):
    future_tense_text = sentence
    matches = re.findall(r'(?:will|shall|should)\s(.*?)[,\.]', future_tense_text)
    if matches:  # Check if there are matches
        return matches[0].strip()  # Return the first match
    else:
        return None
def hapus_nilai_yang_terkandung(when, then):
    when = [elemen_when for elemen_when in when if not any(elemen_when in elemen_then for elemen_then in then)]
    return when
class userStoryScena():
    def nlp_UserStoryScenario(self, input_text):
        paragraph = input_text
        paragraph = paragraph.replace(',', '.')
        paragraph = paragraph.lower()
        sentences = nltk.sent_tokenize(paragraph)
        scenario = []
        index = 0  # Initialize index outside the loop
        synonyms = ["precondition", "requirement", "prerequisite",]
        prev_key = None
        while index < len(sentences):
            sentence = sentences[index]
            if index == 0 or any(synonym in sentence for synonym in synonyms):
                for synonym in synonyms:
                    sentence = sentence.replace(f"There is another {synonym}, ", "")
                scenario.append({"given": sentence})
                prev_key = "given"
            elif when(sentence):
                scenario.append({"when": sentence})
                prev_key = "when"
            
            if then(sentence):
                # Remove the "then" key-value pair if the previous key was "given"
                if prev_key != "given":
                    scenario.append({"then": sentence})
            index += 1
        scenario_final = scenario.copy()
        for dat in scenario:
            if "when" in dat and any(dat["when"] == item.get("then", "") for item in scenario_final):
                scenario_final.remove(dat)

        for dat in scenario_final:
            print(dat)
        for data in scenario_final:
            if "given" in data:
                print(data["given"])
            if "when" in data:
                print(data["when"])
            if "then" in data:
                print(data["then"])
        return scenario_final
    

modelScen = userStoryScena()

filename = "modelScenario.sav"
pickle.dump(modelScen, open(filename,'wb'))