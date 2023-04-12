package com.example.atproject.fcm

import android.content.Intent
import android.util.Log
import android.widget.Toast
import com.example.atproject.MainActivity
import com.google.firebase.messaging.FirebaseMessagingService
import com.google.firebase.messaging.RemoteMessage

class FirebaseMessagingManager : FirebaseMessagingService() {

    override fun onNewToken(token: String) {
        val sharedPrefManager = SharedPrefManager(applicationContext)
        sharedPrefManager.putValue(Constants.FCM_TOKEN, token)
        super.onNewToken(token)
    }

    override fun onMessageReceived(message: RemoteMessage) {
        super.onMessageReceived(message)
        val title = message.notification?.title
        val body = message.notification?.body

        val intent = Intent(applicationContext, MainActivity::class.java)
        intent.flags = Intent.FLAG_ACTIVITY_NEW_TASK
        startActivity(intent)

    }
}