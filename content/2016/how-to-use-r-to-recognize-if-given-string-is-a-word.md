Title: How to use R to recognize if given string is a word
Slug: how-to-use-r-to-recognize-if-given-string-is-a-word
Date: 2016-02-28 19:01:56
Category: Blog
Tags: tutorial, R

StackOverflow user *seakyourpeak* [asked if R can be used to verify whether 
given string is a word in English or not](http://stackoverflow.com/q/34514795/3552063). This is interesting problem that gives us opportunity to explore different kinds of correctness.
<!-- more -->

## Correct answer

This is not possible.

## Longer and incorrect answer

In case you don't find this answer satisfying, you can resort to checking string against dictionary of known English words.
This approach is fundamentally broken, as we will explain later on, but it will work in majority of cases.

First of all, we need a dictionary of "words" that we will match our data against. One such dictionary is compiled by Kevin Atkinson and distributed under open source license at [SCOWL (And Friends)](http://wordlist.aspell.net/) website.

Local copy can be obtained by downloading data file and unzipping it. Distribution package contains plenty of directories, but [README file](http://wordlist.aspell.net/scowl-readme/) says that we can ignore most of them. Our only point of interest is directory called `final` that contains generated words list. 

Words are scattered across multiple files, as they are grouped by variant, category and size. Size can be understood as commonness, or rough probability that everyday English user will **not** be familiar with given word. This structure allows us to use `list.files()` function with `pattern` argument, or `grepl()` function, to pinpoint set of words that we deem correct.

The code below will set up `words` vector with all common English words from scratch. In real-life project you should probably use more persistent storage for words database files.

    #!r
    dict_dir <- tempdir()
    dict_url <- 'http://downloads.sourceforge.net/wordlist/scowl-2016.01.19.zip'
    dict_local_zip <- file.path(dict_dir, basename(dict_url))
    if (! file.exists(dict_local_zip)) {
    	download.file(dict_url, dict_local_zip)
    	unzip(dict_local_zip, exdir=dict_dir)
    }
    
    dict_files <- list.files(file.path(dict_dir, 'final'), full.names=TRUE)
    dict_files_match <- as.numeric(tools::file_ext(dict_files)) <= 60 & grepl("english-", dict_files, fixed = TRUE)
    dict_files <- dict_files[ dict_files_match ]
    
    words <- unlist(sapply(dict_files, readLines, USE.NAMES=FALSE))
    length(words)
<!-- -->

    #!text
    ## [1] 119050

Finally we can verify if string is English word by checking if it exists in vector of known words. The nice thing is that we get vectorization for free.

    #!r
    c("knight", "stack", "selfie", "l8er", "googling", "echinuliform") %in% words
<!-- -->

    #!text
    ## [1]  TRUE  TRUE  TRUE FALSE  TRUE FALSE

Or, instead of downloading archive and reading files, we could just use [`qdapDictionaries`](https://cran.r-project.org/web/packages/qdapDictionaries/index.html) package and load 
`GradyAugmented` dataset. This approach was suggested by another StackOverflow user. Its main benefit is easy integration with current R environment. SCOWL, however, offers more flexibility and larger dictionary.


    #!r
    length(GradyAugmented)
    c("knight", "stack", "selfie", "l8er", "googling", "echinuliform") %in% GradyAugmented
<!-- -->

    #!text
    ## [1] 122806
    ## [1]  TRUE  TRUE FALSE FALSE FALSE FALSE

## Long explanation of correct answer

To answer original question, we must establish some definition of "word".

The naïve approach would say that word is anything that can be found in dictionary, but if we head this direction, things will quickly go south.

The most obvious problem is that dictionaries are not created equal - some have more words than others. Admittedly, this is only small obstacle that can be easily overcome by always using the most complete dictionary available.

But this dictionary will still suffer from the same limitation that all dictionaries do - it is inherently reactive. There is some timespan that passes - must pass - between people starting to use word and dictionary including it. Length of this timespan will depend on how quickly dictionary creator notice that people use the word, decide that it is worth including and issue updated version. In the past, when new issues had to be printed, timespan was long enough that people could actually stop using the word **before** it was included.

Moreover, dictionary creators are people too and they might have certain vision of theirs work purpose. In particular, they seem to be attracted by linguistic prescriptivism for some reason. This point of view greatly extends inclusion timespan and might prevent some words from ever being included. 

By solving these issues, we risk exaggerating in opposite direction - our dictionary might contain words that people never use and often don't even understand. [Dictionary of Unusual Words](http://phrontistery.info/ihlstart.html) is website dedicated to collecting some of these words. In their vast repertory there are gems like "muscariform" and "suaveolent".

Clearly, better definition is needed.

Let's say that word is the smallest element of language that has a meaning (by the way, [Wikipedia says that word is pretty much that](https://en.wikipedia.org/wiki/Word)). This instantly solves problems of missing fresh words and including ones that nobody understands. It also avoids pitfall of appealing to social actors that might be biased; or does it?

If we agree on that definition and try to apply it, we will find ourselves asking "what does that string mean, if anything?". It doesn't take careful consideration to see that this is only illusive solution - all we have done is shifting attention from definition of "word" to definition of "meaning".

In [spirit of late Wittgenstein](http://existentialcomics.com/comic/90), we could say that meaning of word can only be understood by how community of word-users participates in activities involving this word. While this definition has undeniable charm, it leads us back to social actors defining what is and what isn't a word (by specifying whether something has a meaning or not). Except that this time it's even worse.

For starters, community of word-users might as well be anonymous crowd with ambiguous boundaries. It's not exactly environment that promotes consensus.

Furthermore, community of word-users is usually subset of community of interest. This is clearest in academia, where freshmen are interested in some field, but haven't yet internalized language of that field. But sometimes people use words outside of their original context and community of word-users becomes orthogonal to community of interest. These pose substantial practical challenges, as groups of interest are easier to reach out than groups of word-users, but we risk reaching out wrong people.

Overall, Wittgenstein-inspired definition leads to rather uncomfortable situation where the same string is and isn't a word, depending on chosen reference frame of community. Basically all jargon and specialist terminology fall into that category, but slang-, dialect- and cant-specific words do as well. One of my favorite examples is *bootstrapping* - it is hard to comprehend for people without proper background, it means different things in statistics and computer science, and it has **few different meanings** in second one.

Finally, thanks to human mind astonishing ability to infer meaning from broadly defined context, there are odd cases when we are positive that something is a word, but we don't know its meaning. *Jabberwocky* is full of those. But since it does follow grammar rules, we are still able to get general idea what it is about.

As you should have realized by now, the main issue in using computer to verify if given string is a word in English or not is not in computational complexity of problem or limited resources, but in coming up with highly specific and sensitive algorithm. We intuitively know what words are and can recognize them among random characters, but coming up with strict and precise definition is extremely hard.

**Takeaway message**: there are different levels of correctness, in the same way that there is a difference between statistical and practical significance. Fundamentally or substantially incorrect solutions might actually solve all practical problems, so they might be good enough after all.
