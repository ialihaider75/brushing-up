package com.example;

import com.example.helper.ArrayList;

public class Main {

    public static void main(String[] args) {
        ArrayList arrayList = new ArrayList();
        arrayList.insert("Test String1");
        arrayList.insert("Test String2");
        String myFirstTest = (String) arrayList.get(2);
        System.out.println(myFirstTest);
    }
}
