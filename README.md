# UploadCPE
![1](https://user-images.githubusercontent.com/70975465/209453644-04e682a8-e3a3-4563-89e4-96806cd77c5e.jpg)



### Project summary

This is an Python script automation to replace labor-intensive process to manually submit for CPA license renewals in Washington state.
It automates the extraction of key attributes (hours, date, education provider) from PDFs and fills out the online form.
![3](https://user-images.githubusercontent.com/70975465/209453656-a03d33a6-a92d-4798-9af7-d4f52e3afbaf.jpg)



With 10 clicks/text fields per form and average of 120 forms per renewal, resulting in potentially saving 13,000 hours and
$2.6M in billable hours (2+ hours per renewal and 6500+ CPAs in Washington with average at $200 per hour rate).

![2](https://user-images.githubusercontent.com/70975465/209453650-301a2243-fa48-4299-995d-dc91791d0797.jpg)


### Prerequisites

* [PyCharm](https://www.jetbrains.com/pycharm/) - Python IDE
* [Chrome](https://www.google.com/chrome/dr/download/?brand=JJTC&gclid=EAIaIQobChMI-rP-tc2R_AIVIB6tBh0KCAd2EAAYASAAEgL09_D_BwE&gclsrc=aw.ds) - Web Browser
* [Selenium](https://www.selenium.dev/) - Selenium Webdriver

### Installation 

Step 1: Download PyCharm IDE or other Python IDE

https://www.jetbrains.com/pycharm/

Step 2: Download Chrome and check the version

https://www.google.com/chrome/dr/download/?brand=JJTC&gclid=EAIaIQobChMI-rP-tc2R_AIVIB6tBh0KCAd2EAAYASAAEgL09_D_BwE&gclsrc=aw.ds

Step 3: Install HomeBrew

https://docs.brew.sh/Installation

Step 4: Download Chromedriver (using MacOS terminal)

Update Homebrew

```
brew update
```

Install Chromedriver

```
brew install chromedriver --cask
```

Check if your chromedriver is the compatible with the Chrome version

```
chromedriver -v
```


Note: If older version of Chromedriver exists and you may to remove it prior to installing the updated version

find out where chromedriver is installed

```
which chromedriver
```

remove with rm location

```
rm /usr/local/bin/chromedriver
```

Step 5: Install packages

```
pip install pytesseract
```

```
pip install pdf2 image
```

```
pip install python-poppler
```

### Deployment

Step 1: Download the code from [UploadCPE](https://github.com/bonniewt/UploadCPE)

Step 2: Load the code into your IDE

Step 3: To run the code. 


## Additional information

### Tools used!

[4](https://user-images.githubusercontent.com/70975465/209453661-097e3677-c9dc-4146-b095-2f4282cbcc23.jpg)


Form Filler:

* [PyCharm](https://www.jetbrains.com/pycharm/) - Python IDE
* [Selenium](https://www.selenium.dev/) - Selenium Webdriver
* [ChromeDriver](https://chromedriver.chromium.org/downloads) - ChromeDriver


Test Dataset Generator: 

* [Python Faker](https://faker.readthedocs.io/en/master/) - Python Package to generate fake data
* [PyCharm](https://www.jetbrains.com/pycharm/) - Python IDE

### License

MIT License

Copyright (c) 2022 UploadCPE

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

