package com.example.helper;


public class ArrayList{
    private int size = 1;
    private Object[] arrayList;

    public ArrayList() {
        arrayList = new Object[size];
    }

    public void insert(Object value){
        if (arrayList[size-1] != null){
            size++;
            Object[] copyArray = createCopyOfArray(this.arrayList);
            this.arrayList = new Object[size];
            shiftCopiedElementsToTheNewIncreasedLengthArray(copyArray, this.arrayList);
        }
        this.arrayList[size-1] = value;
    }

    public Object get(int index){
        if(index >= size) {
            return null;
        }
        return this.arrayList[index];
    }

    private static Object[] createCopyOfArray(Object[] originalArray){
        Object[] copyArray = new Object[originalArray.length];
        for(int i=0; i<originalArray.length; i++){
            copyArray[i] = originalArray[i];
        }
        return copyArray;
    }

    private static void shiftCopiedElementsToTheNewIncreasedLengthArray(Object[] copyArray, Object[] newArray){
        for(int i=0; i < copyArray.length; i++){
            newArray[i] = copyArray[i];
        }
    }

    public Object[] getArrayList() {
        return arrayList;
    }
}
