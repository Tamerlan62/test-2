int[] array = { 2, 4, 6, 8, 10, 30, 70, 100, 10, 10 };
int minRange = 10;
int maxRange = 90;
int count = 0;

for (int i = 0; i < array.Length; i++)
{
    if (array[i] >= minRange && array[i] <= maxRange)
    {
        count++;
    }
}
System.Console.Write(count);