/*
Main.java (BMP24to16): converts bmp rgb24 to rgb16

Copyright (C) 2019-2020 Sean Stafford (a.k.a. PyroSamurai)

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
*/
import java.io.*;
import java.nio.*;
import java.nio.file.*;
import static java.lang.System.out;

public class Main
{
    //class variables
    private static ByteBuffer bb;
    private static String original,newName,dir,fs=File.separator;
    private static byte[] bmp;
    // main
    public static void main(String[] args)
    {
        try
        {
            JBL bl = new JBL();
            for(int i=0; i < args.length; i++)
            {
                original = args[i];
                newName  = args[i].substring(0,args[i].length()-4)+"_16";
                File orig = new File(original);
                if(orig.exists())
                {
                    dir = orig.getParent()+fs;
                    if(dir.equals("null"+fs))
                        dir = System.getProperty("user.dir")+fs;
                }

                bl.setFileVars(dir,newName);
                //bl.set16BitFmtIn("RGB555");
                //bl.setBitFmtOut("RGB24");
                bl.setBitFmtOut("RGB565");

                byte[] ba = Files.readAllBytes(orig.toPath());
                bl.getBitmapVars(ba);
                bb = ByteBuffer.wrap(ba).order(ByteOrder.LITTLE_ENDIAN);
                bb.position(bl.dataStart);
                byte[] rawBytes = bl.getImgBytes(bb,0);
                byte[] stripped = bl.stripPadding(rawBytes);
                //byte[] pixels   = bl.toStdRGB(rawBytes);
                byte[] pixels   = bl.toStdRGB(stripped);
                boolean flip = false;
                boolean topDown = false;
                // Only needed on bitmaps that were not written correctly
                if(topDown)
                    bmp = bl.setBMP(bl.reverseRows(pixels),flip);
                else
                    bmp = bl.setBMP(pixels,flip);
                bl.makeBMP(bmp);
            }
        }
        catch(Exception ex)
        {
            out.println("Error in (Main):\n"+ex);
        }
    }
}
