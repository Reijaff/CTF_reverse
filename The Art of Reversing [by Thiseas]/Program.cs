using System;

public class Program
{
    static public int nToStop;
    static public int nCounter;
    static public bool bContinue = true;
    static public string ssOut = "";

    static private void Do(ref char a, ref char b)
    {
        if (a == b)
        {
            return;
        }
        a ^= b;
        b ^= a;
        a ^= b;
    }

    // Token: 0x06000003 RID: 3 RVA: 0x00002094 File Offset: 0x00000294
    static public void GetPer(char[] word)
    {
        int m = word.Length - 1;
        GetPer(word, 0, m);
    }

    // Token: 0x06000004 RID: 4 RVA: 0x000020B0 File Offset: 0x000002B0
    static public void GetPer(char[] word, int k, int m)
    {
        if (!bContinue)
        {
            return;
        }
        if (k == m)
        {
            nCounter++;
            if (nCounter == nToStop)
            {
                ssOut = new string(word);
                bContinue = false;
                return;
            }
        }
        else
        {
            for (int i = k; i <= m; i++)
            {
                Do(ref word[i], ref word[k]);
                GetPer(word, k + 1, m);
                Do(ref word[i], ref word[k]);
            }
        }
    }

    // Token: 0x06000005 RID: 5 RVA: 0x00002139 File Offset: 0x00000339
    static public int nPr(int n, int r)
    {
        return FcDv(n, n - r);
    }

    // Token: 0x06000006 RID: 6 RVA: 0x00002148 File Offset: 0x00000348
    static private int FcDv(int topFc, int divFc)
    {
        int num = 1;
        for (int i = topFc; i > divFc; i--)
        {
            num *= i;
        }
        return num;
    }

    // Token: 0x06000007 RID: 7 RVA: 0x00002168 File Offset: 0x00000368
    static private int Fc(int i)
    {
        if (i <= 1)
        {
            return 1;
        }
        return i * Fc(i - 1);
    }



    public static void Main()
    {
        nToStop = 0;
        nCounter = 0;
        bContinue = true;
        ssOut = "";


        string text = "1234";
        int num2 = nPr(text.Length, text.Length);
        nToStop = num2 / 2;
        char[] word = text.ToCharArray();
        int m = word.Length - 1;
        GetPer(word, 0,m);


        Console.WriteLine(ssOut);
    }
}

