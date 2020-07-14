# A simple wrapper for sending whatsapp messages with twilio

## Usage 

* clone the repo 

* create a ` .env file `

    * There are three enviroment variables that need to be set
        -  TWILIO_ACCOUNT_SID='YOUR_ACCOUNT_SID'
        -  TWILIO_AUTH_TOKEN='YOUR_AUTH_TOKEN'
       -   FROM='-------'

* install the dependencies ` pip install -r requirements.txt `

### now you can import the script along with the ` .env file `

## Example

```python 

from script import TwilioMessanger

# to send a message call the send() method 

message  = 'some random message'
recipeint = 'some_recepients_number'

TwilioMessanger.send(message,recepient)

# this should  return True if all went well 

```

### feel free to make a PR or create an issue if you find a bug or have a feature request


## leave a star :grin: