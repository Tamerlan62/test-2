int[] array = { 2, 5, 2, 3, 6, 3, 7, 8, 2, 4};
int count = 0;

for (int i = 0; i < array.Length; i++)
{
    if (array[i] % 2 == 0)
    {
        count++;
    }
}    
System.Console.WriteLine(count);
