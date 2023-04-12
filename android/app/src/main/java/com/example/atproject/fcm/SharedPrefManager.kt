package com.example.atproject.fcm

import android.content.Context

class SharedPrefManager(context: Context) {
    private val prefs = context.getSharedPreferences(Constants.FCM, Context.MODE_PRIVATE)

    fun getValue(key: String) = prefs.getString(key, null)
    fun putValue(key: String, value: String) = prefs.edit().putString(key, value).apply()

}