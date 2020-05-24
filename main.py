# -*- coding: utf-8 -*-

import os
import pickle
import thesisfunctions as tf
from nltk.corpus import big_data_manlog, big_data_manuf, big_data_logist
from nltk.tokenize import sent_tokenize

sourcesLM = os.listdir(r"C:\Users\daniyar.abdimomunov\AppData\Roaming\nltk_data\corpora\big_data_manlog")
sourcesM = os.listdir(r"C:\Users\daniyar.abdimomunov\AppData\Roaming\nltk_data\corpora\big_data_manuf")
sourcesL = os.listdir(r"C:\Users\daniyar.abdimomunov\AppData\Roaming\nltk_data\corpora\big_data_logist")

export_dir = r"C:\\Users\\daniyar.abdimomunov\\Desktop\\"

sample_manlog = []
sample_logist = []
sample_manuf = []

#----- Processing Literature realted to both Manufacturing and Logistics -----#

print('\nProcessing: loading "common" sources')
for source in sourcesLM[:]:
    a = big_data_manlog.raw(source)
    #a_lower = a.lower()
    a_tokenized = sent_tokenize(a) #sent_tokenize(a_lower)
    print("Loading file: " + source)
    for s in a_tokenized:
        sample_manlog.append(s)
print('\nCompleted:  "shared" sources loaded\n')

for s in sample_manlog:
    sample_logist.append(s)
    sample_manuf.append(s)

#----- Processing Literature realted to Logistics specifically -----#
print('\nProcessing: loading "logistics" sources')
for source in sourcesL[:]:
    a = big_data_logist.raw(source)
    #a_lower = a.lower()
    a_tokenized = sent_tokenize(a) #sent_tokenize(a_lower)
    print("Loading file: " + source)
    for s in a_tokenized:
        sample_logist.append(s)
print('\nCompleted:  "logistics" sources loaded')

sampleL_filt = tf.filter_tokenizedS(sample_logist)
#fail-saves; saves (pickles) output in case of crash
#file1 = open(r"C:\\Users\\daniyar.abdimomunov\\Desktop\\sampleL_filt.txt", "wb")
#pickle.dump(sampleL_filt, file1)
#file1.close()

sampleLf_sents = tf.Sentlist_tokenizedS(sampleL_filt)
#file2 = open(r"C:\\Users\\daniyar.abdimomunov\\Desktop\\sampleLf_sents.txt", "wb")
#pickle.dump(sampleLf_sents, file2)
#file2.close()

noun_phrasesLf = tf.parsebyChunk_Sentlist(sampleLf_sents, 'NP')
#file3 = open(r"C:\\Users\\daniyar.abdimomunov\\Desktop\\noun_phrasesLf.txt", "wb")
#pickle.dump(noun_phrasesLf, file3)
#file3.close()

tf.exportfdist(noun_phrasesLf, 1000, "FDist Logistics", export_dir,  2)

#----- Processing Literature related to Manufacturing specifically -----#

print('\nProcessing: loading "manufacturing" sources')
for source in sourcesM[:]:
    a = big_data_manuf.raw(source)
    #a_lower = a.lower()
    a_tokenized = sent_tokenize(a) #sent_tokenize(a_lower)
    print("Loading file: " + source)
    for s in a_tokenized:
        sample_manuf.append(s)
print('\nCompleted:  "manufacturing" sources loaded')

sampleM_filt = tf.filter_tokenizedS(sample_manuf)
#fail-saves; saves (pickles) output in case of crash
#file4 = open(r"C:\\Users\\daniyar.abdimomunov\\Desktop\\sampleM_filt.txt", "wb")
#pickle.dump(sampleM_filt, file4)
#file4.close()


sampleMf_sents = tf.Sentlist_tokenizedS(sampleM_filt)
#file5 = open(r"C:\\Users\\daniyar.abdimomunov\\Desktop\\sampleMf_sents.txt", "wb")
#pickle.dump(sampleMf_sents, file5)
#file5.close()

noun_phrasesMf = tf.parsebyChunk_Sentlist(sampleMf_sents, 'NP')
#file6 = open(r"C:\\Users\\daniyar.abdimomunov\\Desktop\\noun_phrasesMf.txt", "wb")
#pickle.dump(noun_phrasesMf, file6)
#file6.close()

tf.exportfdist(noun_phrasesMf, 1000, "FDist Manufacturing", export_dir,  2)

print("I LOVE YOU! <3")