package ujava;
/*
ubyte.java: this file is part of the ujava library.

Copyright (C) 2020 Sean Stafford (a.k.a. PyroSamurai)

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Lesser General Public License as published
by the Free Software Foundation, either version 3 of the License,
or any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
*/
//import ujava.*;
/**
Class Description:
This is the ubyte class. It mimics an unsigned byte. Hence the lowercase class.

Dev Notes:
Stored input and resulting output is Little-Endian.
*/
public class ubyte
{
    // class variables
    private byte ubyte=(byte)0x00;

    //==========================================================================
    // class constructor with no value.
    public ubyte() {}
    // class constructor with a byte value to be stored
    public ubyte(byte Int)
    {
        set(Int);
    }
    // class constructor with a short value to be stored (lossy)
    public ubyte(short Int)
    {
        set(Int);
    }
    // class constructor with a char value to be stored (lossy)
    public ubyte(char Int)
    {
        set(Int);
    }
    // class constructor with a int value to be stored (lossy)
    public ubyte(int Int)
    {
        set(Int);
    }

    //==========================================================================
    // get() function with a byte value to be returned
    public byte get()
    {
        return ubyte;
    }
    // get() function with a short value to be returned
    public short getS()
    {
        return (short)(ubyte &0xFF);
    }
    // get() function with a char value to be returned
    public char getC()
    {
        return (char)(ubyte &0xFF);
    }
    // get() function with a int value to be returned
    public int getI()
    {
        return (ubyte &0xFF);
    }

    //==========================================================================
    // set() function with a byte value to be stored from a byte
    public void set(byte Int)
    {
        ubyte = Int;
    }
    // set() function with a byte value to be stored from a short (lossy)
    public void set(short Int)
    {
        ubyte = (byte)(Int &0xFF);
    }
    // set() function with a byte value to be stored from a char (lossy)
    public void set(char Int)
    {
        ubyte = (byte)(Int &0xFF);
    }
    // set() function with a byte value to be stored from a int (lossy)
    public void set(int Int)
    {
        ubyte = (byte)(Int &0xFF);
    }
}
