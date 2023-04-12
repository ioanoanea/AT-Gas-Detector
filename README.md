# Gas Detector
This gas detector is a simple smart home system that detects gas leaks. 
The sample captures the gas leaks with a gas sensor connected to an Arduino. 
When a gas leak is detected, the user is notified with a push notification on the mobile phone.

# Screenshots
[![Watch the video](https://i9.ytimg.com/vi/Vu_BIzrB8mc/mqdefault.jpg?sqp=CLis2qEG-oaymwEmCMACELQB8quKqQMa8AEB-AH-CYAC0AWKAgwIABABGGUgXihSMA8=&rs=AOn4CLDshaPFa0YQ_V2CpmfuQyQLkL9gRQ)](https://www.youtube.com/watch?v=Vu_BIzrB8mc)
</br>
Demo: [watch the video](https://www.youtube.com/watch?v=Vu_BIzrB8mc)

# Pre-requisites
- Android Things compatible board (Arduino Uno)
- Gas detector sensor 
- resistor
- led
- Arduino IDE
- Android Studio
- Python 3.9
- Firebase console account

# Setup and Build
Connect + and - pins from the sensor to the Arduino board and the analog pin to one of Arduino's analog pins
</br>
Connect the led to the digital board's pins using a resistor.
</br>
Create and upload code to Arduino board.
</br>
</br>
Create a new Android project. 
Create a new project in the Firebase console and register the Android app and download the google-services.json 
and save it in the Android project directory. Generate an API key for the project. 
</br>
</br>
Configure Firebase in Android project : Tools -> Firebase -> Cloud Messaging -> Set up Firebase Cloud Messaging
</br>or</br>
Manual configuration: [https://firebase.google.com/docs/android/setup](https://firebase.google.com/docs/android/setup)
</br>
</br>
Configure Cloud Messaging in Android projecct:
</br>
Create a new service that extends FirebaseMessagingService()
</br>
in service class overide these two methods:
</br>
```Kotlin
class FirebaseMessagingManager : FirebaseMessagingService() {

    override fun onNewToken(token: String) {
        // save the token
        super.onNewToken(token)
    }

    override fun onMessageReceived(message: RemoteMessage) {
        super.onMessageReceived(message)
        // do your stuff here 
    }
}
  
```
Add service to AndroidManifest:
```XML
 <service android:name=".fcm.FirebaseMessagingManager"
            android:exported="false">
            <intent-filter>
                <action android:name="com.google.firebase.MESSAGING_EVENT" />
            </intent-filter>
 </service>
```
Also add these tags in AndroidManifest:

```XML
<meta-data
    android:name="com.google.firebase.messaging.default_notification_icon"
    android:resource="@drawable/ic_warning" />
<meta-data
    android:name="com.google.firebase.messaging.default_notification_color"
    android:resource="@color/red" />
```

And the internet permission:
```XML
<uses-permission android:name="android.permission.INTERNET" />
```
Official documentation: [https://firebase.google.com/docs/cloud-messaging/android/client](https://firebase.google.com/docs/cloud-messaging/android/client)
</br>
</br>
Create a Python script to capture the Arduino serial and send a notification to the phone.
```
import serial

arduino = serial.Serial('COM7', 9600, timeout=1)
```
</br>
To send firebase notification send a post call to: https://fcm.googleapis.com/fcm/send
</br>
</br>
In headers incude the API key previously generated.
</br>
```
headers = {
    'Authorization': 'key=' + api_key,
    'Content-Type': 'application/json'
} 
```
</br>
</br>
Documentation: https://firebase.google.com/docs/cloud-messaging/send-message#python

# Running
Install the android app to a phone.
</br>
Connect the Arduino board to the pc.
</br>
Run the python script.
