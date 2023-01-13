# Software Requirements

• What is the vision of this product?

> To create a useful tool that can be utilized by many developers to learn how to be more effective in their coding abilities.

• What pain point does this project solve?

> Provides condensed technical information in a more readable/digestible way
> Saves time researching through long articles

• Why should we care about your product?

> It makes learning easier!
> It's a great learning tool for all devs in any experience level.

## Scope IN

> Takes in an article on coding and regurgitates it to a simplified, more readable version.
> Scrapes google web result for a search term
> Processes web result through GPT3 to summarize the article
> Provides options to find another article or launch website

## Scope OUT

> You will not be able to save your results in a database
> It will analyze quality of the article

## MVP

> Returns summarizes results of scraped article

> Stretch: 
> User ability to navigate to article 
> Provides sample code

## Functionality

> Input search terms

## Non-Functional Requirements

> Usability
    - user provide an input successfully
    - launch script in terminal
    - prompt for more information

> Testability
    - successfully web scraping google
    - successfully connect to API with get request
    - successfully returns web scraped article
    - prompt shows up after article is successfully displayed