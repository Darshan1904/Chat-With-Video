import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize

# Download necessary nltk data files
nltk.download('punkt')
nltk.download('stopwords')

def summarize_text(text, num_sentences=5):
    stop_words = set(stopwords.words("english"))
    words = word_tokenize(text)
    
    # Create a frequency table to keep the score of each word
    freq_table = dict()
    for word in words:
        word = word.lower()
        if word in stop_words:
            continue
        if word in freq_table:
            freq_table[word] += 1
        else:
            freq_table[word] = 1

    # Create a dictionary to keep the score of each sentence
    sentences = sent_tokenize(text)
    sentence_value = dict()
    
    for sentence in sentences:
        for word, freq in freq_table.items():
            if word in sentence.lower():
                if sentence in sentence_value:
                    sentence_value[sentence] += freq
                else:
                    sentence_value[sentence] = freq

    # Calculate the average score of a sentence
    sum_values = sum(sentence_value.values())
    average = int(sum_values / len(sentence_value))

    # Store the summary sentences
    summary = ''
    for sentence in sentences:
        if sentence in sentence_value and sentence_value[sentence] > (1.2 * average):
            summary += " " + sentence

    # Optionally limit the number of sentences in the summary
    summary_sentences = sent_tokenize(summary)
    if len(summary_sentences) > num_sentences:
        summary = ' '.join(summary_sentences[:num_sentences])

    return summary

# Example usage
transcript = """
Machine learning. It's crazy.
Like right now I'm running a machine      
learning model that will tell me how bad I
suck at video games in real time. But     
honestly I don't think it's very accurate.
Nevermind. It's pretty accurate. So       
machine learning, it's hot right now.     
It's the future Chad's, G P
T, all the buzzword, you know,
and it's how you ended up watching this   
video. Thank you YouTube algorithm.       
Love you. And I'm making this
video because I wanna tell you,
you can absolutely learn this
technology. You don't need a degree,      
you don't need to be a math genius        
and you can learn this all for free.      
This video game thing,
you're actually gonna set this up yourself
by the end of this video using all        
the crazy machine learning data science   
tools in the Oracle Cloud or oci and it   
will be completely free thanks to
our sponsor Oracle. And by the way,       
you'll find out that if you do wanna      
get started with machine learning,        
this right here is the best way to start. 
Just jump in and stink and do it using    
real tools that real data scientists and  
machine learning engineers actually use.  
I'm telling you about machine learning,   
but I'm not a machine learning engineer.  
Why should you listen to me? Santiago,    
he's a machine learning engineer. In fact,
you know that dog spot from
Boston Dynamics jumps around,
sees things sometimes
piece beer into a cup,
Santiago's on the team
that makes that happen.
It's machine learning and specifically    
it's called computer vision. We.
Build computer vision algorithms
to help the robot see the.
World. And also Nacho, he's
a machine learning engineer.
He's the guy who's gonna help you get     
set up with that machine learning video   
game thing later on.
I created like three workshops and the    
idea is to get started on the most basic  
concepts that I found out that
are, you know, most important in,
in machine learning.
And they're both gonna help me explain    
the wonders of machine learning and how   
you can get started down this kind of     
crazy and extremely lucrative career path.
I mean talk about future
proof dude. And by the way,
I'm obsessed with machine learning        
now. I can't stop playing with it.        
So thanks a lot Oracle. But
before we get into that,
let's first define what the junk
even is. Machine learning. Santiago,      
what is machine learning?
Machine learning is
Teaching a computer how to learn from     
data. Like if you're a software developer,
you're used to uh,
craft a set of rules in order
to accomplish something, right?
Let's say you want to play
tic-tac toe, you will uh,
create rules like if the computer
plays here, I'm gonna play there.
If the other player plays here, right?
You will craft those rules. You will use,
uh, loops and conditions and any
programming, uh, tools that you have.
Mm-hmm  machine learning
is a little bit different and it turns
this on its head. So machine learning
starts with uh, a lot of samples,
right? It's like hey,
this is the temperature over a
year for this particular region.
Can you craft the rules
automatically in order
to predict what the temperature
will be tomorrow? So.
We're teaching a computer to do something
without us explicitly telling it to do
something. If you're like me,
you're like, uh, what ,
what does that mean exactly? What's
the process? How does that work?
Let me give you one quick
example before we dive in.
We'll start by defining our, what
do we want to teach the computer?
And I wanna teach how to
identify a photo of me.
Is this a photo of network chuck?
Yes or no? But how do we do that?
How do we teach it to recognize
me data, the answer's data,
we give it a ton of pictures
of me, different pictures,
me doing this and that.
Then nah, you know,
all kinds of stuff and we'll label it so
it knows it's me and while we're at it,
it also might help to see photos of not
me so we can know what to not look for.
So we'll get a bunch of those of
not me with our data assembled.
We can now train our computer.
He's in training, he's a trainee.
But hold up before we can teach him, we
have to choose how he's going to learn.
And that's called our
machine learning algorithm.
There are a lot out there
doing some crazy math,
but I think the one we want will
be a convolutional neural network.
Now do I know how that works? No.
But do I know that it might be
good for the situation? Yes.
So now we spoon feed the data and the
algorithm will start to learn to start
recognizing the pattern of me.
Every time it sees a beard or
crazy eyes or a man bun, it'll say,
oh you know what? I'm gonna weigh that
feature higher. Or if it doesn't see one,
it'll lower it and it will crunch
through all this data learning me.
And then for good measureable
feed to pictures of not me,
so it knows what to not
look for. And now he's done,
he finished the training data,
he's no longer a trainee.
Now we can test him with testing
data to see how he performs.
Now while this example is very simple,
that's all a machine learning model is,
which is what we just make.
It's a file that's been trained to
recognize certain types of patterns.
Now it could happen that your machine
learning model sucks and its accuracy is
like 10%. That's where being a machine
learning engineer comes into play.
You have to learn what to do to
make that model more accurate.
You have to learn those skills and I'm
gonna show you how to do it right now.
Now according to Santiago,
the first step in learning machine
learning is just to start doing.
It.
I prefer the style of teaching and
learning where you start writing the
deep end and then you
start unpacking things,
breaking down pieces and say, okay,
I need this in order to
understand this particular piece.
Let me go and watch a that
video. Or I need this. Uh,
I do not understand exactly
how the chain rule works.
Let me just pick up this video,
go to YouTube or whatever.
I'm gonna understand that
and then I can move on.
That's the way I would recommend
people to approach this.
So let's just start doing it, shall we?
Let's build a machine learning algorithm
that can tell you how bad you suck at
video games. Check the link below.
Let's get signed up for a free Oracle
cloud account. Oci. And by the way,
signing up for OCI right now means you
get a $300 credit to do whatever you
stink and want with within reason more
than enough to play with this machine
learning stuff. So once
you have your account,
we got three delicious labs to go through.
I created like three
workshops that are uh,
you can do them on your own about
uh, one hour and a half to two hours.
And the idea is to get started on the
most basic concepts that I found out.
And they cover everything
from data extraction,
getting your data ready
like we do with the photos,
to actually building models with
different tools. Psych kittle, learn,
auto glue on even building a neural
network who can say they built a neural
network. You can after this
thing you're doing coffee break.
The first one I'm gonna start
with is data extraction.
The CUS is gonna teach you a ton about
data science as we're walking through
this. Once you got it loaded up,
go ahead and click on start and
then click on run on your tendency,
which just means you're gonna be running
on your own OCI stuff cuz you have free
account.
Now you probably guessed that the video
game we're talking about is League of
Legends. It's kind of a complex game.
It's you playing with four other players
to try and destroy the other player's
base essentially. And there are a
lot of factors that come into play.
What character you choose, the
potions and nerdy stuff you might buy,
how much gold you collect, uh, all
the stuff that happens in the match.
All those are in things that are
important features that might determine if
you're going to win or lose.
And it's in this lab we learn how to
identify those features and feed it into a
machine learning algorithm.
It's kind of crazy.
Now if you are following
along with this lab,
the first thing you wanna do is
set up your infrastructure in oci.
We'll be using a lot of stuff there.
Data science cloud, shell compute,
autonomous js o database. Offer free
offer fun. No, it really is pretty cool.
Oh,
and one more thing you wanna do is you'll
wanna sign up for League of Legends
because you're gonna get an API key to
pull all kinds of data from previous
matches and live matches as
you're playing. It's free,
it's easy just you'll link below, you'll,
you'll follow it along
for the infrastructure.
We're doing all of this deploy
with Terraform and Ansible.
Nacho gives you all the code,
everything in this walkthrough.
You don't have to worry about a
thing, just click, click, click.
You probably won't even know what's
happening half the time and that's fine.
You're just deploying infrastructure.
Just follow directions.
I'm gonna do mine right now.
Now number two,
the next thing you'll want to do to become
a machine learning engineer and that
is to learn why the junk data science.
Like why do we do it? What is it?
What's the process?
The first thing you wanna do is hang out
with nacho nacho's gonna hold your hand
and show you what it's like to actually
tackle a real world machine learning
problem. And using the OCI hands-on labs,
you'll get hands-on to
actually do this yourself.
And this is so cool because you get a
chance to see how a machine learning
engineer thinks how they
approach a problem. Shoot,
he's got five articles detailing it,
every single thing he
does and why he did it.
So if you want to understand the big
what and why of machine learning,
this is like the best place to start.
You're doing it and he's telling you why.
And if you need a bit
more, which I often do,
there is some structure learning out
there for how to understand the whole
machine learning process.
Santiago recommends brilliant. If.
You are like from the
very, very, very beginning,
like you've never seen this, you,
you don't even know where to start,
I would recommend brilliant.
They have a data science
path that's fantastic.
It'll help you to start
thinking like a data scientist.
Now this is for you if you're
very brand new to data science,
like you
"""

summary = summarize_text(transcript)
print(summary)
