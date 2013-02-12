The goal of this project is to visually represent a user's email. In lieu of using my personal email account, I used the Enron corpus located at http://arg.vsb.cz/arg/Enron_Corpus/.

View the visualization: http://bl.ocks.org/d/4760914/

The visualization is made with D3.js (http://d3js.org), and is extended from the Force-Directed Graph implementation.

The Python script jsonbuilder.py, when run, will create the emaildata.json file to be read by the Javascript in index.html. It can be run by typing in the terminal:
./jsonbuilder.py emailID, where emailID is an ID found in PersonList.xml, such as 64610, which corresponds to a user.

Opening index.html in an email browser will open the visualization.

Mousing over each node reveals the user each node represents. The size of each node represents the total emails sent/received to that user.
