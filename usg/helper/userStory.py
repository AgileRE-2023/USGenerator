import nltk
import spacy 
import pickle

nltk.download('punkt')
nltk.download('universal_tagset')
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')
nltk.download('tagsets')
nltk.download('omw-1.4')


nlp = spacy.load("en_core_web_sm")

def detect_subject(sentence):
    doc = nlp(sentence)
    subjects_dep = [token.text for token in doc if "subj" in token.dep_]
    subjects_ner = [ent.text for ent in doc.ents if ent.label_ == "PERSON"]
    who_set = set(subjects_dep + subjects_ner)
    who = list(who_set)
    return who
def hapus_who_redundan(data_list):
    data_list_copy = data_list.copy()
    for kata in data_list_copy:
        for kata_lain in data_list_copy:
            if kata != kata_lain and kata.lower() in kata_lain.lower():
                if len(kata) == len(kata_lain):
                    x=0  
                elif len(kata) < len(kata_lain):
                    data_list.remove(kata)
                    break  
                else:
                    data_list.remove(kata_lain)
                    break 
    while "that" in data_list:
        data_list.remove("that")
def parse_aspect_of_what(word_tokens):
    WHAT_phrases = []
    grammar_what = r'''
         WHAT: {(<ADJ|VERB>+<.|PRT|ADP|CONJ|PRON>*<DET>*<NOUN|ADV>+)+}
    '''
    chunkParser = nltk.RegexpParser(grammar_what)
    tagged = nltk.pos_tag(word_tokens, tagset='universal')
    tree = chunkParser.parse(tagged)
    for subtree in tree.subtrees():
        if subtree.label() in ['WHAT']:
            what = []
            for leave in subtree.leaves():
                what.append(leave[0])
            token = [w for w in what]
            what_phrase = ' '.join(token)
            if len(token) > 0:
                WHAT_phrases.append(what_phrase)
    return WHAT_phrases

def why_selector(sentence):
    sentences = nltk.sent_tokenize(sentence)
    why_target = ['for ', 'so that ', 'in order to ']
    following_sentences = []
    for target in why_target:
        for sent in sentences:
            if target in sent:
                index_target = sent.index(target)
                following_sentence = sent[index_target + len(target):]
                following_sentences.append(following_sentence)
    return following_sentences if following_sentences else None

def hapus_nilai_yang_terkandung(what, why):
    what = [elemen_what for elemen_what in what if not any(elemen_what in elemen_why for elemen_why in why)]
    return what


class UserStory:

    def nlp_userstory(self, ValuePar):
        input_text = ValuePar 
        input_text = input_text.lower()
        kalimat = nltk.sent_tokenize(input_text)
        useStoryVal = []

        for sentence in kalimat:
            word_tokens = nltk.word_tokenize(sentence)
            what_phrases = parse_aspect_of_what(word_tokens)
            who = detect_subject(sentence)
            hapus_who_redundan(who)
            why = why_selector(sentence)
            what = hapus_nilai_yang_terkandung(what_phrases, why)
            who = list(set(who))
            why = list(set(why))
            what = list(set(what))
            useStoryVal.append({'who' : who, 'what' : what, 'why' : why})
            print("Kalimat:", sentence)
            print("Aspect of Who:", who)
            print("Aspect of What:", what)
            print("Aspect of Why:", why)
            print("-----")

        return useStoryVal

model = UserStory()
filename = "model.sav"
pickle.dump(model, open(filename,'wb'))
