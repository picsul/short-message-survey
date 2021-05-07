# Short Message Survey

*Short Message Survey* is an app for sending out text-based ESM surveys.

## Overview

Short message survey is a python app that uses the Flask web app framework. Flask uses the Twilio API to send out SMS messages using our twilio phone numbers based on whatever criteria we set. Originally this was at set times at regular intervals (e.g. every Wednesday at 8:00 am), but now we can also send out messages triggered by students submitting assignments.

## Use case for the Fall, 2020 semester for the PICSUL project

We set up an Gmail inbox for the project, and through canvas we had emails sent to the inbox every time a student submitted an assignment. Then we have a function that accesses the Gmail inbox and reads through the emails. For each email it finds the name of the person who submitted the assignment, and tries to find their phone number in the database. If it does then it checks to make sure the name of the assignment is correct, and that it’s not a re-submission, and if it clears those checks then it sends an SMS to that person to initiate a survey. If it’s a resubmission, or the name isn’t found, the email is moved to trash. Once the student responds to the SMS that triggers the survey to begin, and the student is asked the survey questions until they are finished or five minutes has elapsed, and then it thanks them for their participation.

## Example

![](screenshot.png)

## License

Copyright 2020 PICSUL

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

## Acknowledgment

This material is based upon work supported by the National Science Foundation under Grant No. 1937700. Any opinions, findings, conclusions, or recommendations expressed in this material are those of the authors and do not reflect the views of the National Science Foundation.
