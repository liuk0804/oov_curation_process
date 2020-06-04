import ekphrasis
from ekphrasis.classes.preprocessor import TextPreProcessor
from ekphrasis.classes.tokenizer import SocialTokenizer, Tokenizer

# custom dictionary
from local_dict.emoticons import emoticons
from local_dict.slangdict2 import slangdict

from nltk.stem.snowball import SnowballStemmer
stemmer = SnowballStemmer(language='english')

import pandas as pd
import numpy as np
import pickle

import enchant
d = enchant.Dict("en_US")
import string
import unicodedata
social_pipeline = [
        "EMOJI", "URL", "TAG", "EMAIL", "USER", "HASHTAG",
        "CASHTAG", "PHONE", "PERCENT", "MONEY", "DATE", "TIME",
        "ACRONYM", "CENSORED", "EMPHASIS", "NUMBER", "WORD" ]

simple_proc = TextPreProcessor(tokenizer = Tokenizer().tokenize,)

text_processor = TextPreProcessor(
    fix_text = True, # fix unicode error

    # pre-defined custom dictionary
    dicts=[emoticons, slangdict],
    
    # replace token into <tag> using Regex pattern
    normalize=['email', 'percent', 'money', 'phone', 'user',  'time', 'url', 'date', 'hashtag'],
    # turn token into (word, <tag>) tuple
    annotate= {'allcaps', 'elongated', 'repeated','emphasis', 'censored'},
    
    
    # for word segmentation 
    segmenter="twitter", 
    # for spell correction base on corpus statistics
    corrector="twitter", 
    
    unpack_contractions= True,  # Unpack contractions (can't -> can not)
    unpack_hashtags = False,
    spell_correct_elong= True,  # spell correction for elongated words

    tokenizer = SocialTokenizer(lowercase=True, pipeline = social_pipeline).tokenize,
)


with open('local_dict/emoticon_lst_all.pkl', 'rb') as f:
    emo_lst = pickle.load(f)
with open('local_dict/slang.pkl', 'rb') as f:
    slang_lst = pickle.load(f)


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
 
    try:
        
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass
 
    return False

def en_word(word):
    if is_number(word):
        return False
    elif word in string.punctuation:
        return False
    elif word in slang_lst:
        return False
    elif word in emo_lst:
        return False
    elif '<' in word:
        return False
    elif d.check(word):
        return True
    
def not_en_word(word):
    try:

        if d.check(word):
            return False
        if is_number(word):
            return False
        elif word in string.punctuation:
            return False
        elif word in slang_lst:
            return False
        elif word in emo_lst:
            return False
        elif '<' in word:
            return False
        else:
            return True
    except ValueError:
        pass

def filter_OOV_token(oov_type, listOfElems):
    try:
        indexPosList = [ i-1 for i in range(len(listOfElems)) if listOfElems[i] == oov_type ]
        return [listOfElems[index] for index in indexPosList]
    except ValueError as e:
        pass


def Social_message_curation(msg = "loovvvessss coofffeeeeee......" ):
    # msg = input("Input a sample message: ") or  "loovvvessss coofffeeeeee......"    
       
    print('')
    print('start processing...')
    simple_tok = simple_proc.pre_process_doc(msg)
    tokenized = ' '.join(text_processor.pre_process_doc(msg)).lower().split(' ')
    word_token = [i for i in tokenized if not (('<' in i) or (i in string.punctuation))]

    print('Raw Message Inputed:', msg)
    print('Standard NLP:', simple_tok)
    print('Aggresive/Advanced NLP:', word_token)
    print('OOV-curated NLP process:', tokenized)


    df = pd.DataFrame({'message': [msg]})
    df['tokenize'] = df.message.apply(text_processor.pre_process_doc)\
                               .apply(lambda x: ' '.join(x).lower().split(' '))
    df['simple_tokenize'] = df.message.apply(simple_proc.pre_process_doc)\
                               .apply(lambda x: ' '.join(x).lower().split(' '))
    df['en_IV'] = df.tokenize.apply(lambda x: list(filter(en_word, x)))
    df['en_IV'] = df['en_IV'].apply(lambda x: [stemmer.stem(word) for word in x])


    # df['allcap_oov'] = df.tokenize.apply(lambda x: filter_OOV_token('<allcaps>', x))
    df['slang_oov'] = df.tokenize.apply(lambda x: filter_OOV_token('<slang>', x))
    df['emoji_oov']  = df.tokenize.apply(lambda x: filter_OOV_token('<emoji>', x))
    df['elongated_oov']  = df.tokenize.apply(lambda x: filter_OOV_token('<elongated>', x))
    df['repeated_punct']  = df.tokenize.apply(lambda x: filter_OOV_token('<repeated>', x))

    df['misc_OOV'] = df.tokenize.apply(lambda x: list(filter(not_en_word, x)))

    df2 = df[['en_IV','slang_oov','emoji_oov','elongated_oov','repeated_punct','misc_OOV']].transpose()
    df2.columns = ['Captured_OOV']
    df2['OOV_Count'] = df2.Captured_OOV.apply(len)

    print(df2)
