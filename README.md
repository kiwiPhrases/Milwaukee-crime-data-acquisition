# Milwaukee Crime Data Acquisition
This code is used to download census tract level crime data from the Milwaukee data repository.
However, the code is modular and thus can be quickly amended to automate downloads of other data from Milwaukee's data repository

## Details:
The city of Milwaukee allows public users to download data from their databases on this [website](http://itmdapps.milwaukee.gov/publicApplication_QD/queryDownload/login.faces). 
This is convenient if one wants to download highly specific data but acquiering city-wide data is not a built-in function
into the application. As a result, I wrote this Python code that uses [Selenium](http://selenium-python.readthedocs.io/) to facilitate the 
process. 

The code is not fully automated which is fine for infrequent or one-time bulk downloads (and it saves me a lot of overhead). 
The code is presently used to download data from the "Census Tract" tab on the application website but by modifying the 
tab link, you can download from many other tabs such as "Police District", "Zip Code", and "Whole City".

The crux of the function is that the user fills out query form in the browser itself
and then the function finishes the job by iterating over the desired geographies to obtain
data on the whole city at a particular geographic level. 


