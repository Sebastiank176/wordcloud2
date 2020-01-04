library(shiny)
library(tm)
library(wordcloud)
library(memoise)

text <- readLines("Rohdaten.txt", encoding="UTF-8")

# Using "memoise" to automatically cache the results
getTermMatrix <- memoise(function(roh) {
    
    myCorpus = Corpus(VectorSource(text))
    myCorpus = tm_map(myCorpus, content_transformer(tolower))
    myCorpus = tm_map(myCorpus, removePunctuation)
    myCorpus = tm_map(myCorpus, removeNumbers)
    myCorpus = tm_map(myCorpus, removeWords,
                      c(stopwords("SMART"), "thy", "thou", "thee", "the", "and", "but"))
    myCorpus = tm_map(myCorpus, removeWords,
                      c(stopwords("german"), "bechtle"))    
    myDTM = TermDocumentMatrix(myCorpus,
                               control = list(minWordLength = 1))
    
    m = as.matrix(myDTM)
    
    sort(rowSums(m), decreasing = TRUE)
})

