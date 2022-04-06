def doc_to_cloud(doc_location, stem):
    
    """
    The function takes in a pdf file and the preference to use stemmed text or tokenized text 
    
    The return is a word cloud of the desired document
    
    """
        
    numPages = getPageCount(doc_location)
    
    text_total = " "
    for i in range(numPages):
        text = extractData(doc_location, i)
        text_total = text_total+text

    # remove special charachters 
    text_total = remove_special(text_total)
    
    #create a lower case words
    text_total = text_total.lower()
    
    
    #Tokenize 
    text_total = word_tokenize(text_total)
    
    
    # stemming
    stemmed_text = []
    porter = PorterStemmer()
    for x in text_total:
        x = porter.stem(x)
        stemmed_text.append(x)
        
    
    #declare global variable to be used for the word count plot latter
    global text_total_tocloud
    
    #condition to decide if use tokenized text or stemmed text 
    if stem == 1:
        text_total_tocloud = stemmed_text
    else:
        text_total_tocloud = text_total
    
    # join total text in a single sentence
    text_total_tocloud = " ".join(text_total_tocloud)
    
    
    # create a wordCloud
    # visualization of the stemmed sentences

    wordcloud_low = WordCloud( width = 800, height = 500, random_state = 24,
                             max_font_size = 100).generate(text_total_tocloud)
    plt.figure(figsize=(15,8))
    plt.axis('off')
    plt.imshow(wordcloud_low)
    plt.tight_layout(pad = 0)
    plt.show()


def plot_of_counts(text, plot_title, number_of_repeats_to_ignore):
    
    #create the word counts dictionary of the analyzed text
    word_count_dic = word_count(text)
    
    # create a dataframe of the dictionary 
    total_text_count = pd.DataFrame.from_dict(word_count_dic, orient ='index')
    
    # reset index of the dataframe
    total_text_count.reset_index(inplace = True)
    
    # rename dataframe columns
    total_text_count.columns = ['word', 'word count']
    
    
    #choose only words that are repeated more than x times
    total_text_count_x = total_text_count[total_text_count['word count']>number_of_repeats_to_ignore]
    
    # sort values
    total_text_count_x = total_text_count_x.sort_values('word count',  ascending=False)
    
    #plot the outcome
    word_count_plot(total_text_count_x, plot_title)
    
    
