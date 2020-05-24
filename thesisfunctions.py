# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 01:29:08 2020

@author: Daniyar.Abdimomunov
"""

def filter_tokenizedS(text_tokenizedS):
    
    #filters stop words out of text 
    #text_tokenizedS is a list of 
    
    from nltk.corpus import stopwords
    from nltk.tokenize.treebank import TreebankWordDetokenizer
    from nltk.tokenize import word_tokenize
    from nltk.tag import pos_tag
    
    detokenizer = TreebankWordDetokenizer()
    
    stop_words = set(stopwords.words('english'))
    
    stopwords_academia = ['paper', 'papers', 'research', 'study', 'studies', 'findings', 'finding', 'report', 'reports', 'summary', 'literature', 'review', 'proceedings',  
                          'vol', 'journal', 'journals', 'publication', 'publications', 'publish', 'published', 'issue', 'article', 'articles', 'edition', 'editions', 'ed', 'ed.', 'eds', 
                          'author', 'authors', 'researcher', 'researchers', 'editor', 'editors',  'university', 'universities', 'college', 'colleges', 'institute', 'committee', 'committees', 
                          'table', 'tables', 'figure', 'figures', 'example', 'examples', 'e.g', 'e.g.', 'eg', 'fig', 'fig.', 'figure', 'figures',
                          'title', 'theory',    'introduction', 'conclusion', 'conclusions', 'chapter','results', 'section', 'annex', 'appendix', 'index', 'glossary', 'addition', 
                          'citations', 'citation', 'cite', 'cited', 'cf', 'cf.', 'reference', 'references', 'ref', 'et', 'al', 'al.', 'source', 'sources', 
                          'methodology', 'methodologies', 'methods', 'interview', 'interviews', 'survey', 'surveys', 'participant', 'participants', 'sample', 'scope',
                          'page', 'pages', 'pp', 'keywords', 'keyword', 'abstract', 'note', 'notes',
                          'science', 'scientific', 'sci', 'chem', 'physics', 'phys', 'ecol', 'clin', 'biol', 'clim', ]
    stopwords_alphanumeric = ['a.', 'a', 'b.', 'b', 'c.', 'c', 'd.', 'd', 'e.', 'e',  'f.', 'f', 'g.', 'g', 'h.', 'h', 'i.', 'i', 'î¸', 'j.', 'j', 'k.', 'k', 
                          'l.', 'l', 'm.', 'm', 'n.', 'n', 'o.', 'o', 'p.', 'p', 'q.', 'q', 'r.', 'r', 's.', 's', 't.', 't', 'u.', 'u', 
                          'v.', 'v', 'w.', 'w', 'x.', 'x', 'xx', 'xxx', 'xxxx', 'y.', 'y', 'z.', 'z', 'c.-h', '-h', 'z|x',
                          'b.a', 'bd', 'b.k', 'ci',  'c.m.', 'c.m', 'd.a', 'dc', 'd.g.', 'd.g', 'd.j', 'd.j.', 'd.m', 'd.m.', 'd.p', 
                          'e.j.', 'e.j', 'eq', 'j.a', 'j.a.', 
                          'k.m', 'k.m.', 'm.a', 'm.a.', 'm.b', 'm.c', 'm.d', 'm.d.', 'md','mi', 'mm', 'm.s', 'ms', 
                          'pa', 'p.j.', 'p.j', 'r.j.', 'r.j', 's.h', 'si','s.j', 's.j.', 
                          '%', '//', '=(', '<0.001', '<0.',
                          'Åº', 'Ã¢Å¡', 'Å¡', 'Ë‡',  'âš', '\u010f', r'ď\x82ˇ', 'ď\x82ˇ',  '-', '--', '', 
                          'ďź\x81ndings', '1â\x80\x9393',
                          'â\x88\x921', 'â\x8cšhttps','â\x88\x91', 'Ä\x89', 'Ä\x89',  'Ä\x89', 'â\x88\x92', 'â\x88\x86t', 'â\x80\x93', 'â\x80ś', 'ď\x82ˇ','ďź\x81rms', 'â\x80˘','îą', 'â\x80\x9d',
                          'î¸ě\x82', 'e29\xad141', '3\xad5',  ]
    stopwords_misc = ['address', 'addresses', 'farmers', 'farmer', 'businesses', 'firms', 'company', 'others', 'mater', 'assay', 'assays', 'way', 'today', 
                      'eng', 'engl', 'english',
                      'date', 'year', 'years', 'time',  'name', 'names',  
                      'things', 'thing', 'stuff', 
                      'xxx\xadxxx', 'klerkx', 'cnvs', 'egfr', 'exon', 'lett','ones',  'proc', 'snvs', '\xad',  
                      'den', 'der', 'des', 'dna','inc', 'inc.', 'inf', 'int', 'int.', 'msi', 'ngs', 'one', 'res', 'rev', 'soc', 'sun', 'van', 'way', 'yrs',       
                      'coll', 'procedia', 'direct', 'cirp', 
                      'ie', 'i.e', 'i.e.', 'etc', 'etc.', 'ii', 'iii', 'iv', 'vi',
                      'http', 'https', '//www', 'www', 'e-mail', 'email', 'url',
                      'www.sciencedirect.com',
                      'procedia', 'elsevier', 'ltd', 'ieee', 'trans',  
                      '//creativecommons.org/licenses/by-nc-nd/4.0/', '//creativecommons.org/licenses/by/4.0/','//creativecommons.org/licenses/by-nc-nd/3.0/', 
                      'doi', '//doi', '//dx.doi', '//dx.doi.org/', '//doi.org/', '//doi.org/10', '//doi.org/10.1016/j.heliyon.2018.e00588', '//dx.doi.org/10.1016/j',
                      'www.elsevier.com/locate/procedia', 'the jmd.amjpathol.org', ]
    stopwords_loc = ["us", "usa", "united", "states",  "london", "cambridge",  "boston", 
                     "uk", "kingdom", "york", "germany", "europe", "european", "comission",   
                     "australia", "france", "tx", "canada", "eu", "india", "china", "netherlands", "italy", 
                     "washington", "san", "diego", "philadelphia", "brazil", "california", "spain", "eur", ]                     
    stopwords_time = ["january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december", ]
    stopwords_names = ["kim", "bukov", "zhang", "lett", "li", "lee", "kim", "yang", 
                       'johnson',  "deloitte", "jones", "van", "pa", "hu", "xu", "mehta", "midgley", 
                       "guo", "thomas", "taylor", "cao", "gupta", "cheng", "yin", "gao", "zeng", 
                       "zhao", "zhou", "xi", "zhu", "song", "springer", "qi", "lu", "lin", "yi", 
                       "chang", "zhu", "indels", "huang", "liu", "yu", "sanger", "susha", 'springer', 
                       "jiang", "choi", "newman", "kumar", "rumson", "davis", "hinton", "david", 
                       "wei", "von", "adner", "walker", "martin", "hashem", "mikalef", "zheng", 
                       "xie", "turner", "michael", "du", "verhoef",  "mckinsey",  ]
    new_stopwords = stopwords_academia + stopwords_alphanumeric + stopwords_misc + stopwords_loc + stopwords_names + stopwords_time
    for w in new_stopwords:
        stop_words.add(w)
    stop_pos = ["NNP", "NNPS", "PRP", "PRP$", "WDT", "WP", "WP$", "DT"]
    
    print("Processing: filtering text")
    
    text_tokenizedW = []
    filt_text = []
    for s in text_tokenizedS:
        word_tokenized = word_tokenize(s)
        word_filt = []
        
        for w in pos_tag(word_tokenized):
            if not w[1] in stop_pos: 
                if not w[0].lower() in stop_words:
                    word_filt.append(w[0].lower())
        text_tokenizedW.append(word_filt)
    
    for s in text_tokenizedW:
        filt_text.append(detokenizer.detokenize(s))
      
    #sample1_tokenizedw = []

    #for s in sample1:
    #    word_tokenized = word_tokenize(s)
    #    word_filt = []
    #    for w in word_tokenized:
    #        if not w in stop_words:
    #            word_filt.append(w)
    #    sample1_tokenizedw.append(word_filt)

        
    #sample1_filt = []
    #for s in sample1_tokenizedw:
    #    sample1_filt.append(detokenizer.detokenize(s))
        
    print("Completed:  text filtered")
    return filt_text


def Sentlist_tokenizedS(text_tokenizedS):
    
    from pattern.en import Sentence, parse
    
    print("Processing: tokenizing text by sentence")
    Sent_list = []
    for e in text_tokenizedS:
        s = parse(e, lemmata=False, chunks = True)
        s = Sentence(s)
        Sent_list.append(s)
    print("Completed:  text tokenized by sentence")
    return Sent_list

def parsebyChunk_Sentlist(Sent_list, chunk_tag):
    
    #from nltk.corpus import stopwords
    
    print("Processing: filtering text by NP (noun phrase) chunks")
    
    #stop_words = set(stopwords.words('english'))
    
    #for w in new_stopwords:
    #    stop_words.add(w)

    noun_phrases = []
    
    for s in Sent_list:
        sent_chunks = s.chunk
        for c in sent_chunks:
            if chunk_tag in c.tag:
                noun_phrases.append(c.string)
    print("Completed: text filetered by NP chunks")
    return noun_phrases

def exportfdist(noun_phrases, size=250, filename="Frequency Distribution", export_dir="", doc_type=0):
    
    #type = strucutre of document exported [0, 1, or 2]. 
    #   0 = list as csv
    #   1 = structred text document
    #       |--------------------------------------------------
    #           Frequency [200]:  ('data', 254); 
    #       |--------------------------------------------------
    #           Frequency [100]:  ('big data', 154); 
    #       |--------------------------------------------------
    #   2 = exports both as separate files
    
    from nltk.probability import FreqDist
    
    if (export_dir == ""):
        print('Please specify path of directory where you want your files to be saved.\n' +
              'Example: export_dir = r"C:\\Users\\daniyar.abdimomunov\\Desktop\\" ')
        return
    
    
    #export_dir = r"C:\Users\daniyar.abdimomunov\Desktop\\"
    fdist = FreqDist(noun_phrases)
    most_common = fdist.most_common(size)
    print("\n Frequency Distrubition (" + str(size) +")" + 
          str(most_common) + 
          "\n")
    

    if (doc_type == 0) or (doc_type == 2):
        file_path = export_dir + filename + " (list).csv"
        file = open(file_path, "w", encoding="utf-8")
        
        for i in most_common:
            file.write(i[0]+ "," +str(i[1])+ "\n")
        
        print("Exporting to: " + file_path)
        file.close()
        if (doc_type == 0):
            return
        elif (doc_type == 2):
            doc_type = 1
    
    if (doc_type == 1):
        file_path = export_dir + filename + " (structured).txt"
        file = open(file_path, "w", encoding="utf-8") 
    
    
        maxfreq = fdist.most_common(1)[0][1]
        #print("\nMaxfreq: " + str(maxfreq))
        scales = range(6) #<------ magnitude of scale. 6 = scale limited to 10^6 or 100,000 
        for s in scales:
            interval = 10**(s)
            if maxfreq > interval:
                maxinterval = int(maxfreq/interval) * interval
                scaleinterval = interval
        #print("Max interval: " + str(maxinterval) + 
        #      "\nScale interval: " + str(scaleinterval))

        mi = maxinterval
        si = scaleinterval
        scale = []
        while si >= 1:
            if mi > si:
                scale.append(mi)
                mi -= si
            elif mi > 1:
                si = int(si/10)
            else: 
                scale.append(mi)
                si = int(si/10)
            

        file.write("+---------------------------------------------------------------\n")
        for s in range(len(scale)):
            file.write("   Frequency ["+ str(scale[s]) + "]:  ")
            for i in most_common:
                if s == 0 and (i[1] >= scale[s]):
                    file.write(str(i) + "; ")
                elif (i[1] >= scale[s]) and (i[1] < scale[s-1]):
                    file.write(str(i) + "; ")
            file.write("\n+---------------------------------------------------------------\n")
            
        file.close()
    
        print("Exporting to: " + file_path)
        return
