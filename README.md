# crypto-tracker
Track the growth of the top cryptocurrencies effortlessly

### crypto-tracker.ipynb
This Python script allows you to track the growth of the top cryptocurrencies (Bitcoin, Ethereum, Ethereum Classic, Ripple, Litecoin, Dash, NEO, EOS and Lisk) on your local computer with a press of a button.  

If you would like to automate the process:
   1. Create a Windows batch file that calls the python script and your favourite program that you use on a daily basis. This can be done simply by typing the following:
  
            @echo off
            python <\link to the python file>
            start <\link to your favourite program>
    2. Create a shortcut of the program that is linked above.
    3. Set the address of the shortcut to the batch file we just created.

Now everytime you open your favourite program, you are indirectly calling the python script which is collecting and saving data for you.

### crypto-tracker-util-tool.py
In the event you forgot to run the main script on a daily basis, you can use the terminal to interact with this script to fill in missing data.
        
        python crypto-tracker-util-tool.py 3-12-2017 1-12-2017 2-12-2017

This  will fill in the mssing data for dates: 1st, 2nd and 3rd of December 2017
